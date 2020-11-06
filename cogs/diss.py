import discord
from discord.ext import commands

class Diss(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.default_user_to_roast = 'Sean'

  @commands.command()
  @commands.cooldown(1.0, 60.0, commands.BucketType.user)
  async def diss(self, ctx, member: discord.Member = None):
    message = None
    if member is None:
     message = await ctx.send(f'fuck {self.default_user_to_roast} all my homies hate {self.default_user_to_roast}')
    else:
      message = await ctx.send(f'fuck {member.display_name} all my homies hate {member.display_name}')
    emoji = discord.utils.get(ctx.guild.emojis, name='this')
    await message.add_reaction(emoji)

  @diss.error
  async def diss_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      await ctx.send('Command is on cooldown. Please wait and try again')

def setup(client):
  client.add_cog(Diss(client))