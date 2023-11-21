from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='me'),
    path('about/hello', views.hello, name='number')
]
