#!/usr/bin/env python3
import discord
import re
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load the environment file that holds our token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_TOKEN")

client = commands.Bot(command_prefix=';')
prog = re.compile('(\s+69\s+)|(^69\s+)|(^69$)|(.*\s+69.*)') # 69 regex blaze it

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Fuck Sean'))

@client.event
async def on_command_error(ctx, error):
    pass

@client.command(aliases=['del'],name='delete')
async def delete_last_message(ctx):
    message = ctx.message
    async for m in message.channel.history(limit=20):
        if m.author == message.author and m.id != message.id:
            await m.delete()
            await message.delete()
            break

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def prefix(ctx, new_prefix):
    if new_prefix is None:
        await ctx.send('You must include a new prefix to set')
    else:
        client.command_prefix = new_prefix

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(DISCORD_TOKEN)
