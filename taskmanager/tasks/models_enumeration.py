from django.db import models


class TaskStatus(models.TextChoices):
    """
    Enumeration of task statuses.
    """
    UNASSIGNED = "UNASSIGNED", "Unassigned"
    IN_PROGRESS = "IN_PROGRESS", "In Progress"
    DONE = "DONE", "Done"
    ARCHIVED = "ARCHIVED", "Archived"


class TaskPriority(models.IntegerChoices):
    """
    Enumeration of task priorities.
    """
    LOW = 1, "Low"
    MEDIUM = 2, "Medium"
    HIGH = 3, "High"
    CRITICAL = 4, "Critical"
