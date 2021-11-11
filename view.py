from discord.ui import button, View, Button
from discord.interactions import Interaction
from discord.ext import commands
from discord import ButtonStyle
import discord
import oauth


class MenuView(View):
    def __init__(self, bot: commands.Bot):
        super().__init__(timeout=None)
        self.bot = bot

    @button(label='Random', custom_id='random_anime', style=ButtonStyle.red)
    async def random_clicked(self, button_: Button, interaction: Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        embed = discord.Embed(title="Random anime", description=oauth.random_anime_list(),
                              color=discord.Color.purple())
        await channel.send(embed=embed)

    @button(label='Genres', custom_id='list_of_genres', style=ButtonStyle.blurple)
    async def genres_clicked(self, button_: Button, interaction: Interaction):
        channel = self.bot.get_channel(interaction.channel_id)
        embed = discord.Embed(title='This is a list of available genres:', description=oauth.get_genres_list(),
                              color=discord.Color.brand_green())
        await channel.send(embed=embed)


