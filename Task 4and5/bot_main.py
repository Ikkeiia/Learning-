import asyncio
import discord
import random
from discord.ext import commands

##Local imports
#importing tokens for mal and dc bot
from tokens import mal_token, discord_token
from Functions import *

mal=MALClient(mal_token)
game = SongGuessing()

description = 'Anime bot'
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
async def play(ctx, option=""):
    """
    Usage: 
    $play 
    $play -random  random = random start time and random time to guess
    """
    
    track = None
    global last_played_track 
    

    if not ctx.author.voice:
        return await ctx.send("Join a voice channel first!")

    vc = ctx.voice_client
    if not vc:
        vc = await ctx.author.voice.channel.connect()


    async with ctx.typing():
        # REPEAT
        if option == "-again":
            if last_played_track:
                track = last_played_track
                print(f" again debug{last_played_track}") ###debug
                await ctx.send("🔄 **Replaying the last song...**")
            else:
                return await ctx.send("No previous song found to repeat!")
        else:
            # Normal play
            track = game.get_random_track()
            last_played_track = track 
            print(f"normal play debug: {last_played_track}") ###debug

    if option == "" or "-again":
        #timet to guess
        ttguess = 15
        ffmpeg_params = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': f'-vn -ss 30 -t {ttguess}' 
        }
    elif option == "-random":
        ttguess = random.randint(10,15)
        start_offset = random.randint(1, 40)

        ffmpeg_params = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': f'-vn -ss {start_offset} -t {ttguess}' 
        }
    else: await ctx.send("Wrong option")

    if option == "":
        audio_source = discord.FFmpegPCMAudio(track['stream_url'], 
        executable="C:/ffmpeg/bin/ffmpeg.exe", 
        **ffmpeg_params # type: ignore
        )
        # print(ffmpeg_params) ###debug
        await ctx.send(f"🎶 **Guess the anime song!** You have {ttguess} seconds...")
        vc.play(audio_source)

    else:
        audio_source = discord.FFmpegPCMAudio(last_played_track['stream_url'], 
        executable="C:/ffmpeg/bin/ffmpeg.exe", 
        **ffmpeg_params # type: ignore
        )
        # print(ffmpeg_params) ###debug
        await ctx.send(f"🎶 **Guess the anime song!** You have {ttguess} seconds...")
        vc.play(audio_source)

        
    start_time = asyncio.get_event_loop().time()
    timeout = ttguess

    def check(message):
        # Must be same channel, not a bot
        return message.channel == ctx.channel and not message.author.bot
    
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

    while True:
        # Calculate how much time is actually left
        elapsed = asyncio.get_event_loop().time() - start_time
        remaining = timeout - elapsed

        if remaining <= 0:
            if vc.is_playing():
                vc.stop()
            await ctx.send(f"⏰ **Time's up!** No one got it do you want to try again?")    
            if 
            break

        try:
            # Wait for the NEXT message, but only for the remaining time
            guess = await bot.wait_for('message', check=check, timeout=remaining)
            user_guess = guess.content.lower().strip()
            correct_guess = [track['name'].lower(), track['band'].lower(), track['show'].lower()]
            print(correct_guess) ###debug

            # Check if correct
            if any(user_guess in ans or ans in user_guess for ans in correct_guess if len(user_guess) > 2):
                if vc and vc.is_playing():
                    vc.stop()                

                await ctx.send(f"✅ **{guess.author.display_name}** got it! It was", embed=embed1,) 
                break

                
            else:
                # If wrong, we just do nothing (or add a ❌ reaction) and the loop continues
                await guess.add_reaction("❌") 

        except asyncio.TimeoutError:
            if vc and vc.is_playing():
                vc.stop()
            await ctx.send(f"⏰ **Time's up!** No one got it" , embed=embed1)
            break


        except discord.errors.ClientException:
            break


    
bot.run(discord_token)

