import requests
import pandas as pd
from bs4 import BeautifulSoup

# web scraping mikonim ba beautiful soup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=44.9055&lon=-122.8107')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
print(soup.find_all('a'))

week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
print(items[0])

# get text faghat text ro mide
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [i.find(class_='period-name').get_text() for i in items]
print(period_names)

short_desc = [i.find(class_='short-desc').get_text() for i in items]
print(short_desc)

temps = [i.find(class_='temp').get_text() for i in items]
print(temps)

weather_stuff = pd.DataFrame({'period': period_names
                                 , 'short_desc': short_desc
                                 , 'temperatures': temps,
                              })
print(weather_stuff)
#save mishe dar folder asli file
weather_stuff.to_csv('weather.csv')
