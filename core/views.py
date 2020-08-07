from django.shortcuts import render

from .models import Movie
import requests

class MoviesView(APIView):
    def post(self, request, format=None):

        movie_title = request.data.get('movie_title')

        if not movie_title:
            response = {
                'error': 'Incorrect movie title'
                }
            return Response(response, status.HTTP_400_BAD_RESQUEST)

        url = 'https://ghibliapi.herokuapp.com/films'

        r = resquest.get(url)
        r = r.json()

        #movies in api

        if r.get('Response') == 'False':
            response = {
                'error': f'No movie called {movie_title}'
                }
            return Response(response, status.HTTP_400_BAD_RESQUEST)