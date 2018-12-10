import discord
from discord.ext import commands

class Help:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author
        
        embed = discord.Embed(
                colour = discord.Colour.blue()
        )
        
        embed.set_author(name='Help Commands')
        embed.add_field(name='Common Commands', value='q.help <Shows this message.> q.invite <a invite link for me.>', inline=True)
        embed.add_field(name='Moderation Commands', value='q.kick <user> q.ban <user> q.purge <number of messages.>', inline=True)
        embed.add_field(name='Fun Commands', value='q.ping <returns pong> 8ball <not ready>', inline=True)
        embed.add_field(name='Extension Based Commands', value='q.load <extension> q.unload <extension>', inline=True)
        
        await self.client.send_message(author, embed=embed)
        await self.client.say('Check your mail box :mailbox_with_mail: ')

    


client.add_cog(Help(client))