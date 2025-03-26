from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from outpeer.permissions import IsManager
from .models import Lesson
from .serializers import LessonSerializer

class LessonListView(generics.ListCreateAPIView):
    """Просмотр всех уроков и добавление нового урока (только для аутентифицированных пользователей)"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

class LessonCreateView(generics.CreateAPIView):
    """Добавление уроков только для менеджеров"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsManager]
