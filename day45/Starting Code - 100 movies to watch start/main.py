### This sis how to check what webscrape and what not to webscrape from anywebsite


# weblink/robot.txt

##  This is going to store the top 100 movies of all time. in movies.txt file
import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇
result =  requests.get(url=URL)
Movie_Soup = BeautifulSoup(result.text,'html.parser')
movie_list = Movie_Soup(name="h3", class_="title")
movie_title = [movies.string for movies in movie_list]
with open(file="day45/Starting Code - 100 movies to watch start/movies.txt",mode="w") as movies:
    for movie in movie_title[::-1]:
        if "59)" not in movie: #type:ignore
            movies.writelines(f"{movie}\n")
        