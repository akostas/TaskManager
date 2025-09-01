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


## Creating a user

1. Enter `taskmanager_app` container:
    ```
    docker exec -ti taskmanager_app sh
    ```
2. Use the provided script to create a user:
    ```
    python sample_scripts/create_user.py --username testuser --email test@test.com --password testpass
    ```

    Expected output: `User 'testuser' created successfully.`

## Task API Endpoints (curl Examples)

All endpoints assume the user testuser exists.

### POST: Create a new task

```
curl -u testuser:testpass -X POST http://localhost:8000/api/tasks/ \
    -H "Content-Type: application/json" \
    -d '{
        "title": "Finish backend API",
        "description": "Implement all CRUD endpoints for tasks",
        "status": "UNASSIGNED",
        "priority": 4,
        "due_date": "2025-09-04T12:00:00Z",
        "owner": null
    }'
```

### GET: Get all tasks

```
curl -u testuser:testpass -X GET http://localhost:8000/api/tasks/
```

### GET: Get a single task

```
curl -u testuser:testpass -X GET http://localhost:8000/api/tasks/1/
```

### PATCH: Partially update a task

```
curl -u testuser:testpass -X PATCH http://localhost:8000/api/tasks/1/ \
    -H "Content-Type: application/json" \
    -d '{
        "status": "IN_PROGRESS",
        "priority": 3
    }'
```

### PUT: Update a task

```
curl -u testuser:testpass -X PUT http://localhost:8000/api/tasks/1/ \
    -H "Content-Type: application/json" \
    -d '{
        "title": "Finish backend API v2",
        "description": "Full update of task fields",
        "status": "IN_PROGRESS",
        "priority": 3,
        "due_date": "2025-09-06T12:00:00Z",
        "owner": null
    }'
```

### DELETE: Delete a task

```
curl -u testuser:testpass -X DELETE http://localhost:8000/api/tasks/1/
```

### Notes:
- Replace testuser:testpass with your username/password.
- Replace task IDs (1) as needed.
