#!/usr/bin/env python3

import discord
import re
import headass
import os
from dateutil import tz

client = discord.Client()
prog = re.compile('(\s+69\s+)|(^69\s+)|(^69$)|(.*\s+69*)') # 69 regex blaze it

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

@client.event
async def on_message(message):
    # print(f'[{format_time(message.created_at):%Y-%m-%d %I:%M %p}] {message.author.display_name} in {message.channel.name}: {message.content}')
    if prog.match(message.content):
        await message.channel.send('nice')
    elif 'nice' in message.content and not message.author.bot:
        await message.channel.send('super nice')
    elif message.content.startswith(';del'):
        await delete_user_last_message(message)
    elif message.content.startswith(';headass'):
        result = headass.parse_command(message)
        if result != '':
            await message.channel.send(result)
    elif 'Sean' in message.content:
        await message.channel.send('fuck sean all my homies hate sean')

client.run(os.environ['DISCORD_API_KEY'])
