import csv

from django.http import HttpResponse
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer
from .permissions import TaskPermission, CommentPermission


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, TaskPermission]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["priority", "due_date"]
    ordering = ["due_date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        owner_id = self.request.query_params.get("owner")
        if owner_id is not None:
            queryset = queryset.filter(owner__id=owner_id)
        return queryset

    def perform_create(self, serializer):
        # Automatically set the creator to the logged-in user
        serializer.save(creator=self.request.user)

    @action(detail=False, methods=["GET"], url_path="export")
    def export_tasks(self, request):
        """
        Export tasks as csv.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Prepare response with CSV header
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="tasks.csv"'

        writer = csv.writer(response)

        # Write header row
        writer.writerow([
            "ID", "Title", "Description", "Status", "Priority",
            "Due Date", "Owner", "Creator", "Created At", "Updated At"
        ])

        # Write task rows
        for task in queryset:
            writer.writerow([
                task.id,
                task.title,
                task.description,
                task.status,
                task.priority,
                task.due_date,
                task.owner.username if task.owner else "",
                task.creator.username if task.creator else "",
                task.created_at,
                task.updated_at,
            ])

        return response


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermission]

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)
