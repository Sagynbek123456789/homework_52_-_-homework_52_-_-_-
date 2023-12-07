from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, status_choices


# Create your views here.
def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'status_choices': status_choices})
    elif request.method == 'POST':
        Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            date_of_completion=request.POST.get('date_of_completion')
        )
        return redirect('index')


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_update.html', {'status_choices': status_choices})
    elif request.method == 'POST':
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.date_of_completion = request.POST.get('date_of_completion')
        task.save()
        return redirect('index')


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')


# Create your views here.
# def task_create_view(request):
#     return None
