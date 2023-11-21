from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Сайт-портфолио',
        'values': ['Some', 'hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Music'
        }
    }
    return render(request, 'main/index2.html', data)
    
def about(request):
    return render(request, 'main/about2.html')
    
def hello(request):
    return render(request, 'main/test.html')
