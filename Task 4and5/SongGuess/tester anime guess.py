import yt_dlp
import json
import os
import random

song_file = "Songlist.json" 
score_file = "Score.json"

with open (song_file, "r" ) as sof:                      
    song_pool = json.load(sof)

with open (score_file, "w" ) as scf:                      
    
    ...
      
        
        # These options tell yt-dlp to just get the info, not download the file
ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': True,
    'js_runtimes': {'all': {}},
}

def get_track_info():

    

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # download=False is the key—it just scrapes the metadata and stream URL
        info = ydl.extract_info(song_pool[random.randint(0,9)].get('url'), download=False)
        
        return {
            'stream_url': info['url'],      # The direct link for FFmpeg
            'title': info.get('title'),     # For the answer key
            'duration': info.get('duration')
        }
get_track_info()