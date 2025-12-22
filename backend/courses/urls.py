"""
URL Configuration - Similar to FastAPI router registration

This file maps URLs to views, similar to FastAPI's app.include_router()
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet

# Create router (similar to FastAPI APIRouter)
router = DefaultRouter()

# Register ViewSet (similar to app.include_router() in FastAPI)
# This automatically creates routes for: list, create, retrieve, update, destroy
router.register(r'courses', CourseViewSet, basename='course')

# URL patterns (similar to FastAPI route definitions)
urlpatterns = [
    path('', include(router.urls)),
]
