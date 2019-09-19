from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'blockchange/page1.html')

def page2(request):
    return render(request, 'blockchange/page2.html')

def page3(request):
    return render(request, 'blockchange/page3.html')

def page4(request):
    return render(request, 'blockchange/page4.html')

def page5(request):
    return render(request, 'blockchange/page5.html')

def page6(request):
    return render(request, 'blockchange/page6.html')