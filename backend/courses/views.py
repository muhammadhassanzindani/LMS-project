"""
API Views - Similar to FastAPI route handlers

Django REST Framework ViewSet = FastAPI Router
Each method (list, create, retrieve, update, destroy) = FastAPI endpoint function
"""
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from bson import ObjectId
from bson.errors import InvalidId
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ViewSet):
    """
    Course ViewSet - Handles all CRUD operations
    
    Similar to FastAPI router with multiple endpoints:
    - list() = GET /courses/ (get all)
    - create() = POST /courses/ (create new)
    - retrieve() = GET /courses/{id}/ (get one)
    - update() = PUT /courses/{id}/ (update)
    - destroy() = DELETE /courses/{id}/ (delete)
    """
    serializer_class = CourseSerializer

    def list(self, request):
        """
        GET /api/courses/
        List all courses (similar to FastAPI: @app.get("/courses/"))
        """
        try:
            courses = Course.objects.all()
            data = [self._course_to_dict(course) for course in courses]
            return Response({
                'success': True,
                'count': len(data),
                'data': data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            import traceback
            return Response({
                'success': False,
                'error': str(e),
                'traceback': traceback.format_exc() if request.GET.get('debug') else None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        """
        POST /api/courses/
        Create a new course (similar to FastAPI: @app.post("/courses/"))
        """
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            try:
                course = serializer.save()
                return Response({
                    'success': True,
                    'message': 'Course created successfully',
                    'data': self._course_to_dict(course)
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({
                    'success': False,
                    'error': f'Failed to create course: {str(e)}'
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({
            'success': False,
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        GET /api/courses/{id}/
        Get a single course (similar to FastAPI: @app.get("/courses/{id}"))
        """
        try:
            course = self._get_course_by_id(pk)
            return Response({
                'success': True,
                'data': self._course_to_dict(course)
            }, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({
                'success': False,
                'error': 'Course not found'
            }, status=status.HTTP_404_NOT_FOUND)
        except InvalidId:
            return Response({
                'success': False,
                'error': 'Invalid course ID format'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """
        PUT /api/courses/{id}/
        Update a course (similar to FastAPI: @app.put("/courses/{id}"))
        """
        try:
            course = self._get_course_by_id(pk)
            serializer = CourseSerializer(course, data=request.data)
            if serializer.is_valid():
                updated_course = serializer.save()
                return Response({
                    'success': True,
                    'message': 'Course updated successfully',
                    'data': self._course_to_dict(updated_course)
                }, status=status.HTTP_200_OK)
            return Response({
                'success': False,
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response({
                'success': False,
                'error': 'Course not found'
            }, status=status.HTTP_404_NOT_FOUND)
        except InvalidId:
            return Response({
                'success': False,
                'error': 'Invalid course ID format'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        """
        DELETE /api/courses/{id}/
        Delete a course (similar to FastAPI: @app.delete("/courses/{id}"))
        """
        try:
            course = self._get_course_by_id(pk)
            course.delete()
            return Response({
                'success': True,
                'message': 'Course deleted successfully'
            }, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({
                'success': False,
                'error': 'Course not found'
            }, status=status.HTTP_404_NOT_FOUND)
        except InvalidId:
            return Response({
                'success': False,
                'error': 'Invalid course ID format'
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Helper methods (similar to FastAPI dependency functions)
    def _get_course_by_id(self, course_id):
        """Helper to get course by ID with proper error handling"""
        if not course_id:
            raise ValueError("Course ID is required")
        try:
            return Course.objects.get(id=ObjectId(course_id))
        except (InvalidId, ValueError):
            raise InvalidId("Invalid course ID format")

    def _course_to_dict(self, course):
        """Convert course document to dictionary for JSON response"""
        return {
            'id': str(course.id),
            'title': course.title,
            'description': course.description,
            'instructor': course.instructor,
            'created_at': course.created_at.isoformat() if course.created_at else None,
            'updated_at': course.updated_at.isoformat() if course.updated_at else None
        }
