# `cookiecutter-copilotkit-langchain-fastmcp-django-postgres`

[![CI Pipeline](https://github.com/deathlabs/cookiecutter-copilotkit-langchain-fastmcp-django-postgres/actions/workflows/ci.yaml/badge.svg)](https://github.com/deathlabs/cookiecutter-copilotkit-langchain-fastmcp-django-postgres/actions/workflows/ci.yaml)

A Cookiecutter template for creating an agent-native app consisting of a CopilotKit and Next.js frontend, LangGraph inference service, FastMCP tools server, Django Ninja backend, and PostgreSQL database.

## Quickstart

There are two ways to start using this template. Use Option 1 to create an app for your own project. Use Option 2 to explore the template by cloning the repository and running its Makefile to create, start, and test an agent-native app.

The instructions below assume you have or will get the following software installed: [Make](https://www.gnu.org/software/make/), [Docker](https://docs.docker.com/get-started/get-docker/), [uv](https://docs.astral.sh/uv/), [Ruff](https://docs.astral.sh/ruff/), [Semgrep](https://semgrep.dev/), [TruffleHog](https://github.com/trufflesecurity/trufflehog), [Hadolint](https://github.com/hadolint/hadolint), [Syft](https://github.com/anchore/syft#installation), [Grype](https://github.com/anchore/grype#installation), [yq](https://github.com/mikefarah/yq), and [cookiecutter](https://github.com/cookiecutter/cookiecutter). Ruff, Semgrep, TruffleHog, Hadolint, Syft, and Grype are used in our development workflow to help identify and reduce security risks introduced by this cookiecutter template.

### Option 1

**Step 1.** Run Cookiecutter against this GitHub repository.

```bash
cookiecutter https://github.com/deathlabs/cookiecutter-copilotkit-langchain-fastmcp-django-postgres.git
```

When prompted, either accept the default values or provide your own.

**Step 2.** Open the app you created. Review each service's `.env.example` file and then create a `.env` for each service according to your needs. 

**Step 3.** Use the Makefile to check, scan, build, and start the five service application. The default target stops the containers and removes their images after startup completes.

```bash
make
```

### Option 2

**Step 1.** Clone the repository.

```bash
git clone https://github.com/deathlabs/cookiecutter-copilotkit-langchain-fastmcp-django-postgres.git
```

**Step 2.** Change to the repository directory.

```bash
cd cookiecutter-copilotkit-langchain-fastmcp-django-postgres
```

**Step 3.** Use the Makefile to create, start, and test an agent-native app. The Makefile places the created agent-native app in a subfolder named after the app within the build folder.

```bash
make
```

**Step 4.** Open the created app in VS Code. Replace `<project-name>` with the project slug you created.

```bash
code build/<project-name>
```

## Cleaning Up

To stop running containers while keeping their images, run the command below.

```bash
make stop-containers
```

To stop the containers and delete their images, run the command below. 

```bash
make remove-container-images
```
