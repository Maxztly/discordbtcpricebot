import discord
from discord import Intents
import requests
import math
import asyncio

CRYPTOCOMPARE_API_KEY = 'YOUR API KEY'

intents = Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

async def get_btc_price():
    url = f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key={CRYPTOCOMPARE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    price = data['USD']

    rounded_price = math.ceil(price)

    return f'BTC: ${rounded_price} USD'

async def update_price():
    await client.wait_until_ready()

    while not client.is_closed():
        btc_price = await get_btc_price()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=btc_price))
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print('Bot is ready')
    client.loop.create_task(update_price())

bot_token = 'YOUR TOKEN'
if bot_token:
    client.run(bot_token)
else:
    print("Discord bot token not found.")
