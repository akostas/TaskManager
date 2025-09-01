# Task Manager

A simple Django + PostgreSQL project running in Docker.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)

## Environmnetal Variables

This project uses a `.evn` file for configuration.
An example file is provided as `.env_dist`.

1. Copy the template:
```bash
cp .env_dist .env
```

2. Update values as needed (e.g., database name, user or password).

## Quickstart

1. Build the start the containers image:
```bash
docker-compose up --build
```

2. Visit `http://localhost:8000/` to confirm the Django welcome page loads.
3. Verify PostgreSQL is running:
   - Open a shell inside the taskmanager_db container
     ```bash
     docker exec -it taskmanager_db bash
     ```
     or use the Docker Desktop.

   - Connect to the database:
     ```bash
     psql -U taskuser -d taskdb
     ```
     
   - Once inside `psql`, list databases:
     ```sql
     \l
     ```

## Stopping the application

- Press `Ctrl+C` in the terminal where `docker-compose` is running, or run:
```bash
docker-compose down
```

- To also remove the database volume (frest start):
```bash
docker-compose down -v
```