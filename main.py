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

    if "@everyone" in message.content.lower():
        await message.reply("don't do that agian >:(")

    if "good bot" in message.content.lower():
        await message.reply(":3")

    if "bad bot" in message.content.lower():
        await message.reply("3:")

    if "pixel" in message.content.lower():
        await message.reply("-# *Did you mean: **fluffy**?*")

client.run(TOKEN)
