import discord
import random
import praw
import asyncio
from discord.ext import commands

TOKEN = "NTIxODU0NDg0MzI3MTcwMDU3.DvCeiA.DmZ2b0NWv_w-2NhhfJOfJc9WB-I"

client = commands.Bot(command_prefix="n!")
client.remove_command('help')

reddit = praw.Reddit(client_id='521854484327170057',
                     client_secret='yz0giWCchslo2k9JzUiPCnOliiB6I3XF',
                     user_agent='@JayMC#7498')


@client.event
async def on_ready():
    print('Bot online')
    serverCount = len(client.servers)
    await client.change_presence(game=discord.Game(name="to {} servers | n!help".format(serverCount), type = 2))

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcome')
    await channel.send('Welcome {member.mention}')
    role = discord.utils.get(member.guild.roles, name='Member')
    await member.add_roles(role)

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.blue()
        title = "Help"
    )
    embed.add_field(
        name="NSFW",
        value="""
        .pussy-<random pussy>
        .boobs-<random boobs>    
        """,
        inline=False
    )
    embed.add_field(
        name="Fun",
        value="""
        .meme-<random meme>
        """,inline=False
    )
    embed.add_field(
        name="Info",
        value="""
        .ping-<returns ping and trajectory>    
        """,
        inline=False
    )
    embed.add_field(
        name="Moderation",
        value="""
        .clear <number>-purges a number of messages
        """,
        inline=False
    )          
    await client.say(embed=embed)

@client.command(pass_context=True)
async def meme(ctx):
    if ctx.channel.is_nsfw():
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await client.say(submission.url)
    else:
        await client.say("This command is NSFW-only")

@client.command(pass_context=True)
async def pussy(ctx):
    if ctx.channel.is_nsfw():
        pussy_submissions = reddit.subreddit('pussy').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in pussy_submissions if not x.stickied)

        await client.say(submission.url)
    else:
        await client.say("This command is NSFW-only")

@client.command(pass_context=True)
async def boobs(ctx):
    if ctx.channel.is_nsfw():
        boobs_submissions = reddit.subreddit('boobs').hot()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in boobs_submissions if not x.stickied)

        await client.say(submission.url)
    else:
        await client.say("This command is NSFW-only")

@client.command(pass_context = True)
@commands.has_permissions(manage_=True)
async def clear(ctx, number: int):
    await client.purge_from(ctx.message.channel, limit=number)
@_clear.error
async def clear_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await client.say("You can't run this command.")

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
    """Kicks A User from server"""
    await client.kick(userName)
    await client.say(":ballot_box_with_check: __**Successfully User Has Been Kicked!**__")
@_kick.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await client.say("You can't run this command.")

@client.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
    """bans A User from server"""
    await client.ban(userName)
    await client.say(":ballot_box_with_check: __**Successfully User Has Been Banned!**__")
@_ban.error
async def ban_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await client.say("You can't run this command.")

@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.User):
    role = discord.utils.get(member.server.roles, name='Muted')
    await client.add_roles(member, role)
    await client.send_message(client.get_channel('514577378656256000'), 'A user has been Muted! ***SHAME!***')
@_mute.error
async def mute_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await client.say("You can't run this command.")

@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.User):
    role = discord.utils.get(member.server.roles, name='Muted')
    await client.remove_roles(member, role)
@_unmute.error
async def unmute_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await client.say("You can't run this command.")

client.run(TOKEN)


        