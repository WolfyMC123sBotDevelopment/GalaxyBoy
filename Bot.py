import discord
from discord.ext import commands

TOKEN 'NTIxMzc3ODg0MTMzMjYxMzMz.Du7i_g.jR_BfeI1pWSCvlHq5O_MfjLsDN8'

client = commands.Bot(command_prefix = '.')
client.remove_commands('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='.help'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='User')
    await client.add_roles(member, role)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_author(name='Help')
    embed.add_field(name='Common Commands', value='.invite <gives invite for bot> / .support <support server>')
    embed.add_field(name='Fun Commands', value='.ping <returns pong> / .8ball <random output to your question> / .echo <output>', inline=True)
    embed.add_field(name='Moderation Commands', value='.clear <amount limit=100> / .kick <user> <reason optional> / .ban <user> <reason optional>', inline=True)
    embed.add_field(name='NSFW Commands', value='.boobs <random boobs> / .milf <random milf> / .pussy <random pussy', inline=True)

@client.command()
async def ping():
    await client.say(':ping_pong: Pong!')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(messages)
    await client.delete_messages(messages)
    await client.say('Messages Deleted')

@client.command(pass_context=True)
async def pussy(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'Pussy',
        description = 'Heres your pussy.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Random Pussy')
    embed.set_image(url='https://www.pornpics.com/pussy/')
    embed.set_thumbnail(url='https://www.pornpics.com/pussy/')
    embed.set_author(name='www.pornpics.com'),
    icon_url='https://www.pornpics.com/pussy/')
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)

@client.command(pass_context=True)
async def boobs(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'Boobs',
        description = 'Heres your boob.',
        colour = discord.colour.blue()
    )

    embed.set_footer(text='Random boob')
    embed.set_image(url='https://www.pornpics.com/big-tits/')
    embed.set_thumbnail(url='https://www.pornpics.com/big-tits/')
    embed.set_author(name='www.pornpics.com'),
    icon_url='https://www.pornpics.com/big-tits/')
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)

    await client.say(embed=embed)
    await client.send_message(channel, embed=embed)

@client.command(pass_context=True)
async def milf(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'Milf',
        description = 'Milf.',
        colour = discord.colour.blue()
    )

    embed.set_footer(text='Random Milf')
    embed.set_image(url='https://www.pornpics.com/milf/')
    embed.set_thumbnail(url='https://www.pornpics.com/milf/')
    embed.set_author(name='www.pornpics.com'),
    icon_url='https://www.pornpics.com/milf/')
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)
    embed.add_field(name='Want more', value='well check pornpics.com', inline=True)

    await client.say(embed=embed)
    await client.send_message(channel, embed=embed)

@client.command(pass_context=True)
async def invite(ctx):
    await client.say('Heres your link https://discordapp.com/api/oauth2/authorize?client_id=521377884133261333&permissions=8&scope=bot')

@client.command(pass_context=True)
async def support(ctx):
    await client.say('Support Server https://discord.gg/m9jGrCP')

client.run(TOKEN)
