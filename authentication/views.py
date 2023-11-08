from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
class Login(View):
    template = "login.html"

    def get(self, request):
        return render(request, self.template)

class Register(View):
    template = "register.html"
    form = UserCreationForm
    def get(self, request):
        return render(request, self.template, {"form": self.form})