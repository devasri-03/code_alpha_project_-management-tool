from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Task, Comment


@login_required
def dashboard(request):
    projects = Project.objects.filter(created_by=request.user)
    tasks = Task.objects.filter(project__created_by=request.user)

    return render(request, 'tasks/dashboard.html', {
        'projects': projects,
        'tasks': tasks
    })


@login_required
def create_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        Project.objects.create(
            name=name,
            description=description,
            created_by=request.user
        )

        return redirect('dashboard')

    return render(request, 'tasks/create_project.html')


@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)

    return render(request, 'tasks/project_detail.html', {
        'project': project,
        'tasks': tasks
    })


@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            project=project,
            title=title,
            description=description
        )

        return redirect('project_detail', project_id=project.id)

    return render(request, 'tasks/create_task.html', {
        'project': project
    })


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    comments = Comment.objects.filter(task=task)

    if request.method == 'POST':
        text = request.POST.get('text')

        if text:
            Comment.objects.create(
                task=task,
                user=request.user,
                text=text
            )

        return redirect('task_detail', task_id=task.id)

    return render(request, 'tasks/task_detail.html', {
        'task': task,
        'comments': comments
    })