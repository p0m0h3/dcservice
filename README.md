# DCSERVICE

`dcservice` or Docker Computation Service is a docker based sand-boxed task processing HTTP API implementation.

It takes a set of defined tools (as docker images) and their respective input and listens for task requests on an HTTP REST API.

It plans to support the following featues:

 * Reading tools from yaml config files
 * Delivering standard input and command line arguments to tasks
 * Delivering input files to tasks
 * Output retreival
 * Output streaming (via websockets)

# Run

Install requirements:

```
pip install -r requirements.txt
```

Or use poetry:

```
poetry install
```

Specify the required environment variables in `.env`. An example file is provided: `.env.example`. It should contain the following variables:

```
DOCKER_HOST=unix:///var/run/docker.sock
TOOLS_DIR=tools
```

Run the `api` app from the main modules with uvicorn:

```
uvicorn main:api
```

Or you can run with docker image: `pouriamokhtari/dcservice`

# License

See `LICENSE.txt`