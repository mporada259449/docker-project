from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User
from authentication.forms import RegisterForm


#class Login(View):
#    template = "login.html"
#    form = AuthenticationForm
#
#    def get(self, request):
#        return render(request, self.template, {"form": self.form})
#    
#    def post(self, request):
#        self.form = AuthenticationForm(request.POST)
#        if self.form.is_valid():
#            user = authenticate(request=request, username=self.form.username, password=self.form.password)
#            if user is not None:
#                print("zalogowany")
#                login(request, user)
#                data = "User logged"
#        else:
#            data = "User cannot be authenticated"
#        return render(request, {"form": self.form, "data": data})

class Register(View):
    template = "registration/register.html"
    form = RegisterForm

    def get(self, request):
        return render(request, self.template, {"form": self.form})
    
    def post(self, request):
        self.form = RegisterForm(request.POST)
        if self.form.is_valid():
            user = User.objects.create_user(username=self.form.data["username"], password=self.form.data["password1"])
            login(request, user)
            data = "User created"
        else:
            self.form = RegisterForm() 
            data = "Cannot create user. Invalid password or user already exist"

        return render(request, self.template, {"form": self.form, "data": data})
    
class PasswordCHange(PasswordChangeView):
    success_url = "/"
    
#class PasswordChange(PasswordChangeView):
#    template = "registration/password_change_form.html"
#    
#    def get(self, request):
#        form = PasswordChangeForm
#        return render(request, self.template, {"form": form})
#    
#    def post(self, request):
#        form = PasswordChangeForm(request.POST)
#        if form.is_valid():
#            user = request.user
#            print(form.data, user)
#            data = "Password updated" 
#        else:
#            data = "Cannot update user password"
#            form = PasswordChangeForm
#
#        return render(request, self.template, {"form": form, "data": data})
#