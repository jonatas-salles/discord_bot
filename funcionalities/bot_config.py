import discord
from discord import app_commands
from discord.ext import commands
from config.token import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
embed = discord.Embed()

def run_bot():
    bot.run(TOKEN)