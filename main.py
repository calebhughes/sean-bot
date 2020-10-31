#!/usr/bin/env python3

import discord
import re
import headass
import os

from dateutil import tz
from dotenv import load_dotenv

# Load the environment file that holds our token
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_API_TOKEN")

client = discord.Client()
prog = re.compile('(\s+69\s+)|(^69\s+)|(^69$)|(.*\s+69.*)') # 69 regex blaze it

def format_time(utc):
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    updated_time = utc.replace(tzinfo=from_zone)
    return updated_time.astimezone(to_zone)

async def delete_user_last_message(invoke_message):
    async for m in invoke_message.channel.history(limit=20):
        if m.author == invoke_message.author and m.id != invoke_message.id:
            await m.delete()
            await invoke_message.delete()
            break


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Fuck Sean'))

@client.event
async def on_message(message):
    if prog.match(message.content):
        await message.channel.send('nice')
    elif 'nice' == message.content.lower() and not message.author.bot:
        await message.channel.send('super nice')
    elif message.content.startswith(';del'):
        await delete_user_last_message(message)
    elif message.content.startswith(';fucksean'):
        await message.channel.send('fuck sean all my homies hate sean')
    elif message.content.startswith(';headass'):
        result = headass.parse_command(message)
        if result != '':
            await message.channel.send(result)

client.run(DISCORD_TOKEN)
