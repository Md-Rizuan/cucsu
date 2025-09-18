# elections/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candidate_form', views.candidate_form, name='candidate_form'),
    path('central', views.central, name='central'),
    path('hall', views.hall, name='hall'),
    path('about', views.about, name='about'),
    path('details/<int:pk>/', views.details, name='details'),
]
