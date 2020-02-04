# LJD-bot 試験ビルド
# Patch 1.23
# 何にも動かせねえから痕跡だけ残して一旦クリアに

# Base
from discord.ext import commands
import os
import traceback
# 初期設定
bot = commands.Bot(command_prefix='/') #Botの接頭辞
token = os.environ['DISCORD_BOT_TOKEN'] #herokuに設定されたtokenを適用させてるっぽい、おまじないの類

""" ver1.22 test までやってた化石、結局うごかず。
channel = discord.utils.get(guild.text_channels, name='temp-ch-01')
"""

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

""" ver1.17 までやってた化石、結局うごかず。
@bot.event
async def on_ready(channel):
    channel = discord.utils.get(guild.text_channels, name='test01')
    await channel.send('Yay!')
"""

""" ver1.22 test までやってた化石、結局うごかず。
@bot.event
async def on_member_update(before, after):
    if before.status != after.status:
        msg = after.display_name + " さんが " + str(after.status) + " になりました"
        await discord.bot().send_message(channel,msg)
"""
    
bot.run(token) #おまじない
