from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vckp_users(request):

    return render(request, 'vckp\vckp.html')

def about(request):
    abouttxt='возврат на домашнюю страницу'
    return render(request, 'home.html',{'abttxt':abouttxt})
