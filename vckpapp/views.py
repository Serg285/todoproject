from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# создание скрипта для добавления пользователей в БД ВЦКП
def vckp_users(request):

    return render(request, 'vckp/vckp.html')
