from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer

class LessonListView(generics.ListCreateAPIView):
    """Просмотр всех уроков и добавление нового урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CourseLessonsView(generics.ListAPIView):
    """Просмотр уроков определенного курса"""
    serializer_class = LessonSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Lesson.objects.filter(course_id=course_id)

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление конкретного урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonCreateView(generics.CreateAPIView):
    """Создание нового урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

