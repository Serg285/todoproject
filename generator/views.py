from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def password(request):

    return render(request, 'generator\password.html', {'password':thepassword})

def about(request):
    abouttxt='возврат на домашнюю страницу'
    return render(request, 'home.html',{'abttxt':abouttxt})
