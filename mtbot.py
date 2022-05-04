import discord
import time
import datetime
from discord_buttons_plugin import *
from discord import utils
from discord.ext import commands
from discord import Activity, ActivityType
import mysql.connector as mc
from discord_slash import SlashCommand, SlashContext


bot = commands.Bot(command_prefix = '.')
buttons = ButtonsClient(bot)
slash = SlashCommand(bot, sync_commands = True)

@bot.event

async def on_ready():
	print('Бот запущен')

	await bot.change_presence(status = discord.Status.online, activity = discord.Game('Напиши '))



with open('token.txt', 'r') as f:
    token = f.readline()
bot.run(token)