# TextBook ReSeller

A marketplace for second-hand textbooks: students and pupils sell the textbooks they no longer need to people looking for cheaper copies.

## Status

**Stage 1: project foundation.** The backend skeleton, PostgreSQL in Docker, linters and CI are in place. There are no user-facing features yet.

## Tech stack

- **Backend:** Python 3.13, Django 5.2, Django REST Framework, drf-spectacular (OpenAPI docs)
- **Database:** PostgreSQL 16
- **Frontend (planned):** React, TypeScript, Vite
- **Tooling:** Docker Compose, pytest, ruff, black, pre-commit, GitHub Actions

## Project structure

```
.
├── backend/                 Django project
│   ├── config/              project package: settings (base/dev/prod), urls, wsgi/asgi
│   ├── core/                shared app: health endpoint
│   ├── Dockerfile           development image for the backend
│   ├── .env.example         template for the environment variables
│   ├── requirements.txt     runtime dependencies
│   └── requirements-dev.txt development dependencies (tests, linters)
├── docs/                    requirements, ERD, wireframes
├── .github/workflows/       CI pipeline
├── .pre-commit-config.yaml  pre-commit hooks
└── docker-compose.yml       local services: db and backend
```

## Getting started

### Prerequisites

- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (on Windows with the WSL 2 backend)
- [Python 3.13](https://www.python.org/downloads/), only needed to run Django outside Docker

### 1. Clone the repository

```bash
git clone https://github.com/AtanasI7/TextBook-ReSeller.git
cd TextBook-ReSeller
```

### 2. Create the `.env` file

Copy the template:

```bash
# Linux / macOS
cp backend/.env.example backend/.env

# Windows (PowerShell)
Copy-Item backend\.env.example backend\.env
```

Then edit `backend/.env`:

- `SECRET_KEY`: generate one with
  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
  and put it in single quotes.
- `POSTGRES_PASSWORD`: any password with letters and digits only.

`backend/.env` is listed in `.gitignore` and must never be committed.

### Option A: run everything in Docker

```bash
docker compose up --build
```

In a second terminal, apply the migrations:

```bash
docker compose exec backend python manage.py migrate
```

Run `docker compose up --build` again whenever `requirements*.txt` or the `Dockerfile` change.

### Option B: run Django locally, the database in Docker

```bash
docker compose up -d db

cd backend
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# Linux / macOS: source .venv/bin/activate
python -m pip install -r requirements-dev.txt

python manage.py migrate
python manage.py runserver
```

The database is exposed on host port **5433** (not the default 5432) so that it does not clash with a locally installed PostgreSQL.

### Useful URLs

| URL | What it is |
|---|---|
| http://localhost:8000/api/health/ | Health check, returns `{"status": "ok"}` |
| http://localhost:8000/api/docs/ | Interactive API documentation (Swagger UI) |
| http://localhost:8000/api/schema/ | OpenAPI schema |
| http://localhost:8000/admin/ | Django admin |

## Running the tests

```bash
# locally, from backend/
pytest -v

# or inside Docker
docker compose exec backend pytest -v
```

## Code quality

Install the git hooks once after cloning (from the repository root, with the virtual environment active):

```bash
pre-commit install
```

From then on, ruff, black and a few general file checks run on every commit. To run them on all files manually:

```bash
pre-commit run --all-files
```

## Development workflow

- Every change goes through a pull request linked to an issue (`Closes #<number>`).
- `main` is protected: direct pushes are blocked and CI (lint + tests) must pass before merging.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/), e.g. `feat(api): add health endpoint`.

## Documentation

- [Requirements and plan](docs/requirements.md) (in Bulgarian)
- [ERD](docs/images/erd.png)

## License

[MIT](LICENSE)
