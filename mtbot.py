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
	await ctx.send()


@bot.command()                               #--

async def top(ctx, top_range = 1):
	score = []
	nickname = []
	rang = []
	i = 0

	cursor = db.cursor()

	cursor.execute("SELECT score FROM bw_stats_players")
	for x in cursor:
		score += x

	cursor.execute("SELECT name FROM bw_stats_players")
	for x in cursor:
		nickname += x

	cursor.execute("SELECT rang FROM bw_rang_texted")
	for x in cursor:
		rang += x

	list_length = len(score)
	try:
		# Бабл!
		for iInter in range(len(score)):
			swapped = False
			for jInter in range(top_range - 1 - (top_range - 1), len(score) - iInter - 1):
				if score[jInter] > score[jInter + 1]:
					score[jInter], score[jInter + 1] = score[jInter + 1], score[jInter]
					nickname[jInter], nickname[jInter + 1] = nickname[jInter + 1], nickname[jInter]
					rang[jInter], rang[jInter + 1] = rang[jInter + 1], rang[jInter]
					swapped = True
					i += 1
					if swapped == False:
						break
		
		
		score.reverse()
		nickname.reverse()
		rang.reverse()

		if len(score) <= 10:
			if top_range != 1:
				for i in range(top_range - 1):
					score.remove(score[0])
					nickname.remove(nickname[0])
					rang.remove(rang[0])


		i = 0
		emb = discord.Embed(title = 'Топ игроков в Bed War', description = '[С ' + str(top_range) + ' по ' + str(list_length) + ' места]', colour = discord.Color.gold())
		emb.set_author(name = 'Информация от вашего верного слуги!', icon_url = 'https://cdn.discordapp.com/attachments/571193028190928903/972322466405953536/-----687128.gif')
		emb.add_field(name = f'🏆 {nickname[0]} [Топ-{top_range}]', value = f'Ранг: {rang[0]}\nСчёт: {score[0]}', inline = False)

		for i in range(len(score) - 1):
			emb.add_field(name = f'{top_range + i + 1}-e место', value = f'**{nickname[i+1]}**\n*Счёт: {score[i+1]}*', inline = False)

		await ctx.send(embed = emb)
	except Exception as e:
		print(f'Ошибка выполнения запроса пользователя: {e}\nДанные, полученные ботом: \nnickname: {nickname}\nscore: {score}\nrang: {rang}')
		await ctx.send('Увы, но что-то пошло не так при вашем запросе. Возможно, вы неправильно ввели комманду. Пример правильно введёной команды: ``.top bw 3``, где 3 - место, с которого вы хотите вывести топ игроков.')


@bot.command()                               #--
 
async def stats(ctx, player_name : discord.Member):
	user_id = '\\' + str(player_name.mention)
	user_discord_name = str(player_name).replace('@', '')[:-5]
	cursor = db.cursor()
	information = []
	uuid = []
	emb = discord.Embed(title = '', description = '', colour = discord.Color.blue())
	kd : float 
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
		print(f'Ошибка при использовании команды .stats: {e}\ninfo: ' + str(information) + '\nuuid: ' + str(uuid))
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