from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('eswar/', views.eswar_redirect, name='eswar'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path("resume/", views.resume, name="resume"),
]