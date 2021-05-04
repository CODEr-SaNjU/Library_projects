from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Dashobard(request):
    return render(request, 'Books_html/main.htm')
