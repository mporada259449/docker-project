from django.urls import path
from . import views

urlpatterns = [
    path(r'login/', views.Login.as_view(), name="login"),
    path(r'register/', views.Register.as_view(), name="login"),
]