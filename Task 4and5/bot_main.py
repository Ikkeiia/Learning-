import asyncio
import discord
import random
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
async def play(ctx, ran=""):
    """
    Usage: $play / $play -random
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
    
    if ran == "":
        ffmpeg_params = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn -ss 30 -t 15' 
        }
    elif ran == "-random":
        ffmpeg_params = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': f'-vn -ss {random.randint(1,40)} -t 15' 
        }
    else: await ctx.send("Wrong option")


    audio_source = discord.FFmpegPCMAudio(
    track['stream_url'], 
    executable="C:/ffmpeg/bin/ffmpeg.exe", 
    **ffmpeg_params
    )
    print(ffmpeg_params)
    await ctx.send("🎶 **Guess the anime song!** You have 15 seconds...")
    vc.play(audio_source)
    
    start_time = asyncio.get_event_loop().time()
    timeout = 15.0

    def check(message):
        # Must be same channel, not a bot
        return message.channel == ctx.channel and not message.author.bot
    
    def result_embed():
        embed1 = discord.Embed(
            title=f"Correct song: {track['name']}",
            # Masked link in the description
            description=(
                f"**Author:** {track['band']}\n"
                f"**Anime:** {track['show']}\n\n"
                f"🔗 **[Watch on YouTube]({track['yt_url']})**"
            )
        )

        embed1.set_image(url=track['thumbnail'])

        # Optional: Keep the raw URL in the footer or remove it for a cleaner look
        embed1.set_footer(text="Click the link above to listen!")
        return embed1

    while True:
        # Calculate how much time is actually left
        elapsed = asyncio.get_event_loop().time() - start_time
        remaining = timeout - elapsed

        if remaining <= 0:
            if vc.is_playing():
                vc.stop()
            await ctx.send(f"⏰ **Time's up!** No one got it", embed=result_embed())    
            break

        try:
            # Wait for the NEXT message, but only for the remaining time
            guess = await bot.wait_for('message', check=check, timeout=remaining)
            user_guess = guess.content.lower().strip()
            correct_guess = [track['name'].lower(), track['band'].lower(), track['show'].lower()]
            print(correct_guess)

            # Check if correct
            if any(user_guess in ans or ans in user_guess for ans in correct_guess if len(user_guess) > 2):
                if vc and vc.is_playing():
                    vc.stop()                

                await ctx.send(f"✅ **{guess.author.display_name}** got it! It was", embed=result_embed(),) 
                break

                
            else:
                # If wrong, we just do nothing (or add a ❌ reaction) and the loop continues
                await guess.add_reaction("❌") 

        except asyncio.TimeoutError:
            if vc and vc.is_playing():
                vc.stop()
            await ctx.send(f"⏰ **Time's up!** No one got it" , embed=result_embed())
            break


        except discord.errors.ClientException:
            break


    
bot.run(discord_token)

