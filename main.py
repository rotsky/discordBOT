import discord
import os
import requests
import time
from buttonsView import ButtonsView
from botToken import token
import oauth


client = discord.Client()

genre = ""
all_names = []
genres = {}


#
# if __name__ == '__main__':
#     print(getGenres())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!anime'):
        embed = discord.Embed(title="What do you want?", color=discord.Color.purple())
        await message.channel.send(embed=embed, view=ButtonsView(client))
        # all_names.clear()
    if message.content.startswith('!genre'):
        embed = discord.Embed(title="What do you want?",
                              color=discord.Color.purple())
        await message.channel.send(embed=embed, view=ButtonsView(client))

    # if message.content.startswith('/anime'):
    #     # print("Work")
    #     embed = discord.Embed(title="What anime do you want to watch?", color=discord.Color.random())
    #     await message.channel.send(embed=embed, view=ButtonsView(client, getGenres()))




client.run(token)