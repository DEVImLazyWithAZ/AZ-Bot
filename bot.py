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

bot.remove_command('help')

@bot.command()
async def ping(ctx):
    embed = discord.Embed(colour=0x00FF00)
    embed.add_field(name="Ping", value=f'🏓 {round(bot.latency * 1000 / 2)}ms')
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def yeet(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send("{} get yeeted!".format(member.mention))

@bot.command()
async def hello(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send("Hello {}!".format(member.mention))

@bot.command()
async def overrideenable(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send("Hello {} your override mode is on!!".format(member.mention))

@bot.command()
async def overridedisable(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send("Hello {} your override mode is off!!".format(member.mention))


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="AZ's bot", description="Commands:", color=0x7289DA)

    embed.set_thumbnail(
        url='https://images.emojiterra.com/twitter/v12/512px/1f3d3.png')
    embed.add_field(name="*ping", value="Pings the bot.", inline=False)
    embed.add_field(name="*help", value="Gives this message.", inline=False)
    embed.add_field(name="*yeet [@member]", value="Yeets someone.", inline=False)
    embed.add_field(name="*hello", value="Says hello to you.", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)
    
@bot.command()
@commands.has_any_role("imlazyazlol")
async def pingspam(ctx, member : discord.Member= None):
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
    await ctx.send("{}".format(member.mention))
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description=f"The command `{ctx.invoked_with}` was not found! We suggest you do `*help` to see all of the commands",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:",
                              description=f"`{error}`",
                              colour=0xe73c24)
        await ctx.send(embed=embed)
        raise error

bot.run(os.getenv('TOKEN'))
