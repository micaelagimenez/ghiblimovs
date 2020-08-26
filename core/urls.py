from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('species', views.species, name='species'),
    path('people', views.people, name='people'),
    path('films', views.films, name='films')

]
