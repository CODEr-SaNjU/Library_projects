from django.shortcuts import render

# Create your views here.


def Dashobard(request):
    return render(request, 'Books_html/main.htm')
