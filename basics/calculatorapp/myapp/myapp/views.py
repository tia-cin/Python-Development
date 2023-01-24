from django.shortcuts import render, HttpResponse

def home(req):
    return render(req, 'home.html')

def result(req):
    num1 = int(req.GET.get('num1'))
    num2 = int(req.GET.get('num2'))
    operator = req.GET.get('operator')
    res = 0

    if(operator == '+'):
        res = num1 + num2
    elif(operator == '-'):
        res = num1 - num2
    elif(operator == '×'):
        res = num1 * num2
    else:
        res = num1 // num2

    result = str(num1) + operator + str(num2) + '=' + str(res)

    return render(req, 'result.html', { 'result' : result })