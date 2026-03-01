
import yt_dlp
import json
import random

class SongGuessing():
    song_file = "Songlist.json" 
    score_file = "Score.json"

    def __init__(self) -> None:
        try:
            with open(self.song_file, "r") as sof:
                self.song_pool = json.load(sof)
        except (FileNotFoundError, json.JSONDecodeError):
            self.song_pool = []
            print(f"Error: {self.song_file} missing or corrupt.")

    def get_random_track(self):
        """Picks a song and fetches the stream link."""
        if not self.song_pool:
            return None

        # Pick a random song dict from the pool
        selected_song = random.choice(self.song_pool)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydlp:
            # We use the URL from our JSON list
            info = ydlp.extract_info(selected_song.get('url'), download=False)
            
            return {
                'stream_url': info['url'],
                'answer': selected_song.get('answer'), # Our clean answer
                'metadata': selected_song.get('metadata'),
                'duration': info.get('duration')
            }
        
if __name__ == "__main__":
    play = SongGuessing()
    print(play.get_random_track())
