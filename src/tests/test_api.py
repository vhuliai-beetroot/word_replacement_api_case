from fastapi.testclient import TestClient
from starlette import status

from app.application import app as fastapi_app
from app.constants import REPLACEMENT_MAP


def test_get_config(
    client: TestClient,
) -> None:
    url = fastapi_app.url_path_for("get_config")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["Content-Type"] == "application/json"
    assert response.json()["config"] == REPLACEMENT_MAP


def test_replace_words_from_payload(
    client: TestClient,
) -> None:
    url = fastapi_app.url_path_for("replace_words_from_payload")
    response = client.post(
        url, json=dict(input_str="We really like the new security features of Google Cloud")
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.headers["Content-Type"] == "application/json"
    assert (
        response.json()["processed_str"]
        == "We really like the new security features of Google© Cloud"
    )
