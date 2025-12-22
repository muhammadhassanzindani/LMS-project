from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'message': 'LMS API is running',
        'endpoints': {
            'courses': '/api/courses/',
            'admin': '/admin/'
        }
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
]

