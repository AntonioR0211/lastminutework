# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

my_countries = ['United States', 'Zimbabwe','Cuba', 'Caribbean small states', "Cameroon", "Burundi"]
ns_countries = ['United States', 'Canada', 'Mexico', 'Brazil', 'Cuba', 'Argentina']
eu_countries = ['France', 'Italy', 'Spain', 'Turkey', 'Sweden', 'Norway']
african_countries = ['Egypt', 'Morocco', 'Madagascar', 'Zimbabwe', 'Chad', 'Niger']
asian_countries = ['China', 'Vietnam', 'India', 'Saudi Arabia', 'South Korea', 'North Korea']

df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

unique_countries = df['Entity'].unique()

countries = []
countries.append(ns_countries)
countries.append(eu_countries)
countries.append(african_countries)
countries.append(asian_countries)
for i in range (4):
  for c in unique_countries:
    if c in countries[i]:
      
      years = df[df['Entity'] == c]['Year']

      sum_elec = df[df['Entity'] == c]['Access']

      plt.plot(years, sum_elec, label=c, marker="8", linestyle="-")
  plt.ylabel('Percentage of Country Population')
  plt.xlabel('Year')
  plt.title('Percent of Population with Access to Electricity')
  plt.legend()
  plt.show()


# Question 9: I can notice that Europe is far more developed than other continents as all of the countries
# in the Europe graph end up at 100% or almost 100% in the end, other graphs end all over the place where
# countries could be 100% or even as low as 10%.

# Question 10: My classmate Joe has very similar Europe graphs as they are almost identical. The countries for other
# continents are different so those graphs are a little bit changed since some of his countries are far more developed
# than some of mine.
