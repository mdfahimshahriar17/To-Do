from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    status_filter = request.GET.get('status', 'all')
    category_filter = request.GET.get('category', 'all')
    tasks = Task.objects.filter(user = request.user)

    if status_filter != 'all':
        tasks = tasks.filter(is_completed=(status_filter=='completed'))

    if category_filter != 'all':
        tasks = tasks.filter(category=category_filter)

    completed_tasks = tasks.filter(is_completed = True)
    pending_tasks = tasks.filter(is_completed = False)

    return render(request, '', {
        'completed_tasks' : completed_tasks,
        'pending_tasks' : pending_tasks,
        'status_filter' : status_filter,
        'category_filter' : category_filter,
    })