from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),  
    path("api/courses/", include("courses.urls")),  
    path("api/lessons/", include("lessons.urls")),  
    path("auth/", include("users.urls")),
]
