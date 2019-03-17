import json

import requests
import tmdbsimple

tmdbsimple.API_KEY = "14332739417600e894734cc3287ace7e"
API_KEY = "14332739417600e894734cc3287ace7e"


def get_movie_details(movie_title):
    get_movie_info = requests.get(
        "https://api.themoviedb.org/3/search/movie?api_key=14332739417600e894734cc3287ace7e&language=en-US&query=" + movie_title + "&page=1&include_adult=false")
    data = get_movie_info.json()
    if len(data["results"]):
        brut = data["results"][0]["id"]
        movie = tmdbsimple.Movies(brut)
        response = movie.info()

        movie_info = {'duration': response["runtime"], 'image':response["poster_path"], 'overview': response["overview"], 'title': response["title"]}

        return movie_info
    return "MOVIE NOT FOUND"


print(json.dumps(get_movie_details("cars2"), indent=4))
