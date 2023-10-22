from django.urls import path
from . import views

urlpatterns = [
    path('', views.Calc.as_view(), name="calc"),
]