import discord
from discord import Intents
import requests
import math

intents = Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot is ready')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=await get_btc_price()))


async def get_btc_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    data = response.json()
    price = data['bpi']['USD']['rate']

    price_without_comma = price.replace(',', '')
    rounded_price = math.ceil(float(price_without_comma))

    return f'BTC: ${rounded_price} USD'

client.run('YOUR TOKEN')
