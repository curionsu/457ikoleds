import discord



# create discord client

client = discord.Client()



# token from https://discordapp.com/developers

token = 'NjMxODc3ODk3NTY0NTg1OTk0.XZ_cFQ.EFXqXS9dVwleIPEhiGx6IsI40NY'



# bot is ready

@client.event

async def on_ready():

	try:

		# print bot information

		print(client.user.name)

		print(client.user.id)

		print('Discord.py Version: {}'.format(discord.__version__))

	

	except Exception as e:

		print(e)



# on new message

@client.event

async def on_message(message):

	# print message content

	await message.content



# start bot

client.run(token)