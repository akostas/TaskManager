from rest_framework import viewsets, permissions, filters
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


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermission]

    def perform_create(self, serializer):
        # Automatically set the author to the logged-in user
        serializer.save(author=self.request.user)
