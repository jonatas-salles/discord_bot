import re
from random import randint
import funcionalities.bot_config as conf

bot = conf.bot

@bot.command()
async def roll(ctx, *args):
    arguments = ', '.join(args)

    if (re.search('^[0-9]+?d[0-9]+$', arguments)):
        results = []
        rolls = int(arguments.split('d')[0])
        sides = int(arguments.split('d')[-1])

        for i in range(0, rolls):
            results.append(randint(1, sides))
            i+=1
        
        result = dice_result_format(arguments, results, sides)

        await ctx.reply(result)
    
    else:
        await ctx.reply('Invalid arguments.')

def dice_result_format(msg, results, sides):
    higher = results[0]
    new_results = []
    results.sort(reverse=True)
    
    for result in results:
        if result > higher:
            higher = result

        if result == sides or result == 1:
            new_results.append(f'**{result}**')
        else:
            new_results.append(result)

    str = f'`` {higher} `` ⟵ {new_results} {msg}'.replace("'", "")

    return str