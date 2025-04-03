import os
from flask import Flask, render_template, request, redirect, url_for, session
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Spotify API credentials
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

# Initialize Spotify OAuth
sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope='user-library-read playlist-modify-public user-top-read'
)

@app.route('/')
def index():
    if 'token_info' not in session:
        return redirect(url_for('login'))
    
    sp = spotipy.Spotify(auth=session['token_info']['access_token'])
    
    # Get user's top tracks
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')
    
    # Get new releases
    new_releases = sp.new_releases(limit=10, country='US')
    
    return render_template('index.html', 
                         top_tracks=top_tracks['items'],
                         new_releases=new_releases['albums']['items'])

@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    session['token_info'] = token_info
    return redirect(url_for('index'))

@app.route('/search')
def search():
    if 'token_info' not in session:
        return redirect(url_for('login'))
    
    sp = spotipy.Spotify(auth=session['token_info']['access_token'])
    query = request.args.get('q', '')
    
    if query:
        results = sp.search(q=query, type='track', limit=10)
        return render_template('search.html', 
                             tracks=results['tracks']['items'],
                             query=query)
    
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True) 