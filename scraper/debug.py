from bs4 import BeautifulSoup as soup
import requests

pages = [str(i) for i in range(1, 5)]
years_url = [str(i) for i in range(2000, 2018)]

reqCount = 0
for page in pages:
    for year in years_url:
        reqCount = reqCount + 1
        url = 'http://www.imdb.com/search/title?release_date=' + year + '&sort=num_votes,desc&page=' + page

#testing the url
test_url = 'http://www.imdb.com/search/title?release_date=2000&sort=num_votes,desc&page=1'

#this is getting the request url
responce = requests.get(test_url)

# gets the response as a text and parses it
page_html = soup(responce.text, 'html.parser')


# This is a list of all the divs that contain the information of the scraped page
movie_containers = page_html.findAll('div', class_="lister-item mode-advanced")

print(movie_containers[0])