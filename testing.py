#This is used to import the get module from requests to do http requests
from requests import get
from bs4 import BeautifulSoup as soup

#This is the URL endpoint
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)

#this uses the Beutiful soup method that takes an object as a parameter
htmlSoup = soup(response.text , 'html.parser')

#This code find all divs with the class of "lister-item mode advanced". Returns a list
movie_containers = htmlSoup.find_all('div', class_ = "lister-item mode-advanced") 

#This prints the length of the movie containers.
#What is the response.text data type
#What is the htmlSoup data type
#print(len(movie_containers)) #len can return the length of the movie_containers
#print(type(movie_containers))
#print(movie_containers[0])
#You can string together .find methods to navigate through the collections
print(movie_containers[0].find('div' , class_ = "lister-item-content").h3.a.text)
print(movie_containers[0].find('div', class_ = "lister-item-content").find('span' , class_ = "lister-item-year text-muted unbold").text)

#put it into a variable to make it clearner to look at
firstMovie = movie_containers[0]
print(firstMovie.find('strong').text) #This prints out the value
rating = float(firstMovie.find('strong').text) #convert it to a float/double

#get the number of votes on the film. The find returns a dictionary
dataValue = firstMovie.find('span' , attrs = {'name' : 'nv'})
firstVotes = int(dataValue)
print( dataValue['data-value']) #get the value given the key 'data-value' of the dictionary









