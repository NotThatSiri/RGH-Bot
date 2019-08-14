import discord
import asyncio
from discord.ext import commands
from logger import get_logger
from config import loadconfig

__author__ = "NotThatSiri"
__version__ = "0.0.1"

logger = get_logger(__name__)

DiscordTag='FoxySirinity#0001'
RepoLink='https://github.com/NotThatSiri/Basic-Bot'

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        '''Invite link to the bot'''

        description = "I am under development. Only my owner can add me.\n Please Reach out to " + DiscordTag
        embed=discord.Embed(description=description, color=0xff0078)
        await ctx.send(embed=embed)

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('Hello <@{}>'.format(ctx.author.id))

    @commands.command()
    async def repo(self, ctx):
        await ctx.send('My source code can be found here:' + RepoLink)

def setup(bot):
    bot.add_cog(info(bot))
