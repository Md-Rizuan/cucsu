# elections/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candidate_form', views.candidate_form, name='candidate_form'),
    path('central', views.central, name='central'),
    path('hall', views.hall, name='hall'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('details/<int:pk>/', views.details, name='details'),
    path('vote/<int:candidate_id>/', views.vote_candidate, name='vote_candidate'),
    path('already-voted',views.already_voted, name='already_voted'),
    path('voted',views.voted, name='voted'),
]
