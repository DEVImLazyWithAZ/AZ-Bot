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
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason='No reason provided.'):
    if member.bot == True:
        await member.ban(reason=reason)
        await ctx.message.delete()
        await ctx.send(f'{member} has been banned.')
    else:
        dm = discord.Embed(title="You have been banned!", color=0xAA00FF)
        dm.add_field(name="Moderator:",
                        value=ctx.message.author.display_name)
        dm.add_field(name="Reason:", value=f"{reason}")
        dm.set_thumbnail(url=member.avatar_url)
        await member.send(embed=dm)  # Send DM
        await member.ban(reason=reason)  # Ban
        await ctx.message.delete()  # Delete The Message
        await ctx.send('member has been banned.') 

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
        
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason='No reason provided.'):
    if member.bot == True:
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.send(f'{member} has been kicked.')
    else:
        dm = discord.Embed(title="You have been kicked!", color=0xAA00FF)
        dm.set_thumbnail(url=member.avatar_url)
        dm.add_field(name="Reason:", value=f"{reason}")
        dm.add_field(name="Moderator:",
                        value=ctx.message.author.display_name)
        await member.send(embed=dm)  # Send DM
        await member.kick(reason=reason)  # Kick
        await ctx.message.delete()  # Delete The Message
        await ctx.send('member has been kicked.')
 
@bot.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member=None):
    if discord.utils.get(ctx.guild.roles, name="muted") is None:
      guild = ctx.guild
      await guild.create_role(name="muted")
    if not member:
        await ctx.send("Please specify a member.")
        return
    else:
      role = discord.utils.get(ctx.guild.roles, name="muted")
      await member.add_roles(role)
      await ctx.send("Role added!")
    
@bot.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member = None):
    role = discord.utils.get(ctx.guild.roles, name="muted")
    if not member:
        await ctx.send("Please specify a member.")
        return
    await member.remove_roles(role)
    await ctx.send("Role removed!")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    """Clears the amount of messages that you filled in."""
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"{amount} messages got deleted.")
    
@bot.command()
async def hello(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send("Hello {}!".format(member.mention))

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Kiwi", description="Commands:", color=0x7289DA)

    embed.set_thumbnail(
        url='https://images.emojiterra.com/twitter/v12/512px/1f3d3.png')
    embed.add_field(name="*kick", value="Kicks a member.", inline=False)
    embed.add_field(name="*ban", value="Bans a member.", inline=False)
    embed.add_field(name="*mute", value="Mutes a member.", inline=False)
    embed.add_field(name="*unmute", value="Unmutes a member.", inline=False)
    embed.add_field(name="*unban", value="Unbans a user.", inline=False)
    embed.add_field(name="*clear", value="Clears the amount of messages that you filled in.", inline=False)
    embed.add_field(name="*ping", value="Pings the bot.", inline=False)
    embed.add_field(name="*help", value="Gives this message.", inline=False)
    embed.add_field(name="*hello", value="Says hello to you.", inline=False)
    embed.add_field(name="*say", value="Says what you want!.", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

@bot.command()
async def support(ctx, member : discord.Member= None):
    member = ctx.author if not member else member
    await ctx.send("The support server for AZ's Bot is https://discord.gg/NJ9mr9C!") 

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description=f"The command `{ctx.invoked_with}` was not found! We suggest you do `help` to see all of the commands",
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
