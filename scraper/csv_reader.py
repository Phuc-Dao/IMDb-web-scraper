import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movie_ratings = pd.read_csv('/Users/phucdao/PycharmProjects/project1/venv/movie_ratings.csv' , sep = ',')

fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16,4))
ax1, ax2, ax3 = fig.axes

#first graph that shows normal distribution imdb rating
ax1.hist(movie_ratings['imdb_rating'], bins = 10, range = (0,10)) # bin range = 1
ax1.set_title('IMDB rating')

#second graph of showing normal distribution metascores
ax2.hist(movie_ratings['metascore'], bins = 10, range = (0,100)) # bin range = 10
ax2.set_title('Metascore')

#third graph showing both metascores and imdb distributions
ax3.hist(movie_ratings['n_imdb'], bins = 10, range = (0,100), histtype = 'step')
ax3.hist(movie_ratings['metascore'], bins = 10, range = (0,100), histtype = 'step')
ax3.legend(loc = 'upper left')
ax3.set_title('The Two Normalized Distributions')
for ax in fig.axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

plt.show()