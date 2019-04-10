
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
# Jolts token
TOKEN = 'NTY0NjQ4Nzk2NjQyODY5MjQ4.XKrCew.ZoFF0FF_m0wDUMNmB2DZGs_pPuw'
# Possible starts for a comman
BOT_PREFIX = ("!", "?")
# Create instant of discord bot that we call "client" with our preffered prefixes
client = Bot(command_prefix=BOT_PREFIX)

# Create command ball8
@client.command()
async def ball8(ctx, context):
    # tuple of possible responses from Jolt
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    # Jolt sends a randomized choice from the posible responses and ats the user who sent the ball8 request
    await ctx.send(random.choice(possible_responses) + ", " + context.message.author.mention)

# Create command for hello
@client.command()
async def hello(ctx, context):
    # Jolt send a message of hello to the author, and mentions them as well, this will be follwed by a list of other commmands once things like info are ready for use 
    await ctx.send("Hello, " + ctx.mention.author)
# Create command for square
@client.command()
async def square(ctx, number):
    # cast the users response to a INT type and multiples it to itself
    squared_value = int(number) * int(number)
    # Jolt then sends out a message with the orginal number he squared, then its squared value
    await ctx.send(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready(ctx):
    await ctx.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])


async def list_servers(ctx):
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in ctx.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers(client))
client.run(TOKEN)