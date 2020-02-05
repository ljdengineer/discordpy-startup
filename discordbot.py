# LJD-bot 試験ビルド
# Patch 1.24
# 懲りずに新機能実装トライ、とりあえず何かしらを動かして糸口を見つけたい

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

# ver1.24 test
region_london = 'ロンドン'
region_japan = '日本'
region_hongkong = '香港'

change_bef = 'に変更します。'
change_aft = 'に変更しました。'

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

# ver1.24 test
@bot.event
async def on_message(message):
    if message.content.startswith('!region london'):
        await bot.send_message(message.channel, region_london + change_bef)
        await bot.edit_guild(message.guild,region='london')
        await bot.send_message(message.channel, region_london + change_aft)
    await bot.process_commands(message)
    elif message.content.startswith('!region japan'):
        await bot.send_message(message.channel, region_japan + change_bef)
        await bot.edit_guild(message.guild,region='japan')
        await bot.send_message(message.channel, region_japan + change_aft)
    await bot.process_commands(message)
    elif message.content.startswith('!region hongkong'):
        await bot.send_message(message.channel, region_hongkong + change_bef)
        await bot.edit_guild(message.guild,region='hongkong')
        await bot.send_message(message.channel, region_hongkong + change_aft)
    await bot.process_commands(message)
    elif message.content.startswith('!ikiteru'):
        reply = '生きてます'
        await bot.send_message(message.channel, reply)
    await bot.process_commands(message)
    
bot.run(token) #おまじない
