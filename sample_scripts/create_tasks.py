"""
Script to populate the database with sample tasks for testing pagination.

Usage:
    1. Enter the Django container:
       docker compose exec django sh
    2. Run the script:
       python sample_scripts/populate_tasks.py
"""

import sys
import os
import django
from random import randint, choice
from datetime import datetime, timedelta

# Setup Django environment
PROJECT_ROOT = "/app/taskmanager"
sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskmanager.settings")
django.setup()

from django.contrib.auth.models import User
from tasks.models import Task, Comment

def create_sample_tasks(n: int = 23):
    """Create `n` sample tasks."""
    # Make sure at least one user exists
    user, _ = User.objects.get_or_create(
        username="testuser",
        defaults={"email": "testuser@example.com", "password": "testpass"}
    )

    statuses = ["UNASSIGNED", "IN_PROGRESS", "DONE", "ARCHIVED"]

    for i in range(1, n + 1):
        task = Task.objects.create(
            title=f"Sample Task {i}",
            description=f"This is a sample description for task {i}.",
            status=choice(statuses),
            priority=randint(1, 5),
            due_date=datetime.now() + timedelta(days=randint(1, 30)),
            creator=user,
            owner=user if randint(0, 1) else None
        )

        # Add 0-3 comments per task
        for j in range(randint(0, 3)):
            Comment.objects.create(
                task=task,
                author=user,
                content=f"Comment {j+1} for task {i}",
            )

    print(f"{n} sample tasks created successfully.")

if __name__ == "__main__":
    create_sample_tasks()
