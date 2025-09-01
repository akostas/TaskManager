"""
Script to create a Django user.

Usage:
    Run this script inside your Django project environment:
        python create_user.py

Requirements:
    - Django must be installed
    - This script should be run from the same directory as manage.py
"""
import sys
import os
import django
import argparse

# Add the parent directory (project root) to Python path
PROJECT_ROOT = "/app/taskmanager"
sys.path.insert(0, PROJECT_ROOT)

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskmanager.settings")
django.setup()

from django.contrib.auth.models import User


def create_user(username: str, email: str, password: str) -> User | None:
    """
    Create a regular Django user with the given credentials.

    :param username: str: Username of the new user.
    :param email: str: Email address of the new user.
    :param password: str: Password of the new user (will be hashed automatically).

    :return: User | None: The created Django User object.
    """
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists.")
        return None

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    print(f"User '{username}' created successfully.")

    return user


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Django user.")
    parser.add_argument("--username", required=True, help="Username of the new user")
    parser.add_argument("--email", required=True, help="Email of the new user. It may be dummy.")
    parser.add_argument("--password", required=True, help="Password of the new user")

    args = parser.parse_args()
    create_user(args.username, args.email, args.password)
