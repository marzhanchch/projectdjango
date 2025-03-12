from django.shortcuts import render
import random
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from .models import User
from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()

# Регистрация пользователя с подтверждением по email
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            code = random.randint(1000, 9999)
            user.verification_code = code
            user.save()
            
            send_mail(
                "Ваш код подтверждения",
                f"Ваш код: {code}",
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            return Response({"message": "Код отправлен на email"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Подтверждение кода
class VerifyCodeView(APIView):
    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")

        if not email or not code:
            return Response({"error": "Email и код обязательны"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            if user.verification_code == int(code):
                user.is_active = True  # Активируем пользователя
                user.verification_code = ""  # Очищаем код
                user.save()
                return Response({"message": "Аккаунт подтверждён"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Неверный код"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

# Пагинация и просмотр пользователей
class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
