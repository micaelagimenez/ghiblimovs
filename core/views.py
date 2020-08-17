from django.shortcuts import render, HttpResponse
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
        

        for result in results:
             movie_data = {
                'Title' : result['title'],
                'Release_date': result['release_date'],
                'Director' : result['director'],
                'Producer' : result['producer'],
                'Description' : result['description']
            }

        movies.append(movie_data)  
        print(movies)
     

    context = {
    'movies' : movies
    }
        
    return render(request,'core/index.html', context)

     



