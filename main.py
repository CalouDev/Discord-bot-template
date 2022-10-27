# ---IMPORT LIBRAIRIES---

# Discord
import discord 
from discord.utils import get
from discord.ext import commands

# Web Scraping
import requests
from bs4 import BeautifulSoup

#---------------------------------------------------BOT-------------------------------------------------------------------------------

# set the bot
bot = commands.Bot(command_prefix='/', description="Template Bot")

# To know where the bot is launched
@bot.event
async def on_ready():
    print("Bot ready !")

# Make the "definition" command
@bot.command()
async def definition(ctx, mot):
    url = "https://www.le-dictionnaire.com/definition/{}".format(mot) 
    reponse = requests.get(url)
    if reponse.ok:
        s = BeautifulSoup(reponse.text, 'html.parser')
        trouve = s.find('ul').get_text() # Search for text inside 'ul' tags
        await ctx.send("``` {} ```".format(trouve)) # Send on the server the definition

#---------------------------------------------------RUN-----------------------------------------------------------------------------------

print("Launching the bot..")

bot.run("Token") # Replace here the token of the bot (str)
