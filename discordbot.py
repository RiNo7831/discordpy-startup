from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.command()
async def RiNo(ctx):
    await ctx.send('天才☆')

@bot.command()
async def ONE(ctx):
    await ctx.send('おーね♡')

@bot.command()
async def inu(ctx):
    await ctx.send('わん')

@bot.command()
async def ここがいいんだろ(ctx):
    await ctx.send('えりなむ...')

@bot.command()
async def hello(ctx):
    d = ['こんぺこ〜', 'こんにちは', 'やっほー', 'hello', 'ども', 'だなも', 'こんちゃっちゃー', 'ぶんぶんハローdiscord']
    random.shuffle(d)
    await ctx.send(d[0])

@bot.command()
async def room(ctx):
    await ctx.send(list)

@bot.command()
async def help(ctx):
    await ctx.send('open 部屋名 , close 部屋名 \n team 部屋名　チーム数')

@bot.command()
async def dice(ctx):
    d = [1, 2, 3, 4, 5, 6]
    random.shuffle(d)
    await ctx.send(d[0])

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
