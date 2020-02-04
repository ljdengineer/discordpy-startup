# LJD-bot 試験ビルド
# Patch 1.11
# 1.8で遂に動いた、ただon_readyで入れたメッセージは見えて来ない
# nextは一旦放って置いて、メッセージの出力方法と起動状態をキープし続ける条件の切り分け
## nextに入ってた内容を適用させてみる < これをちょっと修正してみる

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

### ver1.11 test
@bot.event
async def on_ready():
    channel = discord.Object(id='672890703285846016')
    await client.send_message(channel, 'Yay!')
    
bot.run(token) #おまじない
