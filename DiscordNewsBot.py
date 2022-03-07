import discord
from dotenv import load_dotenv
from discord.ext import commands
import requests
import datetime as dt
from datetime import datetime


load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):

  
  title = message.content


  if title != 0 and title.startswith("news"):
      titleOut = title[4:]


      url = ('https://newsapi.org/v2/top-headlines?')

      caracteristicas = {
          'q': titleOut,
          'from': datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),
          'pagesize': 20,
          'apiKey': '406cae42bf3e4b9898911e5c573ce0ee'
          
            }
      response = requests.get(url, params=caracteristicas)
      response_json = response.json()

      for i in response_json['articles']:
        await message.channel.send(i['title'])



  


client.run('OTUwMTkxNTM5MDcyNjk2MzYw.YiVU1A.nxATatROR18L6SxKKfuEaxAqwfg')
