from django.urls import path, include
from . import views

urlpatterns = [
    path(r'auth/', include("django.contrib.auth.urls")),
    #path(r'login/', views.Login.as_view(), name="login"),
    path(r'auth/register/', views.Register.as_view(), name="register"),
]