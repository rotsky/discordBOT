from discord.interactions import Interaction
from discord.ext import commands
import discord

import oauth
from view import MenuView


def setup(bot):
    bot.add_cog(Admin_commands(bot))


class Admin_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='quit')
    @commands.is_owner()
    async def quit(self, ctx):
        await ctx.send('Oh, im die, thank you foreva:)')
        await self.bot.close()

    # @commands.command(name='refresh_token')
    # @commands.is_owner()
    # async def refreshToken(self, ctx):
    #     await ctx.send('Refreshing token')
    #     oauth.refresh()
    #     self.bot.clear()

    @commands.command(name='restart')
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.send('Will be right back')
        self.bot.clear()

