# This module handles crawling on different pages
from requests import get
from bs4 import BeautifulSoup as soup
from time import sleep, time
from random import randint
from warnings import warn
import pandas as pd

# lists to store the information in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# headers that determine how the page will be scraped depending on the website language
headers = {"Accept-Language": "en-US, en;q=0.5"}

# creates a list of the different url parameters
pages = [str(i) for i in range(1, 5)]
years_url = [str(i) for i in range(2000, 2018)]

# Get the start time
start_time = time()

# Number of requests
requests = 0

for year in years_url:
    for page in pages:
        # gets the url for every year and up to four pages
        url = 'http://www.imdb.com/search/title?release_date=' + year + '&sort=num_votes,desc&page=' + page
        responce = get(url)

        # Pauses to prevent overloading the server with requests. Pauses are randomized to immitate human interaction
        sleep(randint(0,9))

        # prints out the request
        requests = requests+  1
        elapsed_time = time() - start_time

        print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))

        # Throw a warning for non-200 status codes
        if responce.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, responce.status_code))

        # Break the loop if the number of requests is greater than expected
        if requests > 72:
            warn('Number of requests was greater than expected.')
            break

        # gets the response as a text and parses it
        page_html = soup(responce.text, 'html.parser')

        # This is a list of all the divs that contain the information of the scraped page
        movie_containers = page_html.findAll('div', class_="lister-item mode-advanced")

        for items in movie_containers:
            # gets all elements that have a metacritic score
            if items.find('span', class_='metascore favorable') is not None:
                # This takes the names of every div element
                name = items.find('div', class_='lister-item-content').h3.a.text
                names.append(name)
                # This takes the year released
                year = items.find('span', class_='lister-item-year text-muted unbold').text
                years.append(year)
                # This gets the imdb ratings
                rating = float(items.find('strong').text)
                imdb_ratings.append(rating)
                # This gets the metascores of each movie
                score = int(items.find('span', class_='metascore favorable').text)
                metascores.append(score)
                # gets the number of votes and casts it to an integer
                value = int(items.find('span', attrs={'name': 'nv'})['data-value'])
                votes.append(value)
                #prints the item that gets scraped
                print('name: '+ str(name) + ' year: ' + str(year) + ' rating ' + str(rating) + ' metascore ' + str(score) + ' votes: ' + str(value))


#Prints out the elapsed time that it took to scrape the data
print('scraping done, Elapsed time: ' + str(time() - start_time) )

#Stores the data into a dataframe
movie_ratings = pd.DataFrame({
    'movies' : names,
    'year' : years,
    'imdb_rating': imdb_ratings,
    'metascore' : metascores,
    'number_of_votes' : votes
})

movie_ratings = movie_ratings[['movies', 'year', 'imdb_rating', 'metascore', 'number_of_votes']]
movie_ratings.head()

print(movie_ratings.info())
movie_ratings.head(10)


movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
movie_ratings.describe().loc[['min', 'max'], ['imdb_rating', 'metascore']]
movie_ratings['n_imdb'] = movie_ratings['imdb_rating'] * 10
movie_ratings.to_csv('movie_ratings.csv')

