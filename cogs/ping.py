import discord
import random
import time
from discord.ext import commands


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.thumbnail = 'https://cdn.discordapp.com/avatars/699447274496851979/78e0894a7594e72c84b0ef94594ae0df.png?size=2048'

    
    @commands.command(name="ping")
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def ping(self, ctx):
        # Ping's Bot
        before = time.monotonic()
        message = await ctx.send("Ping!")
        ping = (time.monotonic() - before) * 1000
        embed = discord.Embed(
            title="Ping",
            color=discord.Colour.blue(),
            description=" Pong! My latency is\n**`{0}`** ms".format(int(ping))
        )
        embed.set_thumbnail(url=self.thumbnail)
        embed.set_footer(
            text="Made by Adela Ramadhina",
            icon_url=ctx.guild.me.avatar_url
        )

        await message.edit(content="", embed=embed)


def setup(client):
    client.add_cog(Help(client))
