# Python + Jenkins CI Starter

This is a minimal, production-quality starter to practice a **local Python dev environment** with **Git** and **Jenkins CI**.

## What you get
- `pyproject.toml` (PEP 621) using **setuptools** and **ruff/black/mypy/pytest** config
- `pre-commit` hooks for fast local linting
- `Jenkinsfile` (Declarative Pipeline) that runs in a **python:3.12** Docker agent
- Sample package under `src/app` and tests in `tests/`
- Makefile for common tasks
- Optional `docker-compose.yml` to run **Jenkins LTS** locally

## Quick start (local dev)

```bash
# 1) Create & activate a virtual env (macOS/Linux)
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
# py -m venv .venv
# .venv\Scripts\Activate.ps1

# 2) Install tools & project (editable)
python -m pip install -U pip
pip install -e ".[dev]"

# 3) Install pre-commit hooks
pre-commit install

# 4) Run checks & tests
make lint
make test
```

## Run Jenkins locally (optional)
Requires **Docker Desktop**.
```bash
docker compose -f jenkins/docker-compose.yml up -d
# Open http://localhost:8080 to finish Jenkins setup
```
Create a **Pipeline** job that points to this repo and uses `Jenkinsfile`.

## Typical workflow
- Work locally → pre-commit keeps style/quality green
- Push to Git → Jenkins runs the same checks on each branch/PR
