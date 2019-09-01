import discord
import os
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix="*")

@bot.event
async def on_ready():
    print("--------------------")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    return

@bot.command()
async def ping(ctx):
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value=f'🏓 {round(bot.latency * 1000 / 2)}ms')
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def yeet(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send(f"{} get yeeted!".format(ctx.member.mention))

@bot.command()
async def hello(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send(f"Hello {}!".format(ctx.member.mention))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description=f"The command `{ctx.invoked_with}` was not found! We suggest you do `*help` to see all of the commands",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRole):
        roleid = error.missing_role
        embed = discord.Embed(title="Error:",
                              description=f"You don't have permission to execute `{ctx.invoked_with}`, this requires the `{roleid}` role to be executed",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:",
                              description=f"`{error}`",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
        raise error

bot.run(os.getenv('TOKEN'))
