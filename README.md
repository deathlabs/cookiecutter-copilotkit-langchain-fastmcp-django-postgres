# `cookiecutter-copilotkit-django-fastmcp-postgres`

[![CI Pipeline](https://github.com/deathlabs/cookiecutter-copilotkit-django-fastmcp-postgres/actions/workflows/ci.yaml/badge.svg)](https://github.com/deathlabs/cookiecutter-copilotkit-django-fastmcp-postgres/actions/workflows/ci.yaml)

A Cookiecutter template for creating a full-stack app consisting of a CopilotKit frontend, Django Ninja backend, FastMCP server, and PostgreSQL database. 

## Quickstart

There are two ways to start using this template. Use Option 1 to create an app for your own project. Use Option 2 to explore the template by cloning the repository and running its Makefile to create, start, and test an example app. 

The instructions below assume you have or will get the following software installed: [Make](https://www.gnu.org/software/make/), [Docker](https://docs.docker.com/get-started/get-docker/), [uv](https://docs.astral.sh/uv/), [Ruff](https://docs.astral.sh/ruff/), [Semgrep](https://semgrep.dev/), [TruffleHog](https://github.com/trufflesecurity/trufflehog), [Hadolint](https://github.com/hadolint/hadolint), [Syft](https://github.com/anchore/syft#installation), [Grype](https://github.com/anchore/grype#installation), [yq](https://github.com/mikefarah/yq), and [cookiecutter](https://github.com/cookiecutter/cookiecutter). Ruff, Semgrep, TruffleHog, Hadolint, Syft, and Grype are used in our development workflow to help identify and reduce security risks introduced by this cookiecutter template.

### Option 1

**Step 1.** Run Cookiecutter against the GitHub repository.

```bash
cookiecutter https://github.com/deathlabs/cookiecutter-copilotkit-django-fastmcp-postgres.git
```

When prompted, either accept the default values or provide your own.

**Step 2.** Open the app you created. 

**Step 3.** Use the Makefile to create, start, and test your app.

```bash
make
```

### Option 2

**Step 1.** Clone the repository.

```bash
git clone https://github.com/deathlabs/cookiecutter-copilotkit-django-fastmcp-postgres.git
```

**Step 2.** Change to the repository directory.

```bash
cd cookiecutter-copilotkit-django-fastmcp-postgres
```

**Step 3.** Use the Makefile to create, start, and test an example app. The Makefile places the created app in the `build` folder, in a subfolder named after the server.

```bash
make
```

**Step 4.** Open the created app in VS Code. Replace `<project-name>` with the name of the server you created.

```bash
code build/<project-name>
```

## Cleaning Up

To stop your app and delete its container images, enter the commands below.

```bash
make stop-containers
make remove-containers
make remove-container-images
```
