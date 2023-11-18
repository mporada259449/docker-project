from django.shortcuts import render
from django.views import View
from calculator.calculator import add, subtract, multiply, divide
from django.core.cache import cache

class Calc(View):
    template = "calc.html"

    def get(self, request):
        cache.clear()
        return render(request, self.template)
    
    def post(self, request):
        result = None
        user_results = None
        operation = request.POST.get("operation")

        try:
            num1 = float(request.POST.get("first"))
            num2 = float(request.POST.get("second"))
        except ValueError:
            if request.user.is_authenticated:
                user_results_id = request.user.username
                user_results = cache.get(user_results_id, [])
            return render(request, self.template, {"result": "ERROR: no value provided", "user_results": user_results})     
    
        if operation == "add":
            result = add.delay(num1, num2)
        elif operation =="subtract":
            result = subtract.delay(num1, num2)
        elif operation == "multiply":
            result = multiply.delay(num1, num2)
        elif operation == "divide":
            result = divide.delay(num1, num2)

        if request.user.is_authenticated:
            user_results_id = request.user.username
            user_results = cache.get(user_results_id, [])
            if isinstance(result.get(), float):
                user_results.append({"num1": num1, "num2": num2, "result": result.get(), "operation": operation})
                cache.set(user_results_id, user_results)

        return render(request, self.template, {"result": result.get(), "user_results": user_results})  
            
        

