import discord
from discord.ext import commands
from botToken import token

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='-', intents=intents, self_bot=False)
bot.load_extension('base_commands')
bot.load_extension('admin_commands')


if __name__ == '__main__':
    bot.run(token)
