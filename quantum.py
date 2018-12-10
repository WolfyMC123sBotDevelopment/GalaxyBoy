import discord
from discord.ext import commands

TOKEN ='NTIxNDk0NzIyMTEyNTIwMjA3.Du9QgA.FcorKoPrhdIK2Fz2EMhbhK1MdkM'
client = commands.Bot(command_prefix = 'q.')
client.remove_command('help')

extensions = ['fun', 'moderation', 'help']

@client.event
async def on_ready():
    serverCount = len(client.servers)
    await client.change_presence(game=discord.Game(name='{} servers | q.help'.format(serverCount), type = 2, status=discord.Status.dnd))
    print('Bot online.')

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded. [{}]'.format(extension, error))

if __name__ == '__main__':
    for extension in extenstions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded. [{}]'.format(extension, error))

client.run(TOKEN)