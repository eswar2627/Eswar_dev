from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from django.conf import settings
import os
from .forms import ContactForm
from .models import Project, Skill

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'core/home.html', {
        'skills': skills,
        'projects': projects
    })
def eswar_redirect(request):
    return redirect('home')
def projects(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {
        'projects': projects
    })
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {
        'project': project
    })
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {
        'form': form
    })
def resume(request):
    file_path = os.path.join(
        settings.BASE_DIR,
        "core",
        "static",
        "resume",
        "Eswar_maguluri1.pdf"
    )
    if not os.path.exists(file_path):
        raise Http404("Resume not found")
    return FileResponse(
        open(file_path, "rb"),
        content_type="application/pdf"
    )