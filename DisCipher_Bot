import discord
from discord import app_commands
import morsecode
import caesarcode

token = 'xxxxxxxxxxxxxxxxxxx'
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1109016227210350634))
    print("DisCipher up")

@tree.command(name = "morse-encode", description = "encodes from english to morse", guild=discord.Object(id=1109016227210350634))
async def encoding(interaction: discord.Interaction, input: str) -> None:
    await interaction.response.send_message(morsecode.encode(input))

@tree.command(name = "morse-decode", description = "decodes from morse  to english", guild=discord.Object(id=1109016227210350634))
async def decoding(interaction: discord.Interaction, input: str) -> None:
    await interaction.response.send_message(morsecode.decode(input))

@tree.command(name = "caesar-encode", description = "encodes from english to caesar cipher", guild=discord.Object(id=1109016227210350634))
async def encoding(interaction: discord.Interaction, shifting: int, *, input: str) -> None:
    await interaction.response.send_message(caesarcode.encode(shifting, input))

@tree.command(name = "caesar-decode", description = "decodes from caeser cipher to english", guild=discord.Object(id=1109016227210350634))
async def encoding(interaction: discord.Interaction, shifting: int, *, input: str) -> None:
    await interaction.response.send_message(caesarcode.decode(shifting, input))

@tree.command(name = "rot13-encode", description = "encodes from english to ROT13", guild=discord.Object(id=1109016227210350634))
async def encoding(interaction: discord.Interaction, input: str) -> None:
    await interaction.response.send_message(caesarcode.rot3encode(input))

@tree.command(name = "rot13-decode", description = "decodes from ROT13 to english", guild=discord.Object(id=1109016227210350634))
async def encoding(interaction: discord.Interaction, input: str) -> None:
    await interaction.response.send_message(caesarcode.rot3decode(input))

client.run(token)
