from pprint import pprint
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

REDIRECT_URI = "http://example.com"

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.environ.get("SPOTIFY_SECRET")
# user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD : ")
user_date = "2005-03-23"

SPOTIFY_CHARTS_URL = f"https://www.billboard.com/charts/hot-100/{user_date}"

response = requests.get(SPOTIFY_CHARTS_URL).text
soup = BeautifulSoup(response,"html.parser")

titles = []
artists = []
song_titles = soup.find_all(name="span", class_="chart-element__information__song")
for title in song_titles:
    titles.append(title.getText())
song_artists = soup.find_all(name="span", class_="chart-element__information__artist")
for artist in song_artists:
    artists.append(artist.getText())

uris = []

songs = dict(zip(titles,artists))

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = ""
for title,artist in songs.items():
    user_id = sp.current_user()['id']
    new_artist = artist.replace('Featuring', '')
    query=f"track: {title} artist: {new_artist} year: 2005"
    result = sp.search(query)['tracks']['items']
    if result:
        uris.append(result[0]['uri'])

# sp.user_playlist_create("rohit", "Rohit", public=False, description='New Playlist')
playlist_name = f"{user_date} Billboard 100"
playlist = sp.user_playlist_create(user_id,playlist_name,public=False,description=f"Top 100 songs on the date {user_date}")
playlist_id = playlist['id']

re = sp.playlist_add_items(playlist_id,uris)
print(re)
