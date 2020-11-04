import discord
from discord.ext import commands

class Diss(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.default_user_to_roast = 'Sean'

  @commands.command()
  async def diss(self, ctx, member: discord.Member = None):
    if member is None or quote is None:
      await ctx.send(f'fuck {self.default_user_to_roast} all my homies hate {self.default_user_to_roast}')
    else:
      await ctx.send(f'fuck <@{member.id}> all my homies hate {member.display_name}')

def setup(client):
  client.add_cog(Headass(client))