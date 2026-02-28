import discord
from discord.ext import commands
from Functions import *

#importing tokens for mal and dc bot
from tokens import mal_token, discord_token


mal=MALClient(mal_token)

description = 'MAL bot'
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '$', description=description, intents=intents)


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
        title, image_url = mal.get_seasonal_anime(year, season.lower())

    if image_url:
        embed = discord.Embed(title=f"Top anime - {season} {year}", description=title,)
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
        rankings = mal.get_top_rankings()
    
    if rankings:
        embed = discord.Embed(title=f"Top 5 anime on MAL")

        first_place_image = rankings[0]['image_url'] # type: ignore

        #init desc text
        description_text = ""
        
        for anime in rankings:
            # We add each anime to the description or as fields
            description_text += f"**#{anime['rank']}**: {anime['title']}\n" # type: ignore
        
        embed.description = description_text
        embed.set_image(url=first_place_image)
        embed.set_footer(text="Showing image for the #1 ranked anime")

        await ctx.send(embed=embed)
    else:
        await ctx.send("Failed to retrieve rankings. Please check the logs.")



    
bot.run(discord_token)

