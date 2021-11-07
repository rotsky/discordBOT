from discord import ButtonStyle, SelectOption
from discord.ui import button, Button, View, select, Select
from discord.interactions import Interaction
from discord.ext import commands
import discord
import oauth

class ButtonsView(View):
    options = []

    def __init__(self, client: discord.Client):

        super().__init__(timeout=None)
        self.client = client

    @button(label='Genre', custom_id='genre_list', style=ButtonStyle.blurple)
    async def button1_clicked(self, button_: Button, interaction: Interaction):
        channel = self.client.get_channel(interaction.channel_id)
        embed = discord.Embed(title="This is your genre list", description=oauth.get_genres_list(),
                              color=discord.Color.purple())
        await channel.send(embed=embed)

    @button(label='Anime', custom_id='anime_list', style=ButtonStyle.blurple)
    async def button2_clicked(self, button_: Button, interaction: Interaction):
        channel = self.client.get_channel(interaction.channel_id)
        embed = discord.Embed(title="This is your anime list", description=oauth.anime_list(),
                              color=discord.Color.purple())
        await channel.send(embed=embed)
