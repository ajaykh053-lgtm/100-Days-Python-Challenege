import requests
import os
from dotenv import load_dotenv

load_dotenv()
import requests

url = "https://api.themoviedb.org/3/search/movie"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZDBlZjFiNGUwMTkyZjA2YzI4ODMyZTZiZWM2ZjQ3YyIsIm5iZiI6MTc4ODg3NTQzNS40MjcsInN1YiI6IjZhYTAxMmFiYTNiZWNiYmZjNGM3NjQxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aJC8UXuev_dSzScRwW8FDF4ogRNkqTB3-IIv8gGQwko",
}
response = requests.get(url,params={"api_key":os.environ['API_KEY'],"query":"movie_title"}, headers=headers)
print(response.text)
# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZDBlZjFiNGUwMTkyZjA2YzI4ODMyZTZiZWM2ZjQ3YyIsIm5iZiI6MTc4ODg3NTQzNS40MjcsInN1YiI6IjZhYTAxMmFiYTNiZWNiYmZjNGM3NjQxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aJC8UXuev_dSzScRwW8FDF4ogRNkqTB3-IIv8gGQwko",
# }
# params = {"api_key": f"{os.environ['API_KEY']}","query": "movie_title"}
# response = requests.get(os.environ["MOVIE_ENDPOINT"], params=params, headers=headers)
with open(file="result.json", mode="w") as file:
    file.write(response.text)
