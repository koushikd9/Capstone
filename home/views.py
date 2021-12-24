from django.shortcuts import render

def home(req):
    return render(req,'index.html')

def login(req):
    return render(req,'login.html')

def food(req):
    return render(req,'food.html')

def services(req):
    return render(req,'services.html')

def storerrr(req):
    return render(req,'foodstore1.html')