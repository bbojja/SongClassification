import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials("262fe468b5374ca3a8719f46444bd980", "a6afaf4ba8f14e42bed655e061e0851e")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

trackNames = []
artistNames = []

file = open('C:/Users/Bharat Bojja/Documents/Programming/SongClassification/Tracks1.txt', 'r', encoding='utf-8')

trackIDs = file.read().split(",")

#artistNamesFile = open('C:/Users/Bharat Bojja/Documents/Programming/SongClassification/ArtistNames.txt', 'w', encoding='utf-8')
#trackNamesFile = open('C:/Users/Bharat Bojja/Documents/Programming/SongClassification/TrackNames.txt', 'w', encoding='utf-8')

time = 2000

#def show_track(track):
    # artistNamesFile.write(track['artists'][0]['name'] + "\n")
    # trackNamesFile.write(track['name'] + "\n")

for id in trackIDs:
    if time % 50 == 0:
        print(time)
    #show_track(sp.track((id[:22]).replace("'", '"')))
    time -= 1