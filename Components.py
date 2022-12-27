from Client import Main_Client
from Client import discord
from Client import datetime
from Client import asyncio
from Client import Tree

@Tree.command(description="Display Avatar Of A Memer",)
async def avatar(ctx, user: discord.Member):
    Url = user.display_avatar
    avatar_embed = discord.Embed(
        color=user.color, title=user.name)
    avatar_embed.add_field(
        name='`Avatar Description :`',
        value=f'URL : <{Url}>',
        inline=False
    )
    avatar_embed.add_field(
        name='`Avatar Image :`',
        value="```md\n# It's Us Find Power Live Life Mind Power...\n```",
        inline=False
    )
    avatar_embed.set_footer(
        text=f'{datetime.now()}'
    )
    avatar_embed.set_image(
        url=Url
    )
    await ctx.response.send_message(embed=avatar_embed, delete_after=35)

@Tree.command(description="Display Member Informations")
async def profile(ctx, user: discord.Member):
    profile_embed = discord.Embed(color=discord.Color(0xaef50a))
    profile_embed.set_author(icon_url=user.display_avatar, name=user.name)
    profile_embed.add_field(
        name='`ID:`', value=f"```{user.id}```", inline=True)
    profile_embed.add_field(name='`Created At:`',
                            value=f"```{user.created_at}```", inline=True)
    profile_embed.add_field(name='`Joined Server At:`',
                            value=f"```{user.joined_at}```", inline=True)
    profile_embed.add_field(
        name='`Color:`', value=f"```{user.colour}```", inline=True)
    profile_embed.add_field(name='`Activity:`', value=f"```{user.activity}```")
    profile_embed.add_field(name='`Bot ?:`', value=f"```{user.bot}```")
    profile_embed.set_thumbnail(url=user.display_avatar)
    await ctx.response.send_message(embed=profile_embed)

@Tree.command(description="Clear An Amount Of Messages In A Channel",)
async def clear(ctx, amount: int):
    clear_embed = discord.Embed(color=discord.Color(0xaef50a))
    clear_embed.add_field(
        name='🚮 `Clear:`', value=f'```You Are Trying To Clear {amount} Messages```')
    clear_embed.add_field(
        name='⚠ `Info:`', value='```The Messages Will Auto Delete After 5s```'
    )
    clear_embed.set_image(
        url='https://media.giphy.com/media/gIYpF7LzpfBHIAo0fv/giphy.gif')
    await ctx.response.send_message(embed=clear_embed)
    await asyncio.sleep(delay=5.7)
    await ctx.channel.purge(limit=amount)

@Tree.command(description="Ban A User From The Server")
async def ban(ctx: discord.Interaction, user: discord.Member, reason: str):
    ban_embed = discord.Embed(color=discord.Color(0xaef50a))
    ban_embed.add_field(
        name='⚡ `Ban :`', value=f"```css\n[You Banned {user.name} From This Server , Enjoy Your Power Master]\n```", inline=False)
    ban_embed.add_field(
        name='💀 `Reason :`', value=f'```\nReason : {reason}\n```', inline=False
    )
    ban_embed.set_image(
        url='https://media.tenor.com/67LIumILNRsAAAAd/ltg-low-tier-god.gif')
    await ctx.user.ban(reason=reason)
    await ctx.response.send_message(embed=ban_embed)

@Main_Client.event
async def on_ready():
    await Tree.sync()
    print(f"Commands Synced At : {datetime.now()}")