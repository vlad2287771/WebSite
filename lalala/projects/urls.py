from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects_home, name='projects'),
    path('<int:pk>', views.projectsDetailView.as_view(), name='projects-detail'),
]