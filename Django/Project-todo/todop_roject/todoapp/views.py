from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'items': items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        TodoItem.objects.create(title=title)
    return redirect('todo_list')

def delete_todo(request, todo_id):
    if request.method == 'POST':
        item = TodoItem.objects.get(id=todo_id)
        item.delete()
    return redirect('todo_list')