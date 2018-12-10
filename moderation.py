import discord
from discord.ext import commands

class Moderation:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def purge(self, ctx, amount=100):
        channel = ctx.message.channel
        messages = []
        async for message in self.client.logs_from(channel, limit=int(amount) +1):
            message.append(message)
        await self.client.delete_messages(messages)
        await self.client.say('Messages deleted.')

    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.Member = None):
        try:
            if ctx.message.author.server_permissions.kick_members:
                if user is None:
                    embed = discord.Embed(description=":no_entry_sign: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                    await self.client.say(embed=embed)
                    return
                await self.client.kick(user)
                embed = discord.Embed(description=f":white_check_mark:  Sucessfuly kicked **{user}**!", color=(random.randint(0, 0xffffff)))
                await self.client.say(embed=embed)
            else:
                embed = discord.Embed(description=":error: **You are missing KICK_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
                await self.client.say(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
            await self.client.say(embed=embed)    
            
    @commands.command(pass_context=True)
    async def ban(ctx, user: discord.Member = None):
        try:
            if ctx.message.author.server_permissions.ban_members:
                if user is None:
                    embed = discord.Embed(description=":no_entry_sign: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                    await self.client.say(embed=embed)
                    return
                await self.client.ban(user)
                embed = discord.Embed(description=f":check: Sucessfuly banned **{user}**!", color=(random.randint(0, 0xffffff)))
                await self.client.say(embed=embed)
            else:
                embed = discord.Embed(description=":error: **You are missing BAN_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
                await self.client.say(embed=embed)
        except discord.Forbidden:
            embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
            await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True, manage_messages=True)
    async def clear(self, ctx, amount=100):
        """Clear the specified number of messages, default 100 messages."""
        channel = ctx.message.channel
        messages = []
        amount = int(amount) + 1
        async for message in cleintt.logs_from(channel, limit=amount):
            messages.append(message)
        await bot.delete_messages(messages)
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await self.client.send_message(ctx.message.channel, "You do not have permission to use that command.".format(ctx.message.author.mention))  

client.add_cog(Moderation(client))