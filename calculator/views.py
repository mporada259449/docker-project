from django.shortcuts import render

def calc(request):
    template = "calc.html"
    return render(request, template)
