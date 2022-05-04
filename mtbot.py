##########################################################################
####                                                                  ####
####    Берём код и создаём ветку со своим именем или никнеймом       ####
####     Для каждого я подписал модуль, которым он занимается         ####
####        Все вопросы задаём либо в лс, либо не задаём              ####
####                  P.S. Даня, ты клоун                             ####
########                                                          ########
##########################################################################


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

	await bot.change_presence(status = discord.Status.online, activity = discord.Game('Напиши /help'))


@bot.command                               #Царан (Команда help должна показать пользователю, какие команды он может использовать)

async def help(ctx):
	await ctx.send()


@bot.command                               #--

async def top(ctx, bw : str, diopozon = 10):
	await ctx.send()


@bot.command                               #Даня (команда должна выдать статистику игрока, который был указан, либо же игрока, который отправил эту команду)
 
async def stats(ctx, player_name : discord.Member):
	await ctx.send()


@bot.command                               #Влад (команда должна синхронизировать пользователя в discord'е с его аккаунтом в minecraft'e (по факту, нужно добавить профиль дс-а в бд
                                           #      с последующей верефикацией))
async def reg(ctx, nickname : str):
	await ctx.send()


@bot.command                               #Влад (изменение привязанного никнейма к профилю discord'а)

async def rereg(ctx, old_nickname : str, new_nickname : str):
	await ctx.send()


@bot.command                               #Даня (выводить лучшие предложения из магазина и давать ссылку на него)

async def shop(ctx):
	await ctx.send()


@bot.command                               #--

async def bp(ctx):
	await ctx.send()



########################################
####     Команды администратора     ####
########################################
@bot.command
@commands.has_permissions(administrator = True)

async def ban(ctx):
	await ctx.send()


@bot.command
@commands.has_permissions(administrator = True)

async def mute(ctx):
	await ctx.send()


@bot.command
@commands.has_permissions(administrator = True)

async def tempban(ctx):
	await ctx.send()


@bot.command
@commands.has_permissions(administrator = True)

async def voiceban(ctx):
	await ctx.send()

with open('token.txt', 'r') as f:
    token = f.readline()
bot.run(token)