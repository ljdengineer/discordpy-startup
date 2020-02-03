import discord #-system
from discord.ext import commands #-system
#from discord.ext import tasks #-cycle
#from itertools import cycle #-cycle
import os #-system
import traceback #-system

client = discord.Client() #-in progress_1
bot = commands.Bot(command_prefix='/') #-system
token = os.environ['DISCORD_BOT_TOKEN'] #-system

ID_CHANNEL_README = 673725558898688047 # 該当のチャンネルのID  
ID_ROLE_WELCOME = 673726943538970640 # 付けたい役職のID  

#status = cycle(['Status 1', 'Status 2']) #-cycle


@bot.event #-fixed_general
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event #-fixed_general
async def on_ready
    #change_status.start() #-cycle
    print('bot is ready')

"""
@tasks.loop(seconds=10) #-cycle
async def change_status():
    await client.change_preference(activity=discord.Game(next(status)))
"""

@bot.event #-in progress_1
async def on_raw_reaction_add(payload): 
    channel = client.get_channel(payload.channel_id)  
    if channel.id == ID_CHANNEL_README:  
        guild = client.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id)  
        role = guild.get_role(ID_ROLE_WELCOME)  
        await member.add_roles(role)  
        await channel.send('dekita')  

"""
@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 673725675131240458:
        guild_id = payload.guild_id
        guild = discord.utils.find(lamba g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'lxmage':
            role = discord.utils.get(guild.role, name='mage')
        elif payload.emoji.name == 'lxfighter':
            role = discord.utils.get(guild.role, name='fighter')
        elif payload.emoji.name == 'lxmarksman':
            role = discord.utils.get(guild.role, name='marksman')
        elif payload.emoji.name == 'lxtank':
            role = discord.utils.get(guild.role, name='tank')
        elif payload.emoji.name == 'lxsupport':
            role = discord.utils.get(guild.role, name='support')
        elif payload.emoji.name == 'lxassasin':
            role = discord.utils.get(guild.role, name='assasin')
        else:
            role = discord.utils.get(guild.role, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lamba m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("added")
            else:
                print("Role not found")

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 673725675131240458:
        guild_id = payload.guild_id
        guild = discord.utils.find(lamba g : g.id == guild_id, client.guilds)

        if payload.emoji.name == 'lxmage':
            role = discord.utils.get(guild.role, name='mage')
        elif payload.emoji.name == 'lxfighter':
            role = discord.utils.get(guild.role, name='fighter')
        elif payload.emoji.name == 'lxmarksman':
            role = discord.utils.get(guild.role, name='marksman')
        elif payload.emoji.name == 'lxtank':
            role = discord.utils.get(guild.role, name='tank')
        elif payload.emoji.name == 'lxsupport':
            role = discord.utils.get(guild.role, name='support')
        elif payload.emoji.name == 'lxassasin':
            role = discord.utils.get(guild.role, name='assasin')
        else:
            role = discord.utils.get(guild.role, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lamba m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("removed")
            else:
                print("Role not found")
"""

@bot.command() #-fixed_exp
async def ping(ctx):
    for i in range(5):
        await ctx.send(f'No.{i} Latency: {round(bot.latency * 1000)}ms')

@bot.command() #-fixed_exp
async def teemo(ctx):
    await ctx.send('On duty!!')

bot.run(token) #-fixed_general
