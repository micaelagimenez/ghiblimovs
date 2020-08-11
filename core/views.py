from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from core.models import Movie
from django.views.generic import ListView
import requests

def index(request):
    movies = []
    if request.method == 'POST':
        
        film_url = 'https://ghibliapi.herokuapp.com/films/'
        
        search_params = {
            'films' : 'title',
            'films' : 'description',
            'films' : 'director',
            'films' : 'release_date',
            'q' : request.POST['search']
            
            }

        
        r = requests.get(film_url, params=search_params)
        results = r.json()
        print(results)

        for result in results:
             movie_data = {
                'Title' : result['title'],
                'Release_date': result['release_date'],
                'Director' : result['director'],
                'Description' : result['description']
            }

            
    context = {
    'movies' : movies
    }
         
    return render(request,'core/index.html', context)
        
    


class MovieList(ListView):
    model = Movie

