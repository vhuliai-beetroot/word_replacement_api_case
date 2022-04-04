import json
import time
from typing import Optional

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwcrypto import jwe, jwk, jws, jwt

from app import APP_NAME
from app.exceptions import AuthError
from app.settings import settings

auth_scheme = HTTPBearer()


def create_api_token(jti: str) -> str:
    """Create API JWT using jwk4jwt from app settings"""
    key = jwk.JWK.from_json(json.dumps({"k": settings.jwk4jwt, "kty": "oct"}))
    claims = {
        "iss": APP_NAME,
        "jti": jti,
        "iat": int(time.time()),
    }
    token = jwt.JWT(header={"alg": "HS512"}, claims=claims)
    token.make_signed_token(key)
    return token.serialize()


def verify_token(token_text: str) -> Optional[dict]:
    """Verify API JWT with jwk4jwt from app settings"""
    key = jwk.JWK.from_json(json.dumps({"k": settings.jwk4jwt, "kty": "oct"}))
    try:
        st = jwt.JWT(key=key, jwt=token_text)
        return json.loads(st.claims)
    except (
        ValueError,
        jws.InvalidJWSObject,
        jws.InvalidJWSSignature,
        jwt.JWTExpired,
        jwe.InvalidJWEData,
    ):
        ...


def authorized_request(auth_header: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> None:
    """Check if the request is authorized"""
    payload = verify_token(auth_header.credentials)
    if not payload or "jti" not in payload:
        raise AuthError("Invalid Auth Credentials")
