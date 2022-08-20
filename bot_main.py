import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv('.env.txt')

intent = discord.Intents.all()
client = commands.Bot(command_prefix='s-', intents=intent)

token = open("my_token.txt").read()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command(name="test")
async def test(context):
    respone = "```" \
              "Hello world" \
              "```"
    await context.send(respone)


client.run(token)
