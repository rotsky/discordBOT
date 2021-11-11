from discord.ui import button, View, Button
from discord.interactions import Interaction
from discord.ext import commands
import discord

import oauth
from view import MenuView


def setup(bot):
    bot.add_cog(Base_commands(bot))


class Base_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_5_deleted_msg = []
        self.menu_message_id = 0

    @commands.command(name='user')
    async def user(self, ctx):
        embed = discord.Embed(title='Tags an author of the message',
                              description=f'Hello, {ctx.message.author.mention}',
                              colour=65535)
        await ctx.send(embed=embed)

    @commands.command(name='menu')
    async def menu(self, ctx):
        embed = discord.Embed(title='Menu', description='What do you want to do?',
                              colour=65535)
        await ctx.send(embed=embed, view=MenuView(self.bot))

    @commands.command(name='search')
    async def on_message(self, ctx):
        await ctx.channel.send('Type the name of the anime')
        msg = await self.bot.wait_for('message', timeout=30)
        anime = oauth.search_anime(str(msg.content))
        embed = discord.Embed(title=f"{anime[0]['name']}")
        if anime[0]['russian']:
            embed.add_field(name="Russian name: ", value=f"{anime[0]['russian']}")
        picture = anime[0]['image']["original"]
        embed.set_author(name='Shikimori.one', url="https://shikimori.one/",
                         icon_url='https://shikimori.one/favicons/opera-icon-228x228.png')
        embed.add_field(name='Score :', value=f"{anime[0]['score']}")
        embed.add_field(name='Episodes total(released): ',
                        value=f'{anime[0]["episodes"]}({anime[0]["episodes_aired"]})')
        embed.set_thumbnail(url=f"https://shikimori.one{picture}")
        embed.set_footer(text=f"Information requested by: {ctx.author.display_name}")
        await ctx.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Successfully login!')
