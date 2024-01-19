from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("super_dashboard/", views.super_dashboard, name = 'super_dashboard')
]