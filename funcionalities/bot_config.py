import discord
from discord.ext import commands
from config.token import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
embed = discord.Embed()

