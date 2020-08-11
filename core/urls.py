from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('movies',
         views.MovieList.as_view(),
         name='MovieList'),
    path('', views.index, name='index'),

]
