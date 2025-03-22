import os
import random
import discord
from dotenv import load_dotenv

from response import load_response

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()

client = discord.Client(intents=intents)


def load_responses():
    responses = []
    for file in os.listdir('responses'):
        if file.endswith('.json'):
            responses.append(load_response(f'responses/{file}'))
    return responses


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    client.responses = load_responses()
    print(f'Loaded {len(client.responses)} responses')


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content == "!reload" and message.author.id == 854819626969333771:
        client.responses = []
        for file in os.listdir('responses'):
            if file.endswith('.json'):
                client.responses.append(load_response(f'responses/{file}'))
        await message.reply(f'Loaded {len(client.responses)} responses')
        return

    potential_responses = []
    for response in client.responses:
        output = response.getOutput(message.content)
        if output:
            potential_responses.append(output)

    if potential_responses:
        await message.reply(random.choice(potential_responses))

client.run(TOKEN)
