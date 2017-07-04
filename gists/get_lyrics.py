# Hans Kamin
# Spring 2017

# Using web scraping to gather all of Logic's lyrics.

import requests
import time
from bs4 import BeautifulSoup

links = []
for pg in range(1,3):
    url = "http://www.metrolyrics.com/logic-alpage-%d.html" % pg
    # Get the html of the webpage.
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    # First table on this page contains links to songs by Logic.
    table = soup.find("table")
    for song in table.find_all('a'):
        links.append(song.get("href"))
        
# Enter each link and scrape all of the lyrics.
# Each element in our lyrics list will pertain to one song.
# Parsing through each link takes a while, expect long runtime.
lyrics = []
for link in links:
    # Delay each html request for security reasons.
    time.sleep(0.1)
    bs = BeautifulSoup(requests.get(link).text, "html.parser")
    paragraphs = bs.find_all('p')
    song_text = ""
    for p in paragraphs:
        if p.get("class") != None and "verse" in p.get("class"):
            song_text = song_text + p.text
    lyrics.append(song_text)
    
# Print the lyrics to the first song we scraped, "1-800-273-8255"
print(lyrics[0])

# Serialize the lyrics object to disk so we can access it later.
import pickle
pickle.dump(lyrics, open("lyrics.pkl", "wb"))
        
