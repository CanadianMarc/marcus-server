import os
import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
TOKEN = os.getenv("DISCORD_TOKEN")

@tree.command(name = "sup", description = "My first application Command", guild=discord.Object(id=292068243579994113)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Nice!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=292068243579994113))
    print("Ready!")
    
client.run(TOKEN)
