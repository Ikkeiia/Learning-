import asyncio
import discord
from discord.ext import commands
from Functions import *


#importing tokens for mal and dc bot
from tokens import mal_token, discord_token


mal=MALClient(mal_token)
game = SongGuessing()

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
    title, image_url = mal.get_seasonal_anime(year, season.lower()) # type: ignore

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


@bot.command()
async def play(ctx):
    """
    Usage: $play
    """
    if not ctx.author.voice:
        return await ctx.send("Join a voice channel first!")

    vc = ctx.voice_client
    if not vc:
        vc = await ctx.author.voice.channel.connect()

    async with ctx.typing():
        # In a real bot, we'd run this in a thread to prevent lag
        track = game.get_random_track()
        print(f"Playing {track['name']} from {track['band']} from {track['show']}") # type: ignore
    
    if not track:
        return await ctx.send("Song pool is empty!")
    
    ffmpeg_params = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn -ss 30 -t 15' 
    }
    
    audio_source = discord.FFmpegPCMAudio(
    track['stream_url'], 
    executable="C:/ffmpeg/bin/ffmpeg.exe", 
    **ffmpeg_params
    )
    
    await ctx.send("🎶 **Guess the anime song!** You have 15 seconds...")
    vc.play(audio_source)
    
    start_time = asyncio.get_event_loop().time()
    timeout = 15.0
    game_over = False

    def check(message):
        # Must be same channel, not a bot
        return message.channel == ctx.channel and not message.author.bot

    while not game_over:
        # Calculate how much time is actually left
        elapsed = asyncio.get_event_loop().time() - start_time
        remaining = timeout - elapsed

        if remaining <= 0:
            await ctx.send(f"⏰ **Time's up!** No one got it. It was **{track['name']}** from {track['band']}({track['show']})")
            break

        try:
            # Wait for the NEXT message, but only for the remaining time
            guess = await bot.wait_for('message', check=check, timeout=remaining)
            
            user_guess = guess.content.lower().strip()
            name = track['name'].lower().strip()
            band  = track['band'].lower().strip()
            show  = track['show'].lower().strip()

            # Check if correct
            if name or band or show in user_guess:
                await ctx.send(f"✅ **{guess.author.display_name}** got it! It was **{track['name']}** from {track['band']}({track['show']})")
                game_over = True # This breaks the while loop
            else:
                # If wrong, we just do nothing (or add a ❌ reaction) and the loop continues
                await guess.add_reaction("❌") 

        except asyncio.TimeoutError:
            await ctx.send(f"⏰ **Time's up!** The name was **{track['name']}** from {track['band']}({track['show']})")
            break



    
bot.run(discord_token)

