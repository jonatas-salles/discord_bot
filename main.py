from funcionalities.basics import *
from funcionalities.dice_roller import *


on_ready()

repeat(conf.discord.ext.Context.message)

ping(conf.discord.ext.Context.message)

roll(conf.discord.ext.Context.message)

userinfo(conf.discord.ext.Context.message)