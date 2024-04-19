from discord import app_commands
import discord
from datetime import datetime
import discord , time
from threading import Thread

class Client(discord.Client):
    async def on_ready(self):
        print(f"Loged In As : {self.user} At {datetime.now()}")
    async def on_message(self, message):
        print(f"{message.author} : {message.content}")

intents = discord.Intents.default()
client = Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Commands Synced At : {datetime.now()}")

@tree.command(description="Display Avatar Of A Memer",)
async def avatar(ctx, user: discord.Member):
    Url = user.display_avatar

    avatar_embed = discord.Embed(color=user.color, title=user.name)
    avatar_embed.set_footer(text=f'{datetime.now()}')
    avatar_embed.set_image(url=Url)
    await ctx.response.send_message(embed=avatar_embed, delete_after=35)

@tree.command(description="Display Member Informations")
async def profile(ctx, user: discord.Member):

    profile_embed = discord.Embed(color=discord.Color(0xaef50a))
    profile_embed.set_author(icon_url=user.display_avatar, name=user.name)
    profile_embed.add_field(name='`ID:`', value=f"```{user.id}```", inline=True)
    profile_embed.add_field(name='`Created At:`',value=f"```{user.created_at}```", inline=True)
    profile_embed.add_field(name='`Joined Server At:`',value=f"```{user.joined_at}```", inline=True)
    profile_embed.add_field(name='`Color:`', value=f"```{user.colour}```", inline=True)
    profile_embed.add_field(name='`Activity:`', value=f"```{user.activity}```")
    profile_embed.add_field(name='`Bot ?:`', value=f"```{user.bot}```")
    profile_embed.set_thumbnail(url=user.display_avatar)
    await ctx.response.send_message(embed=profile_embed)

@tree.command(description="Clear An Amount Of Messages In A Channel",)
async def clear(ctx, amount: int):
    clear_embed = discord.Embed(color=discord.Color(0xaef50a))
    clear_embed.add_field(name='🚮 `Clear:`', value=f'```You Are Trying To Clear {amount} Messages```')
    clear_embed.add_field(name='⚠ `Info:`', value='```The Messages Will Auto Delete After 5s```')
    clear_embed.set_image(url='https://media.giphy.com/media/gIYpF7LzpfBHIAo0fv/giphy.gif')
    await ctx.response.send_message(embed=clear_embed)
    await ctx.channel.purge(limit=amount)

@tree.command(description="Ban A User From The Server")
async def ban(ctx: discord.Interaction, user: discord.Member, reason: str):
    ban_embed = discord.Embed(color=discord.Color(0xaef50a))
    ban_embed.add_field(name='⚡ `Ban :`', value=f"```css\n[You Banned {user.name} From This Server , Enjoy Your Power Master]\n```", inline=False)
    ban_embed.add_field(name='💀 `Reason :`', value=f'```\nReason : {reason}\n```', inline=False)
    ban_embed.set_image(url='https://media.tenor.com/67LIumILNRsAAAAd/ltg-low-tier-god.gif')
    await ctx.user.ban(reason=reason)
    await ctx.response.send_message(embed=ban_embed)

@tree.command(description="Ban A User From The Server")
async def task(ctx:discord.Interaction):
    await ctx.response.send_message("Hello World")



@client.event
async def on_ready():
    await tree.sync(guild=1120025228232359976)
    print(f"Commands Synced At : {datetime.now()}")


client.run("")