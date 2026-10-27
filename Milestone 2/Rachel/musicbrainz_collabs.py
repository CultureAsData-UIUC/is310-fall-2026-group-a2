import requests
import time

url = "https://musicbrainz.org/ws/2/artist/"
headers = {"User-Agent": "is310-course-scraper/1.0 (student project; rtam7@illinois.edu)"}

#get Ariana Grande's artist ID
params = {
    "query": 'artist:"Ariana Grande"',
    "fmt": "json",
    "limit": 5
}

response = requests.get(
    url,
    headers=headers,
    params=params,
    timeout=15
)

if response.status_code == 200:
    data = response.json()

    for artist in data["artists"]:
        print(artist["name"], artist["id"])
else:
    print("Error:", response.status_code)

# Get Ariana Grande's genres
artist_id = "f4fdbb4c-e4b7-47e8-b8bd-91bbfcfa3877"

genre_url = "https://musicbrainz.org/ws/2/artist/" + artist_id
print("Genre URL:", genre_url)

time.sleep(2)

genre_response = requests.get(
    genre_url,
    headers=headers,
    params={"inc": "genres", "fmt": "json"},
    timeout=15
)

if genre_response.status_code == 200:
    genre_data = genre_response.json()

    for genre in genre_data.get("genres", []):
        print(genre["name"])
else:
    print("Genre request error:", genre_response.status_code)