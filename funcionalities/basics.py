import funcionalities.bot_config as conf

bot = conf.bot

def on_ready():
    print('Bot Online - hello world!')
    print('-'*25)
    bot.run(conf.TOKEN)
    conf.on_ready()

@bot.command()
async def repeat(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{arguments}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'estou online')

# --- test
#   embed = conf.discord.Embed(
#             title = ctx.author,
#             description =  arguments,
#             color = 16777113
#     )
#     await ctx.send(embed = embed)