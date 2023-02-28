import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())

load_dotenv(r'C:\Users\ahmet\Documents\GitHub\discord-bot\main.env')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
	guild_count = 0

	for guild in client.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@client.event
async def on_message(message):
	# channel = message.channel
	if message.content == "kötü":
		await message.delete()

@bot.command()
async def say(ctx, text):
	await ctx.message.delete()
	await ctx.channel.send(text)

@bot.command(pass_context = True)
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)
    
@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar
    await ctx.send(userAvatarUrl)
    
@bot.command()
async def ship(ctx, avamember1 : discord.Member=None,  avamember2 : discord.Member=None):
	rate = random.random() * 100
	await ctx.send(f"Ship rate is: {rate}")

@bot.command()
async def unban(ctx, *, member):

	banned_users = ctx.guild.bans()
	async for ban_entry in banned_users:
		user = ban_entry.user

		if str(user) == member:
			await ctx.guild.unban(user)
			await ctx.channel.send("The user is unbanned")


bot.run(DISCORD_TOKEN)