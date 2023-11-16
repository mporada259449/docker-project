from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView

urlpatterns = [
    path(r'auth/password_change/', PasswordChangeView.as_view(success_url = '/'), name="password_change"),
    path(r'auth/register/', views.Register.as_view(), name="register"),
    path(r'auth/login/', LoginView.as_view(), name='login'),
    path(r'auth/logout/', LogoutView.as_view(), name='logout')
]