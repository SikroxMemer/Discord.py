from discord import app_commands
from datetime import datetime
from tabulate import tabulate
import asyncio , discord

class Main_Client(discord.Client):
    async def on_ready(self):
        print(f"Loged In As : {self.user} At {datetime.now()}")

    async def on_message(self, message):
        print(f"{message.author} : {message.content}")
    pass
pass

Intents = discord.Intents.default()
Main_Client = Main_Client(intents=Intents)
Tree = app_commands.CommandTree(Main_Client)

@Main_Client.event
async def on_ready():
    await Tree.sync()
    print(f"Commands Synced At : {datetime.now()}")

Table = [['Sikrox Memer' , 'Enjoy :)'],['Client Loaded',f'At: {datetime.now()}']]

print(tabulate(Table ,headers='firstrow', tablefmt="grid"))