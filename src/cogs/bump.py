#!/usr/bin/env python3
import discord
from discord.ext import commands
import asyncio
import sqlite3

database = "./data/mpsdb.sqlite3"

class bump(commands.Cog): 

    def __init__(self, bot): 
        self.bot = bot

    bump = discord.SlashCommandGroup("bump-config")

    @bump.command(name="remind-title")
    async def remind_title(self, ctx):
        await ctx.respond('This command I\'snt made yet -Nugget')
    
    @bump.command(name="remind-description")
    async def remind_description(self, ctx):
        await ctx.respond('This command I\'snt made yet -Nugget')

    @bump.command(name="thank-title")
    async def thank_title(self, ctx):
        await ctx.respond('This command I\'snt made yet -Nugget')
    
    @bump.command(name="thank-description")
    async def thank_description(self, ctx):
        await ctx.respond('This command I\'snt made yet -Nugget')
    
    @bump.command(name="embed")
    async def embed(self, ctx):
        await ctx.respond('Command not made yet, but it will let you choose whether the bump messages are an embed or not. -Nugget')
    
    @bump.command(name="role")
    async def role(self, ctx):
        await ctx.respond('Command not made yet, but it will let you set or remove a role to be pinged. -Nugget')



    @commands.Cog.listener()
    async def on_message(self, message):
        #ignores non bots
        if not message.author.bot:
            return
        channel = message.channel
        if message.author.id == 302050872383242240:
            for embed in message.embeds:
                if "Bump done!" in embed.description:
                    with sqlite3.connect(database) as conn:
                        cur = conn.cursor()
                        cur.execute("INSERT OR REPLACE INTO bumpconfig (guild_id) VALUES (?)", (message.guild.id,))
                        cur.execute("SELECT * from bumpconfig WHERE guild_id = ?", (message.guild.id,))
                        rows = cur.fetchall()
                        column_names = [description[0] for description in cur.description]
                        for row in rows:
                            raw_data = dict(zip(column_names, row))
                            is_embed = raw_data[is_embed]
                            thank_title = raw_data[thank_title]
                            thank_description = raw_data[thank_description]
                            remind_description = raw_data[remind_description]
                            remind_title = raw_data[remind_title]
                            ping_role = raw_data[ping_role]
                            role_id = raw_data[role_id]
                    if is_embed == 1:
                        if thank_title:
                            embed = discord.Embed(
                            title=thank_title,
                            description=thank_description
                        )
                        else:
                            embed = discord.Embed(
                            description=thank_description
                        )
                    elif is_embed == 0:
                        if thank_title:
                            content = thank_title + thank_description
                        else:
                            content = thank_description
                    
                    
                    await channel.send(content=content, embed=embed)
                    # waits 2 hours and sends a followup
                    await asyncio.sleep(7200)

                    if is_embed == 0 and ping_role == 0:
                        if remind_title:
                            content = remind_title + "\n" + remind_description
                        else: 
                            content = remind_description
                    elif is_embed == 0 and ping_role == 1:
                        if remind_title:
                            content = f"<@&{role_id}>" + "\n" + remind_title + "\n" + remind_description
                        else: 
                            content = f"<@&{role_id}>" + "\n" + remind_description
                    elif is_embed == 1 and ping_role == 1:
                        if remind_title:
                            embed = discord.Embed(
                                title=remind_title,
                                description=remind_description
                            )
                            content = f"<@&{role_id}>"
                        else:
                            embed = discord.Embed(
                                description=remind_description
                            )
                            content = f"<@&{role_id}>"
                    elif is_embed == 1 and ping_role == 0:
                        if remind_title:
                            embed = discord.Embed(
                                title=remind_title,
                                description=remind_description
                            )
                        else:
                            embed = discord.Embed(
                                description=remind_description
                            )
                    await channel.send(content=content, embed=embed)

def setup(bot): 
    bot.add_cog(bump(bot))