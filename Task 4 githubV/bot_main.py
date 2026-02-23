import discord
from discord.ext import commands
import requests

#importing tokens for mal and dc bot
from tokens import mal_token, discord_token


description = 'MAL bot'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '$', description=description, intents=intents)

"""
Functions part
"""

def top_rankings():
    """
    (Top 5 anime overall)
    """
    #url to the request in this case request for the top 5 list
    url = f'https://api.myanimelist.net/v2/anime/ranking?ranking_type=all&limit=5?'
   
    #headers need to be setup for authentification
    headers = {
        'X-MAL-CLIENT-ID': mal_token
    }
    #storing the response inside a variable
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        #for debuging
        # print(response.json())    
        data = response.json()
        top5_list = data.get('data', [])
        results = []

        for item in top5_list:
            node = item.get('node')
            results.append({
                "rank": item.get('ranking').get('rank'),
                "title": node.get('title'),
                "image_url": node.get('main_picture').get('large')
            })
        return results
    
    else:
        return f"Error: {response.status_code}, {response.text}"
    

def top_anime_from_season(year: int, season:str):
    """("Enter your year in the format YYYY")   
    ("enter your season:  summer, spring, fall, winter")"""
    #url to the request
    url = f"https://api.myanimelist.net/v2/anime/season/{year}/{season}?limit=1"
   
    #headers need to be setup for authentification
    headers = {
        'X-MAL-CLIENT-ID': mal_token
    }
    #storing the response inside a variable
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        #for debuging
        # print(response.json())    
        
        data = response.json()
        title = (f"Title: {data.get('data')[0].get('node').get('title')}")
        picture = f"{data.get('data')[0].get('node').get('main_picture').get('large')}"
        return title, picture
    
    else:
        return f"Error: {response.text}"



"""
The Bot activity
"""


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def topanimefromseason(ctx, year:int, season:str):
    """
    Usage: $topanimefromseason 2024 winter
    """
    #thinking
    async with ctx.typing():
        title, image_url = top_anime_from_season(year, season.lower())
        print(image_url)

    if image_url:
        embed = discord.Embed(title=f"Top anime - {season} {year}", description=title)
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send(title)

@bot.command()
async def topanime(ctx):
    """
    Usage: $topanime
    """
    #thinking
    async with ctx.typing():
        rankings = top_rankings()
    
    if rankings:
        embed = discord.Embed(title=f"Top 5 anime on MAL")

        first_place_image = rankings[0]['image_url']

        #init desc text
        description_text = ""
        
        for anime in rankings:
            # We add each anime to the description or as fields
            description_text += f"**#{anime['rank']}**: {anime['title']}\n"
        
        embed.description = description_text
        embed.set_image(url=first_place_image)
        embed.set_footer(text="Showing image for the #1 ranked anime")

        await ctx.send(embed=embed)
    else:
        await ctx.send("Failed to retrieve rankings. Please check the logs.")
    
bot.run(discord_token)

