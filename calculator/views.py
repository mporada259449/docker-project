from django.shortcuts import render
from django.views import View
from calculator.calculator import Calculator
class Calc(View):
    template = "calc.html"

    def get(self, request):
        return render(request, self.template)
    
    def post(self, request):
        num1 = int(request.POST.get("first"))
        num2 = int(request.POST.get("second"))
        calc = Calculator(num1, num2)

        if "add" in request.POST:
            return render(request, self.template, {"result": calc.add()})
        elif "subtract" in request.POST:
            return render(request, self.template, {"result": calc.subtract()})
        elif "multiply" in request.POST:
            return render(request, self.template, {"result": calc.multiply()})
        elif "divide" in request.POST:
            return render(request, self.template, {"result": calc.divide()})


