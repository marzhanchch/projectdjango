
from django.urls import path
from .views import RegisterView, UserListView, VerifyCodeView  

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("verify-code/", VerifyCodeView.as_view(), name="verify-code"),  
]
