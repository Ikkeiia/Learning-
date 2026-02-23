# This example requires the 'message_content' intent.
import discord
from discord.ext import commands
import requests


from tokens import mal_token, discord_token



description = 'MAL bot'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '$', description=description, intents=intents)



def top_anime_from_season(year: int, season:str):
    """("Enter your year in the format YYYY")   
    ("enter your season:  summer, spring, fall, winter")"""
    #url to the request 

    url = f"https://api.myanimelist.net/v2/anime/season/{year}/{season}?limit=1"
    print(url)
   

    #headers need to be setup for authentification
    headers = {
        'X-MAL-CLIENT-ID': mal_token
    }
    #storing the response inside a variable
    response = requests.get(url, headers=headers)



    if response.status_code == 200:
        #for debuging
        print(response.json())    
        
        data = response.json()
        title = (f"Title: {data.get('data')[0].get('node').get('title')}")
        picture = (f"Picture: {data.get('data')[0].get('node').get('main_picture').get('large')}")
        return print(title, picture)
    
    else:
        return print(f"Error: {response.text}, {response.status_code}")
    
top_anime_from_season(2024, "winter")