# LJD-bot 試験ビルド
# Patch 1.8
# 1.7もまた落ちた、下手な鉄砲も数撃ちゃ当たる的なテスト

# Base
from discord.ext import commands
import os
import traceback


# 初期設定
bot = commands.Bot(command_prefix='/') #Botの接頭辞
token = os.environ['DISCORD_BOT_TOKEN'] #herokuに設定されたtokenを適用させてるっぽい、おまじないの類

# 初期搭載機能群ここから
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
# 初期搭載機能群ここまで

### ver1.8 test
@bot.event
async def on_ready(channel):
    channel = 672890703285846016:
    await message.channel.send('Yay!')
    
bot.run(token) #おまじない
