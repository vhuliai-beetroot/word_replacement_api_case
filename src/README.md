### Python FastAPI service for word replacement api case

Project was built using Ubuntu 20.04 LTS and Python 3.9.1.
The main stack for the local environment is:

* poetry==1.1.8

Install poetry using [this link](https://python-poetry.org/docs/)

To bootstrap local environment for the project we suggest using Makefile,
to get a full list of available commands run `make help`.

### Development environment

1. Export `WR_JWK4JWT` env variable to export JSON Web Key, which will be use for 
generating a JWT to authorize requests to API. 
2. Run `make install` to setup local Poetry python virtualenv
3. Run `make generate_token` to generate JWT token, which will be printed into stdout.
4. Run application:
   
    4.1 `make local_run` will start web server locally
    
    4.2 `make docker_build` - to build image and `make docker_run` to run container app locally.


You may setup extra environment variables, which will be used by application like
`WR_DEBUG`, `WR_WORKERS_COUNT` see full list in `app.settings.settings` Python object, where
`WR_` is application env prefix and name for the env variable could be in upper or lower case.