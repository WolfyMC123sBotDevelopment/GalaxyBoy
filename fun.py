import discord
from discord.ext import commands

class Fun:
	"""Repeats text"""
	
	def __init__(self, client):
		self.client = client
	
	@commands.command(no_pm=True)
	async def mimic(self, *, text):
		"""Copies your words"""
		await self.client.say(text)
		
		
def setup(client):
	n = Fun(client)
	client.add_cog(n(client))