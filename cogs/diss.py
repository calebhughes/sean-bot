import discord
from discord.ext import commands

class Diss(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.default_user_to_roast = 'Sean'

  @commands.command()
  async def diss(self, ctx, member: discord.Member = None):
    message = None
    if member is None:
     message = await ctx.send(f'fuck {self.default_user_to_roast} all my homies hate {self.default_user_to_roast}')
    else:
      message = await ctx.send(f'fuck <@{member.id}> all my homies hate {member.display_name}')
    emoji = discord.utils.get(ctx.guild.emojis, name='this')
    await message.add_reaction(emoji)

def setup(client):
  client.add_cog(Diss(client))