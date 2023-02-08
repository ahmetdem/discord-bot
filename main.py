import discord 
from discord.ext import commands
from decouple import config
from dotenv import load_dotenv
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())

load_dotenv(r'C:\Users\ahmet\Documents\GitHub\python-projects\discord bot\main.env')
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
    

bot.run(DISCORD_TOKEN)