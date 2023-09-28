#!/usr/bin/env python3
import discord
from discord.ext import commands
import asyncio

class bump(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        if message.author == 302050872383242240:
            for embed in message.embeds:
                if "Bump done!" in embed.description:
                    embed = discord.Embed(
                        title="Thank you for bumping the server!",
                        description="I'll ping <@836263721281650718> when the server can be bumped again."
                    )
                    await channel.send(embed=embed)
                    # waits 2 hours and sends a followup
                    await asyncio.sleep(7200)
                    content = '<@836263721281650718>'
                    embed = discord.Embed(
                        title='It\'s time to bump!',
                        description='Bump the server by running </bump:947088344167366698>'
                    )
                    await channel.send(content=content, embed=embed)
def setup(bot): 
    bot.add_cog(bump(bot))