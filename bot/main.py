import discord
import os
from discord.ext import commands


bot = commands.Bot()
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.slash_command(name="runnit")
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command! High Five!")

bot.run(TOKEN)
