# Property of CabanaCore and Colin Cabana. Do not distribute
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print ("Bot active")
    print ("Version 1.11")
    bot.say("Activated and Online")


#@bot.command(pass_context=True)
#async def command(ctx):

@bot.command(pass_context=True)
async def aboutme(ctx):
    await bot.say("Hi! I'm Top Hat McGee! What a pleasure to meet you!")
    await bot.say("I've been developed by <@194679082196140034> to make hug and kiss commands!")


@bot.command(pass_context=True)
async def developer(ctx):
    await bot.say ("Oh! Is there a problem? Or a suggestion?")
    await bot.say ("You can contact my developer")


@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    await bot.say("Hugssss for {}".format(user.name))



bot.run("token")
