import asyncpraw  
import discord
import os
from dotenv import load_dotenv
import time
from datetime import date
import random
import datetime
import wikipedia

bot = discord.Client()

reddit_client = asyncpraw.Reddit(
    client_id="m1Xu8ChRC5X5kg",
    client_secret="mjMj7Q-Oglx0GwWsV7BdINuc8tSHhw",
    user_agent="bot:dexter (by /u/1Sankalp)",
)


greet = ['Hello, Sir',"It's a pleasure to meet you, Sir","Hello Sir, It's a pleasure to meet you."]
ask = ['sup dex','Sup Dex','Sup Dexter','sup dexter','hey dex','Hey Dex','hey dexter','Hey Dexter','hi dex','Hi Dex','hi dexter','Hi Dexter','hey d','Hey D']
city = ['agartala','agra','ahemdabad','ajmer','allahabad','ambala','amritsar','hoshangabad','bhopal','chennai','jammu','kashmir','bangaluru','chandigarh','coorg','dehradun','goa','gwalior','hydrabad','jabalpur','kanpur','kolkata','lucknow','mumbai','mysore','nagpur','navi mumbai','new delhi','delhi','ooty','pune','raipur','rajhasthan','rajkot','rishikesh','indore','shimla','tirupur','udaipur','ujjain']

def wiki_summary(arg):
    definition = wikipedia.summary(arg, sentences=3, chars=100, auto_suggest=True, redirect=True)
    return definition

@bot.event
async def on_message(message):

    if message.content == 'hello':
        await message.channel.send(random.choice(greet))

    elif message.content == "hello dexter":
        await message.channel.send('Hello Sir', tts=True)

    elif message.content == "illusion":
        await message.channel.send("Hello, Illusion", tts=True)

    elif message.content == 'time':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        await message.channel.send(current_time)

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
            await message.channel.send(reply)

    elif message.content == "help":
        embed = discord.Embed(title="Help on BOT", description="Some useful commands")
        embed.add_field(name="hello", value="Greets the user")
        embed.add_field(name="news", value="Gives Times of India Headlines")
        embed.add_field(name="time", value="Gives the curent Time")
        embed.add_field(name="date", value="Gives the current Date")
        await message.channel.send(content=None, embed=embed)

    elif message.content in city:
        import requests, json
        # base URL
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # City Name CITY = "Hyderabad"
        # API key API_KEY = "Your API Key"
        # upadting the URL
        URL = BASE_URL + "q=" + message.content + "&appid=" + '11ae50ac9474c2111ed60e7622a5b6e9'

        # HTTP request
        response = requests.get(URL)

        # checking the status code of the request


        if response.status_code == 200:
            # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = main['temp'] - 273.15

            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            # weather report
            report = data['weather']
            await message.channel.send(f"{message.content:-^30}")
            await message.channel.send(f'Temperature: {temperature}')
            await message.channel.send(f"Humidity: {humidity}")
            await message.channel.send(f"Weather Report: {report[0]['description']}")
        else:
            await message.channel.send("Error in the HTTP request")


    elif message.content == 'countdown':
        while True:
            await message.channel.send('Initiating Countdown')
            time.sleep(1)
            await message.channel.send('10')
            time.sleep(1)
            await message.channel.send('9')
            time.sleep(1)
            await message.channel.send('8')
            time.sleep(1)
            await message.channel.send('7')
            time.sleep(1)
            await message.channel.send('6')
            time.sleep(1)
            await message.channel.send('5')
            time.sleep(1)
            await message.channel.send('4')
            time.sleep(1)
            await message.channel.send('3')
            time.sleep(1)
            await message.channel.send('2')
            time.sleep(1)
            await message.channel.send('1')
            time.sleep(1)
            await message.channel.send('TIME UP!!!')
            break

    elif message.content == 'delete':
        deleted = await message.channel.purge(limit=11)
        await message.channel.send('All messages deleted.'.format(deleted))

    words = message.content.split()
    if words[0].lower() == "define":
        important_words = words[1:]
    await message.channel.send(wiki_summary(important_words))



load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(DISCORD_TOKEN)
