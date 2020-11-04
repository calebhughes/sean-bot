import discord
import csv
import random
from datetime import datetime
from discord.ext import commands

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
      await ctx.send('Quote added successfully :ok:')

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





