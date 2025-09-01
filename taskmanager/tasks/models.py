from django.db import models
from django.contrib.auth.models import User

from .models_enumeration import TaskStatus, TaskPriority


# Create your models here.
class Task(models.Model):
    """
    Represents a task to be tracked and managed.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False, default="")
    status = models.CharField(
        max_length=20,
        choices=TaskStatus,
        default=TaskStatus.UNASSIGNED,
        db_comment="Can be UNASSIGNED, IN_PROGRESS, DONE or ARCHIVED.",
    )

    priority = models.IntegerField(
        choices=TaskPriority,
        blank=True,
        null=True,
        db_index=True,
        help_text="Optional priority level (Low, Medium, High, Critical).",
    )

    due_date = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
        help_text="Optional deadline for the task.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        User,
        related_name="created_tasks",
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        User,
        related_name="owned_tasks",
        on_delete=models.SET_NULL,
        null=True,
        db_comment="Foreign Key to the User who currently owns the task.",
    )
