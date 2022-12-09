import discord
from discord.ext import commands
from config.token import TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
embed = discord.Embed()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='dados viciados'))

