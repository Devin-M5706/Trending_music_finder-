import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# Load API credentials from .env file
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# Define genres to fetch trending music from
GENRES = ["pop", "hip-hop", "rock", "jazz", "electronic", "classical", "r&b", "reggae"]

def get_trending_tracks(genre):
    """
    Fetches trending tracks from a given genre using Spotify's recommendations.
    """
    try:
        results = sp.recommendations(seed_genres=[genre], limit=10)
        tracks = results.get('tracks', [])
        
        trending_tracks = []
        for track in tracks:
            track_info = {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "album": track['album']['name'],
                "spotify_url": track['external_urls']['spotify']
            }
            trending_tracks.append(track_info)
        
        return trending_tracks
    except Exception as e:
        print(f"Error fetching tracks for {genre}: {e}")
        return []

def main():
    """
    Fetches trending music for multiple genres and displays the results.
    """
    for genre in GENRES:
        print(f"\n🔥 Trending {genre.capitalize()} Tracks 🔥")
        trending_tracks = get_trending_tracks(genre)
        
        if trending_tracks:
            for idx, track in enumerate(trending_tracks, start=1):
                print(f"{idx}. {track['name']} - {track['artist']} ({track['album']})")
                print(f"   🎵 Listen: {track['spotify_url']}")
        else:
            print("No tracks found.")

if __name__ == "__main__":
    main()
