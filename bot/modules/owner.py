import discord

from discord.ext import commands
from logger import get_logger
from config import loadconfig

__author__ = "NotThatSiri"
__version__ = "0.0.1"

logger = get_logger(__name__)


class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['quit'])
    @commands.is_owner()
    async def shutdown(self, ctx):
        '''Stopping the bot :('''
        await ctx.send('I am sorry I did something wrong, I will take my leave. Bye!')
        await self.bot.logout()
        sys.exit(0)

    @commands.command(aliases=['game'])
    @commands.is_owner()
    async def changegame(self, ctx, gameType: str, *, gameName: str):
        '''Change the bots playing game'''
        gameType = gameType.lower()
        if gameType == 'playing':
            type = discord.ActivityType.playing
        elif gameType == 'watching':
            type = discord.ActivityType.watching
        elif gameType == 'listening':
            type = discord.ActivityType.listening
        elif gameType == 'streaming':
            type = discord.ActivityType.streaming
        await self.bot.change_presence(activity=discord.Activity(type=type, name=gameName))
        await ctx.send(f'I am now {gameType} {gameName}')

    @commands.command(aliases=['status'])
    @commands.is_owner()
    async def changestatus(self, ctx, status: str):
        '''Change the  Online Status of the Bot'''
        status = status.lower()
        if status == 'offline' or status == 'off' or status == 'invisible':
            discordStatus = discord.Status.invisible
        elif status == 'idle':
            discordStatus = discord.Status.idle
        elif status == 'dnd' or status == 'disturb':
            discordStatus = discord.Status.dnd
        else:
            discordStatus = discord.Status.online
        await ctx.send(f'I have changed my status to {status}')
        await self.bot.change_presence(status=discordStatus)

    @commands.command()
    @commands.is_owner()
    async def name(self, ctx, name: str):
        '''Changes the global name of the Bot'''
        await self.bot.edit_profile(username=name)

    @commands.command(aliases=['guilds'])
    @commands.is_owner()
    async def servers(self, ctx):
        '''Lists the current servers the bot is in'''
        msg = 'I am in the following servers:\n```js\n'
        msg += '{!s:19s} | {!s:>5s} | {} | {}\n'.format('ID', 'Member', 'Name', 'Owner')
        for guild in self.bot.guilds:
            msg += '{!s:19s} | {!s:>5s}| {} | {}\n'.format(guild.id, guild.member_count, guild.name, guild.owner)
        msg += '```'
        await ctx.send(msg)

    @commands.command()
    @commands.is_owner()
    async def leaveserver(self, ctx, guildid: str):
        '''get the bot to leave a server
        syntax:
        -----------
        :leaveserver 102817255661772800
        '''
        guild = self.bot.get_guild(guildid)
        if guild:
            await self.bot.leave_guild(guild)
            msg = 'I have left **{}** successfully!'.format(guild.name)
        else:
            msg = 'I could not find the server with that id'
        await ctx.send(msg)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        cogfix = 'modules.'+cog

        try:
            self.bot.load_extension(cogfix)
        except Exception as e:
            await ctx.send(f'I could not load module due to:\n```{type(e).__name__} - {e}```')
            logger.warning(f'Couldn\'t load cog {cog}')
            logger.error(e)
        else:
            await ctx.send(f'I have successfully loaded **{cog}**.')
            logger.info('<{0}> Loaded successfully.'.format(cog))

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        cogfix = 'modules.'+cog

        try:
            self.bot.unload_extension(cogfix)
        except Exception as e:
            await ctx.send(f'I could not unload module due to:\n```{type(e).__name__} - {e}```')
            logger.warning(f'Couldn\'t unload cog {cog}')
            logger.error(e)
        else:
            await ctx.send(f'I have successfully unloaded **{cog}**.')
            logger.info('<{0}> Unloaded successfully.'.format(cog))

    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        cogfix = 'modules.'+cog

        try:
            self.bot.unload_extension(cogfix)
            self.bot.load_extension(cogfix)
        except Exception as e:
            await ctx.send(f'I could not reload module due to:\n```{type(e).__name__} - {e}```')
            logger.warning(f'Couldn\'t reload cog {cog}')
            logger.error(e)
        else:
            await ctx.send(f'I have successfully reloaded **{cog}**.')
            logger.info('<{0}> reloaded successfully.'.format(cog))

def setup(bot):
    bot.add_cog(owner(bot))
