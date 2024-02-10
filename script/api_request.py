import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import re

def track_uri_to_features(track_uri, c_id, c_secret):

    client_credentials_manager = SpotifyClientCredentials(client_id=c_id, client_secret=c_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    #Audio features
    features = sp.audio_features(track_uri)[0]
    
    #Artist of the track, for genres and popularity
    artist = sp.track(track_uri)["artists"][0]["id"]
    artist_pop = sp.artist(artist)["popularity"]
    artist_genres = sp.artist(artist)["genres"]
    
    #Track popularity
    track_pop = sp.track(track_uri)["popularity"]
    
    #Add in extra features
    features["artist_pop"] = artist_pop
    if artist_genres:
        features["genres"] = " ".join([re.sub(' ','_',i) for i in artist_genres])
    else:
        features["genres"] = "unknown"
    features["track_pop"] = track_pop
    
    return features


if __name__ == '__main__':
    # test
    load_dotenv()
    c_id = os.getenv('CLIENT_ID')
    c_secret = os.getenv('CLIENT_SECRET')
    track_uri = '6I9VzXrHxO9rA9A5euc8Ak'
    test_features = track_uri_to_features(track_uri, c_id, c_secret)
    print(test_features)