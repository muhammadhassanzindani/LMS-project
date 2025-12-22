"""
Serializers - Similar to FastAPI Pydantic models for request/response validation

Serializers handle:
- Input validation (like Pydantic in FastAPI)
- Data transformation
- Response formatting
"""
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.Serializer):
    """
    Course Serializer for API requests/responses
    
    Similar to FastAPI's Pydantic models:
    - Validates input data
    - Transforms data for database
    - Formats response data
    """
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(
        max_length=200,
        required=True,
        help_text="Course title (max 200 characters)"
    )
    description = serializers.CharField(
        required=True,
        help_text="Course description"
    )
    instructor = serializers.CharField(
        max_length=100,
        required=True,
        help_text="Instructor name (max 100 characters)"
    )
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create a new course instance
        Similar to FastAPI's dependency injection for creating objects
        """
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update an existing course instance
        Only updates provided fields (partial update support)
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.instructor = validated_data.get('instructor', instance.instructor)
        instance.save()
        return instance
