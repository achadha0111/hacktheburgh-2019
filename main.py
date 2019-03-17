import requests
import tmdbsimple

import os

from flask import Flask, jsonify
from utils import categories_finder

tmdbsimple.API_KEY = os.environ.get("API_KEY")
API_KEY = os.environ.get("API_KEY")

app = Flask(__name__)


@app.route('/getVideoSuggestions/<movie_title>', methods=['GET'])
def get_movie_details(movie_title):
    get_movie_info = requests.get(
        "https://api.themoviedb.org/3/search/movie?api_key={0}&language=en-US&query={1}&page=1&include_adult=false".format(API_KEY, movie_title))

    data = get_movie_info.json()

    if len(data["results"]):
        film_id = data["results"][0]["id"]
        movie = tmdbsimple.Movies(film_id)

        response = movie.info()

        movie_info = {'duration': response["runtime"], 'image':response["poster_path"], 'overview': response["overview"], 'title': response["title"]}

        video_suggestions, _ = categories_finder.get_videos_for_duration(response["runtime"]*60)

        # Construct result object

        result = {"movie_result": [movie_info], "video_suggestions": video_suggestions}

        return jsonify(result), 200

    return jsonify(
        {"movie_result": [], "video_suggestions": []}
    ), 200


if __name__ == "__main__":
    app.run(debug=True)
