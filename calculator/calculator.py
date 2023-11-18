from celery import shared_task

@shared_task
def add(num1, num2):
    return num1+num2

@shared_task
def subtract(num1, num2):
    return num1-num2

@shared_task
def multiply(num1, num2):
    return num1*num2

@shared_task
def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "ERROR: devide by 0"
    