import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.content.startswith('$spam'):
        while True:
            await message.channel.send('Message to spam')
            await asyncio.sleep(1)

client.run('your_token_here')
