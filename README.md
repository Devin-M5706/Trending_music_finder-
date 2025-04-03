# Trending Music Finder

A Python application that helps you discover trending music using the Spotify API.

## Setup Instructions

1. Install Python 3.8 or higher
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Spotify API Setup:
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Log in with your Spotify account
   - Create a new application
   - Get your Client ID and Client Secret
   - Add `http://localhost:5000/callback` to your Redirect URIs in the app settings

4. Create a `.env` file in the project root with your Spotify credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:5000/callback
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://localhost:5000`

## Features
- View trending tracks
- Search for specific songs
- Get track details and previews
- Create and manage playlists

## Security Note
Never commit your `.env` file or share your Spotify API credentials publicly.

---
🎧 *Enjoy tracking trending music with Spotify!*

