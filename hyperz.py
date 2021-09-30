import discord
from discord.ext import commands, tasks
import youtube_dl

from random import choice

client = commands.Bot(command_prefix='-')
status = ["What's up! Use me with '-'", "Playing Music", "Sleeping!"]

@client.event
async def on_ready():
    change_status.start()
    print('Bot is Online!')


@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Ping!** Latency: {round(client.latency * 1000)}ms')

@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['What up bruv!', 'Wazzzup!', 'Hi!']
    await ctx.send(choice(responses))

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


client.run('ODkyOTM4NDIzMTY0MzU0NjUw.YVULtg.zUTySK0-dQknAJCbYH8Pza7eFgE')