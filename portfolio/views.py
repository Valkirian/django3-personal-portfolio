from django.shortcuts import render
# Importando el modelo Projects para mapearlo en la vista principal del portafolio
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
