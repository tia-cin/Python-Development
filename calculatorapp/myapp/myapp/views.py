from django.shortcuts import render, HttpResponse

def home(req):
    return render(req, 'home.html')

def result(req):
    num1 = req.GET.get('num1')
    num2 = req.GET.get('num2')

    result = num1 + '+' + num2 + '=' + str(int(num1) + int(num2))

    return render(req, 'result.html', { 'result' : result })