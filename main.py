import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

everyone_triggers = ["everyone", "everybody",
                     "every person", "every one", "every body"]


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if any(trigger in message.content.lower() for trigger in everyone_triggers) and "@everyone" not in message.content.lower():
        await message.reply("hey there it looks like you forgot to actually ping everyone, let me help you with that :3\n@everyone")

client.run(TOKEN)
