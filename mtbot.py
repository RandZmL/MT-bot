##########################################################################
####                                                                  ####
####    Берём код и создаём ветку со своим именем или никнеймом       ####
####     Для каждого я подписал модуль, которым он занимается         ####
####        Все вопросы задаём либо в лс, либо не задаём              ####
####                  P.S. Даня, ты клоун                             ####
########                                                          ########
##########################################################################


from cmath import inf
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

db = mc.connect(
    host = "mysql3.joinserver.xyz",
    user = "u77034_L1ZfOAh3wl",
    passwd = "hETSKgyQjb=aYMwmHst+=L0q",
    database = "s77034_BadWars"
)

@bot.event

async def on_ready():
	print('Бот запущен')

	await bot.change_presence(status = discord.Status.online, activity = discord.Game('Напиши /help'))


@bot.command()                               #Царан (Команда help должна показать пользователю, какие команды он может использовать)

async def helpme(ctx):
	emb = discord.Embed(title = 'Команды бота', colour = discord.Color.green())
	emb.set_author(name = 'Даун', icon_url = 'https://cdn.discordapp.com/attachments/571193028190928903/972322466405953536/-----687128.gif')
	emb.add_field(name = '.helpme', value = 'Команда для вызова этого сообщения', inline = False)
	emb.add_field(name = '.stats [Ник игрока]', value = 'Показывает статистику введёного игрока', inline = False)
	emb.add_field(name = '.top [Номер места]', value = 'Показывает топ игроков, начиная с указанного места (Например: .top15 покажет вам 10 лучших игроков, начиная с 15-го места ', inline = False)
	emb.add_field(name = '.reg [Ник игрока в майнкрафте]', value = 'Связывает ваш аккаунт дискорда с вашим аккаунтом в майнкрафте', inline = False)
	emb.add_field(name = '.rereg [Старый ник игрока в майнкрафте] [Новый ник игрока в майнкрафте]', value = 'Связывает ваш аккаунт дискорда с вашим новым аккаунтом в майкнрафте', inline = False)
	emb.add_field(name = '.shop', value = 'Показывает самые интересные товары в магазине', inline = False)
	emb.add_field(name = '.bp', value = 'Показывает информацию о вашем боевом пропуске', inline = False)
	await ctx.send(embed = emb)


@bot.command()                               #--

async def top(ctx, bw : str, diopozon = 10):
	await ctx.send()



@bot.command()                               #--
 
async def stats(ctx, player_name : discord.Member):
	user_id = '\\' + str(player_name.mention)
	user_discord_name = str(player_name).replace('@', '')[:-5]
	cursor = db.cursor()
	information = []
	uuid = []
	emb = discord.Embed(title = '', description = '', colour = discord.Color.blue())
	kd = float 
	winrate : float

	try:
		cursor.execute("SELECT uuid FROM bw_stats_players WHERE discord_id = '" + user_id + "'")
		for x in cursor:
			uuid += x

		cursor.execute("SELECT * FROM bw_stats_players WHERE uuid = '" + uuid[0] + "'")
		for x in cursor:
			information += x
		cursor.execute("SELECT * FROM bw_rang_texted WHERE uuid = '" + uuid[0] + "'")
		for x in cursor:
			information += x

		information.remove(information[6])
		information.remove(information[10])
		information.remove(information[10])

		if information[6] == 0 or information[6] == 1:
			kd = information[0]
		else:
			kd = information[0]/information[6]
		
		winrate = (information[1]/(information[1] + information[3])) * 100

		emb = discord.Embed(title = 'Информация о пользователе ' + user_discord_name, description = 'Профиль игрока в режиме Bed Wars', colour = discord.Color.blue())
		emb.set_author(name = information[4] + ': ' + information[9], icon_url = player_name.avatar_url)
		emb.set_thumbnail(url = player_name.avatar_url)
		emb.add_field(name = 'Ранг: ' + information[9], value = '*Счёт в сезоне: ' + str(information[2]) + '*')
		emb.add_field(name = 'К/Д: ' + str(kd), value = '*Убийств: ' + str(information[0]) + '*\n*Смертей: ' + str(information[6]) + '*')
		# if information[2] > 10000:                                                                                                                       Алгаритм на будущее. Скорее всего, возьму за основу
		# 	emb.add_field(name = 'Текущее место среди лиги лучших: ' + information[x], value = '*Разрыв: ' + information[x] + ' очков*')                   алгоритм из команды выше.
		emb.add_field(name = 'Винрейт: ' + str(winrate) + '%', value = '*Побед: ' + str(information[1]) + '*')
		await ctx.send(embed = emb)
	except Exception as e:
		print('Ошибка при использовании команды .stats: ' + str(e) + '\ninfo: ' + str(information) + '\nuuid: ' + str(uuid))
		await ctx.send('**Ошибка:** пользователь не найден. Возможно, ты допустил ошибку в никнейме, или же такого игрока нет на сервере.')
    

@bot.command()                               #Влад (команда должна синхронизировать пользователя в discord'е с его аккаунтом в minecraft'e (по факту, нужно добавить профиль дс-а в бд
                                             #     с последующей верефикацией))
async def reg(ctx, nickname : str):
	await ctx.send()


@bot.command()                               #Влад (изменение привязанного никнейма к профилю discord'а)

async def rereg(ctx, old_nickname : str, new_nickname : str):
	await ctx.send()


@bot.command()                               #Даня (выводить лучшие предложения из магазина и давать ссылку на него)

async def shop(ctx):
	await ctx.send()


@bot.command()                               #Даня

async def bp(ctx):
	await ctx.send()



########################################
####     Команды администратора     ####
########################################
@bot.command()
@commands.has_permissions(administrator = True)

async def ban(ctx):
	await ctx.send()


@bot.command()
@commands.has_permissions(administrator = True)

async def mute(ctx):
	await ctx.send()


@bot.command()
@commands.has_permissions(administrator = True)

async def tempban(ctx):
	await ctx.send()


@bot.command()
@commands.has_permissions(administrator = True)

async def voiceban(ctx):
	await ctx.send()

with open('token.txt', 'r') as f:
    token = f.readline()
bot.run(token)