import discord
import os
from discord.ext import commands
from discord.ext.commands import when_mentioned_or


def covid_prefix(bot, message):
    if message.content[0:2] == "c.":
        return when_mentioned_or("c.")(bot, message)
    elif message.content[0:2] == "C.":
        return when_mentioned_or("C.")(bot, message)
    return when_mentioned_or("c.")(bot, message)


client = commands.Bot(command_prefix=covid_prefix)
client.remove_command('help')


@client.event
async def on_ready():
    print(f'{client.user} is ready.')
    await client.change_presence(activity=discord.Game(name="Covid-19 | c.help"))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('TOKEN')
