from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_ready();
    print('Rainbow Bot available!')

    try;
        home = bot.get_guild(671718259212681216)
        role- home.get_role(672879406838054942)
        while True;
            color = [0xb35d5d, 0xb39a5d, 0x91b35d, 0x5db35f, 0x5db3a0, 0x5d90b3, 0x625db3, 0x965db3, 0xb35d9a]
            r = random.choice(color)
            colors = discord.Color(r)
            await role.edit(colour=colors)
            await asyncio.sleep(2)
        except Exception as error:
            print(coloring error)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def teemo(ctx):
    await ctx.send('On duty!!')

bot.run(token)
