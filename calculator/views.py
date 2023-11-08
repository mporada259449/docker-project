from django.shortcuts import render
from django.views import View
from calculator.calculator import Calculator
from django.core.cache import cache

class Calc(View):
    template = "calc.html"

    def get(self, request):
        cache.clear()
        return render(request, self.template)
    
    def post(self, request):
        num1 = float(request.POST.get("first"))
        num2 = float(request.POST.get("second"))
        operation = request.POST.get("operation")
        calc = Calculator(num1, num2)
        result = None


        if operation == "add":
            result = calc.add()
        elif operation =="subtract":
            result = calc.subtract()
        elif operation == "multiply":
            result = calc.multiply()
        elif operation == "divide":
            result = calc.divide()
            print(result)

        user_results = cache.get("user_results", [])
        if isinstance(result, float):
           user_results.append({"num1": num1, "num2": num2, "result": result, "operation": operation})
           cache.set("user_results", user_results)

           
        return render(request, self.template, {"result": result, "user_results": user_results})
