from django.urls import path
from .views import LessonListView, CourseLessonsView, LessonDetailView, LessonCreateView  # Импортируем LessonCreateView

urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson-list'),  
    path('courses/<int:course_id>/lessons/', CourseLessonsView.as_view(), name='course-lessons'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
]
