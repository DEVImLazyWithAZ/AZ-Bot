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
async def say(ctx, *, args):
    await ctx.message.delete() 
    output = ''
    for word in args:
        output += word
        output += ''
    await ctx.send(output)
    
@bot.command()
async def creepah(ctx):
    await ctx.send("Aww man so we back in the mines got our pickaxe swinging from side to side side side to side This task a grueling one hope to find some diamonds tonight, night, night, diamonds tonight. Heads up. You hear a sound turn around and look up. Total shock fills your body, Oh no it's you again, I can never forget those eyes eyes eyes, eyes eyes eyes Cause baby tonight, the creeper's tryin' to steal all our stuff again Cause baby tonight, you grab your pick shovel and bolt again, bolt again, gain,            ImLazyWithAZ was to lazy to put the rest of the song in so that's all")
    
    @bot.command()
async def alan(ctx):
    await ctx.send("#RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN #RESPECTFORALAN")
    
@bot.command()
async def yeet(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send("{} get yeeted boyo!".format(member.mention))

@bot.command()
async def IdleGuild(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send("Join the Idle Miner guild by Direct Messaging @ImLazyWithAZ#8327!")
    
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
    embed.add_field(name="*creepah", value="Aww man.", inline=False)
    embed.add_field(name="*IdleGuild", value="Join the Idle Miner Guild!.", inline=False)
    embed.add_field(name="*say", value="Says what you want!.", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)
    
@bot.command()
@commands.has_any_role("Ping Spammer - Approved by ImLazyWithAZ")
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
    await ctx.send("Hello {}. I'm sorry that the process took so long. Heroku speeds SUCK".format(member.mention))

        
bot.run(os.getenv('TOKEN'))
