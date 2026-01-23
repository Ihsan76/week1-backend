# config/urls.py

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from auth_app import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth_app.urls')),
    # Auth endpoints
    path('api/auth/register/', auth_views.register, name='register'),
    path('api/auth/login/', auth_views.login, name='login'),
    path('api/auth/users/', auth_views.get_users, name='get_users'),
    path('api/auth/users/<int:user_id>/delete/', auth_views.delete_user, name='delete_user'),

    # Courses endpoints
    path('api/courses/', auth_views.courses_list_create, name='courses_list_create'),
    path('api/courses/<int:course_id>/delete/', auth_views.course_delete, name='course_delete'),
]
