from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from outpeer.permissions import IsManager
from users.models import Course, User
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_student(self, request, pk=None):
        """Добавить студента в курс"""
        course = self.get_object()
        student_email = request.data.get('email')
        student = get_object_or_404(User, email=student_email)
        course.students.add(student)
        return Response({'status': 'Студент добавлен'})

    @action(detail=True, methods=['post'])
    def remove_student(self, request, pk=None):
        """Удалить студента из курса"""
        course = self.get_object()
        student_email = request.data.get('email')
        student = get_object_or_404(User, email=student_email)
        course.students.remove(student)
        return Response({'status': 'Студент удален'})

class CourseCreateView(viewsets.ModelViewSet):
    """Добавление курсов только для менеджеров"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsManager]
