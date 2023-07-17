from django.shortcuts import render, redirect
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"task_list":tasks})


def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, "task/create.html", {})


def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.completed = not task.completed
        task.save()
        return redirect('task_list')
    return render(request, "update.html", {"task":task})
    
    
def delete_task(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        id = request.POST.get('id')
        task = Task.objects.get(id=id).delete()
        return render(request, "delete_success.html", {"task":tasks})
    else:
        return render(request, "delete_page.html", {"task":tasks})