from django.shortcuts import render
from .models import todoapp_TodoListItem
from django.http import HttpResponseRedirect


def todoappView(request):
    all_todo_items = todoapp_TodoListItem.objects.all()
    return render(request, 'todolist/todolist.html',{'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = todoapp_TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = todoapp_TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')
