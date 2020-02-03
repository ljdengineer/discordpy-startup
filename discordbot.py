# LJD-bot 試験ビルド

from discord.ext import commands
import os
import traceback


bot = commands.Bot(command_prefix='/') #Botの接頭辞
token = os.environ['DISCORD_BOT_TOKEN'] #herokuに設定されたtokenを適用させてるっぽい、おまじないの類


@bot.event
async def on_command_error(ctx, error): #接頭辞付きの知らないコマンド来たら動く
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg) #上で色々混ぜたのを出力してるらしい、難しい


@bot.command()
async def ping(ctx):
    await ctx.send(f'No.{i} Latency: {round(bot.latency * 1000)}ms')


@bot.command()
async def teemo(ctx):
    await ctx.send('On duty!!')

bot.run(token) #おまじない
