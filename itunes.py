import requests
import json
import sys

artist = input("Enter the name of the artist: ")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + artist)
o = response.json()
for i in o["results"]:
    print(i["trackName"])
