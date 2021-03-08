import discord
import os
client = discord.Client()
print('Connecting...')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='the prefix [fh]'))
    print("{0.user} is up and running.".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('fh'):
        await message.channel.send(
            "I'm online and working as usual!")
client.run('NzgyMjA5NjA3Mjc5NTc1MDcw.X8I3dw.xz9wC-s3v9N6tuhnTBWhRYsb_ds')
