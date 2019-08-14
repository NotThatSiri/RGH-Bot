import discord
import asyncio
from discord.ext import commands
from logger import get_logger
from config import loadconfig

__author__ = "NotThatSiri"
__version__ = "0.0.1"

logger = get_logger(__name__)

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['boot'])
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member=None, *reason):
        '''ban a member with a reason
        Example:
        -----------
        a/ban @bob#1234
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.ban(reason=reason)
            description = "I have banned **{}** for **{}**".format(member,reason)
            embed=discord.Embed(description=description, color=0xE82E2E)
            await ctx.send(embed=embed)
        else:
            await ctx.send('I am sorry, but I cannot find that user')

    @commands.command(aliases=['resurrect'])
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def unban(self, ctx, user: discord.User=None, *reason):
        '''unban a member with a reason
        example:
        -----------
        a/unban 102815825781596160
        '''
        if user is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await ctx.guild.unban(user, reason=reason)
            await ctx.send('I unbanned {} as your requested'.format(user))
        else:
            await ctx.send('I am sorry, but I cannot find that user')

    @commands.command(aliases=['prune'])
    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def purge(self, ctx, *limit):
        '''delete amount of messages
        Example:
        -----------
        a/purge 100
        '''
        try:
            limit = int(limit[0])
        except IndexError:
            limit = 1
        deleted = 0
        while limit >= 1:
            cap = min(limit, 100)
            deleted += len(await ctx.channel.purge(limit=cap, before=ctx.message))
            limit -= cap
        tmp = await ctx.send(f'I have deleted {deleted} messages as you requested.')
        await asyncio.sleep(5)
        await tmp.delete()
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *reason):
        '''Kick a member with a reason
        example:
        -----------
        a/kick @bob#1234
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.kick(reason=reason)
            await ctx.send("I have kicked **{}** for **{}**".format(member,reason))
        else:
            await ctx.send('I am sorry, but I cannot find that user')

def setup(bot):
    bot.add_cog(mod(bot))
