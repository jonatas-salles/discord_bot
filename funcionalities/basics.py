import funcionalities.bot_config as conf

bot = conf.bot

def on_ready():
    print('Bot Online - hello world!')
    print('-'*25)
    bot.run(conf.TOKEN)
    conf.on_ready()

@bot.command()
async def repeat(ctx, *args):
    arguments = ' '.join(args)
    print(arguments)
    await ctx.send(f'{arguments}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'estou online')

@bot.command()
async def userinfo(ctx, member: conf.discord.Member=None):
    if member == None:
        member = ctx.message.author
    embed = conf.discord.Embed(
        title = member.name,
        description= member.mention,
        color = 16777113,
        timestamp=ctx.message.created_at
    )
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name='Joined', value=member.joined_at.strftime(f'%a, %b %d, %Y %I:%M %p'))
    embed.add_field(name='Registered', value=member.created_at.strftime(f'%a, %b %d, %Y %I:%M %p'))
    await ctx.reply(embed = embed)
