import discord
import os
from discord.ext import commands


bot = commands.Bot()
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.slash_command(name="first_slash", guild_ids=[292068243579994113]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user.name}({bot.user.id})")

if __name__ == "__main__":
    bot.run(TOKEN)
