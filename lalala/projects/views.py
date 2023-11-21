from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def projects_home(request):
    projects = Articles.objects.order_by('-date')
    return render(request, 'projects/projects.html', {'projects': projects})

class projectsDetailView(DetailView):
    model = Articles
    template_name = 'projects/details_views.html'
    context_object_name = 'article'






