import os
import discord.ext

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.commands.CommandTree(client)
TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=292068243579994113))
    print("Ready!")
    
@tree.command(name = "sup", description = "My first application Command", guild=discord.Object(id=292068243579994113)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def slashing_commanding(int: discord.Interaction):    
    await int.response.send_message("sup dude")
    
client.run(TOKEN)
