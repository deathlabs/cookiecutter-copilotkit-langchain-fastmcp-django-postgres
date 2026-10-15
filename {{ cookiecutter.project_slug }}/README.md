# {{ cookiecutter.project_name }}
[![CI](https://github.com/{{ cookiecutter.github_repository }}/actions/workflows/ci.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_repository }}/actions/workflows/ci.yaml)

{{ cookiecutter.project_description }}

This agent-native example combines a CopilotKit and Next.js frontend, LangGraph inference service, Django Ninja API, FastMCP tools server, and PostgreSQL database. It includes Docker Compose profiles, Helm charts, and custom resource definitions for Zarf and UDS packages.

See the [project documentation](https://{{ cookiecutter.github_organization }}.github.io/{{ cookiecutter.__github_repository_name }}/) for architecture, setup, and deployment details.

## Local development

Review the `.env.example` file in each service directory. Set a valid `OPENAI_API_KEY` in `inference/.env.example` or copy the examples to `.env` files and run Make with `ENV_FILE=.env`.

Build, scan, start, and test all five services:

```bash
make
```

Use `DOCKER_COMPOSE_PROFILE` to work with a smaller service group. For example, start the database and backend services with:

```bash
make DOCKER_COMPOSE_PROFILE=backend start-containers
```

The frontend is available on port 8080, inference on port 8001, the backend on port 8000, FastMCP tools on port 8002, and PostgreSQL on port 5432.
