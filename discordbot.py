from discord.ext import commands
import os
import traceback
import time

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def ping(ctx):
    for i in range(5):
        await ctx.send(f'No.{i} Latency: {round(bot.latency * 1000)}ms')
        time.sleep(1)

@bot.command()
async def teemo(ctx):
    await ctx.send('On duty!!')

bot.run(token)
