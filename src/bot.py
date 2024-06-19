import os
import discord

class Myweomp(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = Myweomp(intents=intents)

token = os.getenv('MEAL_TOKEN')
client.run(token)