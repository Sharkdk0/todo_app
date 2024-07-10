from django.shortcuts import render, redirect, HttpResponse
from .models import Todo

# Create your views here.

def home(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        new_todo = Todo(title=title, description=description)
        new_todo.save()
        return redirect('/home')

def show_update(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    return render(request, 'update.html', {'todo': todo})

def update_todo(request, todo_id):
    # if request.method == 'POST':
        todo = Todo.objects.get(pk = todo_id)
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.save()
        return redirect('/home')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.delete()
    return redirect('/home')