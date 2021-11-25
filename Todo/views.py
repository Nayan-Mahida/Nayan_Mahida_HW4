from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForms, UpdateTodoForm
from django.contrib import messages

# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    form = TodoForms()
    context = {'tasks': tasks, 'form':form}
    return render(request, 'Todo/index.html', context)

def add(request):
    if request.method == 'POST':
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')


def complete_task(request, id):
    tasks = Todo.objects.get(id=id)
    tasks.completed = True
    tasks.save()
    messages.success(request, tasks.task_name + " has been completed.")
    return redirect('/')


def update(request, id):
    # Get the product based on its id
    tasks = Todo.objects.get(id=id)
    if request.method == "POST":
        form = UpdateTodoForm(request.POST, instance=tasks)
    # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UpdateTodoForm(instance=tasks)
    context = {'form': form, 'id': id}
    return render(request, 'Todo/update.html', context)

def delete(request, id):
    # Get the product based on its id
    tasks = Todo.objects.get(id=id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        messages.success(request, tasks.task_name + " has been removed.")
        tasks.delete()
        return redirect('/')
    context = { 'tasks': tasks}
    # if the request is not post, render the page with the product's info
    return render(request, 'Todo/delete.html', context)