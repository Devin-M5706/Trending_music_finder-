# Spotify Trending Music Tracker

## 📌 Overview
This Python script fetches trending music recommendations from different genres using the Spotify API. It utilizes the `spotipy` library to access Spotify's recommendation system and display trending tracks along with their details.

## 🚀 Features
- Fetches trending tracks from various genres.
- Displays track name, artist, album, and a direct Spotify link.
- Uses Spotify API authentication with client credentials.
- Handles missing credentials and API errors gracefully.

## 📦 Requirements
Ensure you have the following installed before running the script:
- Python 3.x
- `spotipy` (Spotify API wrapper)
- `python-dotenv` (for managing environment variables)

Install dependencies using:
```bash
pip install spotipy python-dotenv
```

## 🔧 Setup
1. **Create a Spotify Developer Account**
   - Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Create an app and obtain your **Client ID** and **Client Secret**.

2. **Set Up Environment Variables**
   - In the project directory, create a `.env` file and add:
   ```ini
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   ```

3. **Run the Script**
   ```bash
   python your_script.py
   ```

## 🛠 How It Works
1. Loads API credentials from the `.env` file.
2. Authenticates with Spotify using `spotipy`.
3. Fetches trending tracks for predefined genres.
4. Displays the track list in the console.

## 🎵 Supported Genres
The script currently supports the following genres:
- Pop
- Hip-Hop
- Rock
- Jazz
- Electronic
- Classical
- R&B
- Reggae

## ⚠️ Troubleshooting
- **Issue: `ImportError: No module named 'spotipy'`**
  - Run `pip install spotipy python-dotenv`.
- **Issue: `Missing API credentials`**
  - Ensure the `.env` file is properly set up.
- **Issue: `No tracks found`**
  - Spotify might not have recommendations for that genre at the moment.

## 📜 License
This project is open-source and available for modification.

## 📩 Contact
For any issues or suggestions, feel free to reach out!

---
🎧 *Enjoy tracking trending music with Spotify!*

