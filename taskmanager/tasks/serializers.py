from rest_framework import serializers
from .models import Task, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "task", "author", "author_username", "content", "created_at", "updated_at"]


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "creator",
            "owner",
            "created_at",
            "updated_at",
            "comments",
        ]
        read_only_fields = ["id", "creator", "created_at", "updated_at"]
