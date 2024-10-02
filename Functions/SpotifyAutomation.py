import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import random
import AppOpener
from keyboard import press
from time import sleep
import json

def PlaySong(song_name):
    with open("D:\Virtual Assistant\Database\Spotifyclientid.json", "r") as f:
        file = json.load(f)

    client_id = file['clientid']
    client_secret = file['clientsecret']

    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = spotify.search(q=song_name, type='track')

    if results['tracks']['items']:
        return results['tracks']['items'][0]
    else:
        return "Error"

def PausePlaySong():
    AppOpener.open("Spotify", match_closest=True, output=False)
    sleep(1)
    press("spacebar")

def NextSong():
    AppOpener.open("Spotify", match_closest=True, output=False)
    sleep(1)
    press('ctrl+right arrow')

def PreviousSong():
    AppOpener.open("Spotify", match_closest=True, output=False)
    sleep(1)
    press('ctrl+left arrow')
    sleep(0.5)
    press('ctrl+left arrow')

def StartingSong():
    AppOpener.open("Spotify", match_closest=True, output=False)
    sleep(1)
    press('ctrl+left arrow')

def SeekFrwd():
    AppOpener.open("Spotify", match_closest=True, output=False)
    sleep(1)
    press("shift+right arrow")

def SeekBkwrd():
    AppOpener.open("Spotify", match_closest=True, output=False)
    sleep(1)
    press("shift+left arrow")

def Shuffle():
    AppOpener.open("Spotify", match_closest=True, output=False)
    sleep(1)
    press("ctrl+s")

def Repeat():
    AppOpener.open("Spotify", match_closest=True, output=False)
    sleep(1)
    press("ctrl+r")

def Playlist(name):
    with open("D:\Virtual Assistant\Database\Spotifyclientid.json", "r") as f:
        file = json.load(f)

    with open("D:\Virtual Assistant\Database\Spotifyplaylistids.json", "r") as fobj:
        playlistfile = json.load(fobj)

    playlistnames = GetPlaylistName(playlistfile)

    if name.lower() in playlistnames:
        id = GetPlaylistId(playlistfile[name.title()])
    else:
        return "ERROR"
    
    client_id = file['clientid']
    client_secret = file['clientsecret']
    redirect_uri = file['redirecturi']
    scope = "user-modify-playback-state"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))\

    tracks = sp.playlist_tracks(id)

    if 'items' in tracks and tracks['items']:
        track_uris = [track['track']['uri'] for track in tracks['items']]
        random.shuffle(track_uris)
        
        sp.start_playback(uris=track_uris)
        return name 
    
    else:
        return "ERROR"
        
def GetPlaylistId(playlist_link):
    id = ((playlist_link.split('playlist/')[1:]))[0].split('?si')[:1][0]
    return id

def GetPlaylistName(file):
    playlist_names = []

    for items in dict.keys(file):
        playlist_names.append(''.join(items.lower()).strip())

    return playlist_names

# print(f"Playing {PlaySong('Wavin Flag')['name']} by {PlaySong('Wavin Flag')['artists'][0]['name']}")