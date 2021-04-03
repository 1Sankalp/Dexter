import asyncpraw  
import discord
import os
from dotenv import load_dotenv
import time
from datetime import date
import random
import datetime
import wikipedia
#from pygame import mixer
#client_id = m1Xu8ChRC5X5kg
#secret = mjMj7Q-Oglx0GwWsV7BdINuc8tSHhw

bot = discord.Client()

reddit_client = asyncpraw.Reddit(
    client_id="m1Xu8ChRC5X5kg",
    client_secret="mjMj7Q-Oglx0GwWsV7BdINuc8tSHhw",
    user_agent="bot:dexter (by /u/1Sankalp)",
)


greet = ['Hello, Sir',"It's a pleasure to meet you, Sir","Hello Sir, It's a pleasure to meet you."]
ask = ['sup dex','Sup Dex','Sup Dexter','sup dexter','hey dex','Hey Dex','hey dexter','Hey Dexter','hi dex','Hi Dex','hi dexter','Hi Dexter','hey d','Hey D']
video = ['open youtube','Open Youtube', 'open yt','Open YT']
google = ['open google','Open Google','open g','Open G']


@bot.event
async def on_message(message):

	if message.content == 'hello':
		await message.channel.send(random.choice(greet))

	elif message.content == "hello dexter":
		await message.channel.send('Hello Sir', tts=True)

	elif message.content == "illusion":
		await message.channel.send("Hello, Illusion", tts=True)

	elif message.content == 'time':
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		await (message.channel.send(current_time, tts=True))

	elif message.content == 'date':
		today = date.today()
		now = today.strftime('%B %d %Y')
		await message.channel.send(now)

	elif message.content in ask:
			hour = int(datetime.datetime.now().hour)
			if hour >= 0 and hour < 12:
				await message.channel.send("Good Morning Sir !", tts= True)

			elif hour >= 12 and hour < 18:
				await message.channel.send("Good Afternoon Sir !", tts=True)

			else:
				await message.channel.send("Good Evening Sir !", tts=True)

	#elif message.content in video:
		#await message.channel.send(webbrowser.open('www.youtube.com'))

	#elif message.content in google:
		#await message.channel.send(webbrowser.open('www.google.com'))

	elif message.content == 'news':
		import requests

		async def NewsFromBBC():
			query_params = {
				"source": "bbc-news",
				"sortBy": "top",
				"apiKey": "bcca9a1be42a4b8b85dd6501d9359a54"
			}
			main_url = " https://newsapi.org/v1/articles"

			# fetching data in json format
			res = requests.get(main_url, params=query_params)
			open_bbc_page = res.json()

			# getting all articles in a string article
			article = open_bbc_page["articles"]

			# empty list which will
			# contain all trending news
			results = []

			for ar in article:
				results.append(ar["title"])

			for i in range(len(results)):
				# printing all trending news
				await message.channel.send((i + 1, results[i]))


		# Driver Code
		if __name__ == '__main__':
			# function call
			await NewsFromBBC()

	elif message.content.split()[0] == 'reddit':
		reply = ''
		args = message.content.split()
		args.remove(args[0])
		if len(args) != 0 :
			subreddit = await reddit_client.subreddit(args[0])
			submission = ([post async for post in subreddit.hot(limit=30)])[random.randint(0, 30)]
			txt = ''
			obj = ''
			url = ''
			if len(submission.selftext) != 0:
				txt = submission.selftext
			if len(submission.url) != 0:
				obj = (str(submission.url))
			if submission.url != ("https://www.reddit.com" + submission.permalink):
				url = ("https://www.reddit.com" + submission.permalink)
			reply = f"<@!{message.author.id}>\n{submission.title}\n{txt}\n{obj}\n{url}"
		if len(reply) != 0:
			await  message.channel.send(reply)

	elif message.content == "help":
		embed = discord.Embed(title="Help on BOT", description="Some useful commands")
		embed.add_field(name="hello", value="Greets the user")
		embed.add_field(name="news", value="Gives Times of India Headlines")
		embed.add_field(name="time", value="Gives the curent Time")
		embed.add_field(name="date", value="Gives the current Date")
		await message.channel.send(content=None, embed=embed)



load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(DISCORD_TOKEN)