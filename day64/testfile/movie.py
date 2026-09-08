import requests

url = "https://api.themoviedb.org/3/movie/day?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZDBlZjFiNGUwMTkyZjA2YzI4ODMyZTZiZWM2ZjQ3YyIsIm5iZiI6MTc4ODg3NTQzNS40MjcsInN1YiI6IjZhYTAxMmFiYTNiZWNiYmZjNGM3NjQxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.aJC8UXuev_dSzScRwW8FDF4ogRNkqTB3-IIv8gGQwko"
}

response = requests.get(url, headers=headers)
with open(file='json.txt',mode='w') as file:
    file.write(response.text)