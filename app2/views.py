from django.shortcuts import render

def index(request):
    return render(request, 'app2/index.html')

def order(request):
    return render(request, 'app2/order.html')

def menu(request):
    return render(request, 'app2/menu.html')
