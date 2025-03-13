# 📚 Course Selection API System

This is a course selection backend system built with FastAPI, using Poetry for dependency management and Docker for containerization.

## Features

- Teachers can:

  - View available courses
  - Enroll in courses
  - Drop courses

- Students can:
  - Add new courses
  - Update courses
  - Delete existing courses

## Run with Docker

### Build the Docker image

```bash
docker build -t course-api .

```

```bash
docker run -p 8000:8000 course-api
```

API and API doc are now available at:

- http://localhost:8000
- http://localhost:8000/docs

## Run on your local

### Install poetry

```bash
brew install pipx
pipx ensurepath
sudo pipx --global ensurepath
pipx install poetry
```

### Install dependencies

```bash
poetry install
```

```bash
poetry run uvicorn src.app:app --reload
```

Run Tests

```bash
poetry run pytest
```
