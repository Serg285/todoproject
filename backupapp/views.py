import os
import datetime
#from datetime import datetime

from django.shortcuts import render
from .models import backup
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

def password1(request):
    return render(request, 'generator/password1.html')

def backupView(request):
    all_backup_items_vckp = backup.objects.all().filter(system_name = 'ВЦКП')
    all_backup_items_adsums = backup.objects.all().filter(system_name = 'АДСУМС')
    backup_error_count_adsums = backup.objects.all().filter(system_name = 'АДСУМС').count()
    return render(request,'backup/backupstatus.html', {'all_items_vckp':all_backup_items_vckp, 'all_items_adsums':all_backup_items_adsums, 'error_count_adsums':backup_error_count_adsums})

def day_type(day_of_backup):
    substring = 'weekly_'
    weekly = day_of_backup.find(substring)
    if weekly > -1:
        return True
    return False

def addBackupView(request):
    #x = request.POST['backup_status']
    #new_item = backup(backup_status = x)
    #new_item.save()
    #y = backup.objects.all().filter(system_name = 'ВЦКП')
    #y.delete()

    backup.objects.all().filter(system_name = 'ВЦКП').delete()
    disk = 'M:'
    subdir = '/daily'
    disk_list = os.listdir(disk)
    #print(datetime.now())
    #print(disk_list)
    n0 = len(disk_list)

    for i0 in range(n0):
        path_b_up = disk + '/' + disk_list[i0] + subdir
        # print(path_b_up)
        path = path_b_up
        #path = 'M:/aisq2/daily'
        contents = os.listdir(path)
        #path_b = path + '/' + contents[0]
        #contents2 = os.listdir(path_b)
        #date_m = os.path.getmtime(path_b)

        #localcurrentdate = datetime.now()
        localcurrentdate = datetime.date.today().strftime('%d.%m.%Y')
        #localcurrentdateandtime = datetime.
        #print(localcurrentdateandtime)
        #print(datetime.now())
        n= len(contents)
        i_fault = 0
        #  print(disk_list[i0] + ' найдено ' + str(i_fault) + ' ошибок')
        for i in range(n):
            path_b = path + '/' + contents[i]
            date_m = os.path.getmtime(path_b)
            date_m = datetime.date.today().strftime('%d.%m.%Y')
            #date_m = time.ctime(date_m)
            if localcurrentdate != date_m :
                i_fault = i_fault + 1
                print(path_b + ' - ' + date_m + ' FAULT!!!')
                #print(disk_list[i0] + ' найдено ' + str(i_fault) + ' ошибок')
                #else:
                #  print(path_b + ' - ' + date_m + ' OK!')
        x=disk_list[i0] + ' найдено ' + str(i_fault) + ' ошибок'
        new_item = backup(backup_status = x,
                          system_name = 'ВЦКП')
        new_item.save()
        print(disk_list[i0] + ' найдено ' + str(i_fault) + ' ошибок')

    return HttpResponseRedirect('/backupapp/')

def addBackupViewADSUMS(request):
    backup.objects.all().filter(system_name = 'АДСУМС').delete()
    disk = 'N:'
    disk_list = os.listdir(disk)
    print(datetime.date.today().strftime('%d.%m.%Y'))
    deltatime = 1
    one_day = datetime.timedelta(deltatime)
    today = datetime.datetime.today()
    yesterday = today - one_day

    delta_control_date_week = today.weekday()+1
    one_day_week = datetime.timedelta(delta_control_date_week)
    yesterday_week = today - one_day_week

    control_date = datetime.datetime(yesterday.year, yesterday.month,yesterday.day, 22, 00, 00)
    control_date_week = datetime.datetime(yesterday_week.year, yesterday_week.month,yesterday_week.day, 22, 00, 00)
    print(control_date)
    print(control_date_week)

    if control_date.weekday() == 6 :
        deltatime = 3
        one_day = datetime.timedelta(deltatime)
        today = datetime.datetime.today()
        yesterday = today - one_day
        control_date = datetime.datetime(yesterday.year, yesterday.month,yesterday.day, 22, 00, 00)
        #print(control_date)
    n0 = len(disk_list)
    i_fault = 0
    for i0 in range(n0):
        # ежедневные бекапы
        if day_type(disk_list[i0]) == False :
            path_b = disk + '/' + disk_list[i0]
            date_m = os.path.getmtime(path_b)
            date_m2 = datetime.datetime.fromtimestamp(date_m)
            if (date_m2 < control_date) :
                i_fault = i_fault + 1
                print(path_b + ' - ' + (date_m2.strftime('%d.%m.%Y-%H:%M:%S' )) + ' FAULT!!!')
                x = path_b + ' - ' + (date_m2.strftime('%d.%m.%Y-%H:%M:%S' )) + ' FAULT!!!'
                new_item = backup(backup_status=x,
                                  system_name = 'АДСУМС',
                                  backup_type = 'daily',
                                  request_d = today.strftime('%d.%m.%Y -%H:%M:%S'))
                new_item.save()
        # недельные бекапы
        else:
            path_b = disk + '/' + disk_list[i0]
            date_m = os.path.getmtime(path_b)
            date_m2 = datetime.datetime.fromtimestamp(date_m)
            if (date_m2 < control_date_week) :
                i_fault = i_fault + 1
                print(path_b + ' - ' + (date_m2.strftime('%d.%m.%Y-%H:%M:%S' )) + ' FAULT!!!')
                x = path_b + ' - ' + (date_m2.strftime('%d.%m.%Y-%H:%M:%S' )) + ' FAULT!!!'
                new_item = backup(backup_status=x,
                                  system_name = 'АДСУМС',
                                  backup_type = 'weekly',
                                  request_d = today.strftime('%d.%m.%Y -%H:%M:%S'))
                new_item.save()
            else:
                print(path_b + ' - ' + date_m2.strftime('%d.%m.%Y-%H:%M:%S' ) + ' OK!')

    print('Найдено ' + str(i_fault) + ' ошибок')

    return HttpResponseRedirect('/backupapp/')
