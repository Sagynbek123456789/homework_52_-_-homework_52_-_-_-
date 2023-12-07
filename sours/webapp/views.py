from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, status_choices
from webapp.validate_char_field import task_validate


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
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_of_completion = request.POST.get('date_of_completion')
        errors = task_validate(description, status, date_of_completion)

        if errors:
            return render(request, 'task_create.html', {'status_choices': status_choices, 'errors': errors})
        else:
            task = Task.objects.create(description=description, status=status, date_of_completion=date_of_completion)
            return redirect('index')


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_update.html', {'status_choices': status_choices, 'task': task})
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_of_completion = request.POST.get('date_of_completion')
        errors = task_validate(task.description, task.status, task.date_of_completion)

        if errors:
            return render(request, 'task_update.html', {'status_choices': status_choices, 'errors': errors, 'task': task})
        else:
            task.description = description
            task.status = status
            task.date_of_completion = date_of_completion
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
