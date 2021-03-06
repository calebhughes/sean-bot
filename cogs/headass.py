import discord
import csv
import random
from datetime import datetime
from discord.ext import commands
from discord.utils import get

class Headass(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.filename = "headass_quotes.csv"
  
  @commands.command()
  async def addquote(self, ctx, member: discord.Member = None, *, quote):
    if member is None or quote is None:
      await ctx.send('You must include a valid member and a quote for this command')
    else:
      self.save_quote(member, quote)
      await ctx.send('Quote added successfully :ok_hand:')

  def save_quote(self, member: discord.Member, quote):
    with open(self.filename, 'a+', newline='') as csvfile:
      writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
      writer.writerow([member.id, quote, datetime.now()])

  @commands.command()

  async def headass(self, ctx):
    member, quote, when = self.get_quote()
    if member is None:
      await ctx.send(quote)
    else:
      when_dt = datetime.strptime(when, '%Y-%m-%d %H:%M:%S.%f')
      formatted_time = when_dt.strftime('%m-%d-%Y')
      await ctx.send(f'<@{member}> on {formatted_time} "{quote}"')

  @headass.error
  async def headass_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send('Command is on cooldown. Please wait and try again.')
    else:
      pass

  @commands.command()
  async def quotelist(self, ctx):
    embed = discord.Embed(title='List of Saved Quotes', description='', color=0x03f4fc)
    desc = ''
    with open(self.filename, 'r+') as f:
      reader = csv.reader(f, delimiter=',')
      lines = list(reader)
      desc = '\n'.join(f'{i+1}. <@{line[0]}> {line[1]}' for i,line in enumerate(lines))
      embed.description = desc
    await ctx.message.channel.send(embed=embed)


  def get_quote(self):
    with open(self.filename, 'r+') as f:
      reader = csv.reader(f, delimiter=',')
      lines = list(reader)
      if not lines:
        return None,'No quotes added yet',None
      else:
        return random.choice(lines)

def setup(client):
  client.add_cog(Headass(client))





