import requests
import json
import random
import yt_dlp

class MALClient:
    """Handles all MyAnimeList API requests."""
    
    BASE_URL = "https://api.myanimelist.net/v2"

    def __init__(self, token: str):
        self.headers = {
            'X-MAL-CLIENT-ID': token
        }

    def get_top_rankings(self, limit: int = 5):
        """Fetches the top X anime overall."""
        url = f"{self.BASE_URL}/anime/ranking?ranking_type=all&limit={limit}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            results = []
            for item in data.get('data', []):
                node = item.get('node')
                results.append({
                    "rank": item.get('ranking').get('rank'),
                    "title": node.get('title'),
                    "image_url": node.get('main_picture').get('large')
                })
            return results
        return None

    def get_seasonal_anime(self, year: int, season: str):
        """Fetches the top anime for a specific season."""
        url = f"{self.BASE_URL}/anime/season/{year}/{season.lower()}?limit=1"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            data = response.json()
            # Safety check if list is empty
            if not data.get('data'):
                return None
            
            node = data.get('data')[0].get('node')
            title = node.get('title')
            picture = node.get('main_picture').get('large')
            return title, picture
        return None


class SongGuessing:
    """Handles the music guessing game logic."""
    
    def __init__(self, song_file: str = "Songlist.json"):
        self.song_file = song_file
        self.song_pool = self._load_songs()

    def _load_songs(self):
        """Private helper to load the JSON file."""
        try:
            with open(self.song_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Warning: {self.song_file} not found or invalid.")
            return []

    def get_random_track(self):
        """Picks a song and fetches the stream link via yt-dlp."""
        if not self.song_pool:
            return None

        selected = random.choice(self.song_pool)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydlp:
            info = ydlp.extract_info(selected.get('url'), download=False)
            return {
                'stream_url': info['url'],
                'answer': selected.get('answer'),
                'metadata': selected.get('metadata'),
                'duration': info.get('duration')
            }