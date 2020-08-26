from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
import requests

def index(request):
    print('x')
    return render(request, 'core/index.html')

def species(request):
    species = []
    
    if request.method == 'POST':
        
        species_url = 'https://ghibliapi.herokuapp.com/species/'
        
        search_params = {
            'species' : 'name',
            'species' : 'classification',
            'species' : 'eye_colors',
            'species' : 'hair_colors',
            'q' : request.POST['search']
            
            }

        
        r = requests.get(species_url, params=search_params)
        results = r.json()
        
        if len(results):
            for result in results:
                species_data = {
                'Name' : result['name'],
                'Classification': result['classification'],
                'Eye_Colors' : result['eye_colors'],
                'Hair_Colors' : result['hair_colors']
            }
                species.append(species_data)  
        
        else:
            message = print("No results found")

        print(species)
     

    context = {
    'species' : species
    }
        
    return render(request,'core/species.html', context)


def films(request):
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
        
        if len(results):
            for result in results:
                movie_data = {
                'Title' : result['title'],
                'Release_date': result['release_date'],
                'Director' : result['director'],
                'Producer' : result['producer'],
                'Description' : result['description']

            }
                movies.append(movie_data)  
        
     
        else:
            message = print('No results found')

    context = {
    'movies' : movies
    }
        

    return render(request,'core/films.html', context)


def people(request):
    people = []
    
    if request.method == 'POST':
        
        people_url = 'https://ghibliapi.herokuapp.com/people/'
        
        search_params = {
            'people' : 'name',
            'people' : 'age',
            'people' : 'gender',
            'people' : 'eye_color',
            'people' : 'hair_color',
            'q' : request.POST['search']
            
            }

        
        r = requests.get(people_url, params=search_params)
        results = r.json()
        
        if len(results):
            for result in results:
                people_data = {
                'name' : result['name'],
                'age': result['age'],
                'gender': result['gender'],
                'eye_Color' : result['eye_color'],
                'hair_Color' : result['hair_color']
            }

                people.append(people_data)  
        
        else:
            message = print("No results found")

        print(people)
     

    context = {
    'people' : people
    }
        
    return render(request,'core/people.html', context)
