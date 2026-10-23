from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
    return HttpResponse("Project Started")

# def calapp(request):
#     # num1 = request.get
#     return render(request,'calapp.html')

# def addition(request):
#     num1 = request.GET['num1']
#     num2 = request.GET['num2']

#     result = int(num1)+int(num2)

#     return render(request, 'calapp.html', {
#         'result': result,"num1":num1,"num2":num2
#     })

# def substraction(request):
#     num1 = request.GET['num1']
#     num2 = request.GET['num2']
    
#     result = int(num1)-int(num2)
    
#     return render(request, 'calapp.html', {
#         'result': result,"num1":num1,"num2":num2
#     })

# def division(request):
#     num1 = request.GET['num1']
#     num2 = request.GET['num2']
    
#     result = int(num1)/int(num2)
    
#     return render(request, 'calapp.html', {
#         'result': result,"num1":num1,"num2":num2
#     })

# def multiplication(request):
#     num1 = request.GET['num1']
#     num2 = request.GET['num2']
    
#     result = int(num1)*int(num2)
    
#     return render(request, 'calapp.html', {
#         'result': result,"num1":num1,"num2":num2
#     })
    
def calculate(request):

    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    operation = request.GET.get('operation')

    result = None

    if num1 and num2:

        num1 = int(num1)
        num2 = int(num2)

        if operation == 'add':
            result = num1 + num2

        elif operation == 'sub':
            result = num1 - num2

        elif operation == 'mul':
            result = num1 * num2

        elif operation == 'div':
            result = num1 / num2

    return render(request, 'calapp.html', {
        'num1': num1,
        'num2': num2,
        'result': result
    })


