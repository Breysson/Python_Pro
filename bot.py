#bot.py =

import discord
from bot_logic import gen_pass, gen_emo, gen_dato_cur

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hola'):
        await message.channel.send("¡Hola!")
    elif message.content.startswith('$adios'):
        await message.channel.send("Adiós 👋")
    elif message.content.startswith('$contraseña'):
        await message.channel.send(f"Tu contraseña: {gen_pass(10)}`")
    elif message.content.startswith('$emoji'):
        await message.channel.send(f"Emoji: {gen_emo()}")
    elif message.content.startswith('$dato curioso'):
        await message.channel.send(f"¿Lo sabias? {gen_dato_cur()}") 
    elif message.content.startswith('help!'):
        await message.channel.send(f"Comandos del Bot : $hola(hace que el bot te salude), $adios(hace que el bot se despida), $contraseña(hace que el bot geere una contraseña de 10 digitos), $emoji(hace que el bot genere un emoji de animales al azar), $dato curioso(hace que el bot genere un dato curioso)") 
    

client.run("MTM4OTYzODY4MDc1NDM4OTA4NQ.Gw1gDR.TMeRRyEL8wTNljWOQZYV6rAFWVJcTXco2aUynQ")

#bot_logic.py = el signo de pregunta es un emoji que en discord se muestra como pulmon

import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emo():
    emojis_animales = (
        "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨",
        "🐯", "🦁", "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🐦",
        "🐤", "🦆", "🦉", "🦇", "🐴", "🦄", "🐝", "🐛", "🦋",
        "🐌", "🐞", "🦖", "🦕", "🐙", "🦀", "🐠", "🐬", "🐳",
        "🦈", "🐊", "🐘", "🦒", "🦘", "🐐", "🐑", "🐕", "🐓",
        "🦜", "🐇", "🐿", "🦔"
    )
    return random.choice(emojis_animales)
         

def gen_dato_cur():

    datos_curiosos = (
        "En un minuto, un adulto en reposo inhala y exhala unos 6 litros de aire :cloud: ",
        "El pulmón 🫁 derecho es ligeramente más grande que el izquierdo",
        "Los pelos de la nariz 👃 ayudan a calentar 🌡️ y limpiar el aire que respiramos",
        "Los estornudos 🤧 pueden alcanzar una velocidad de hasta 165 km/h",
        " Los humanos 👱 perdemos alrededor de medio litro de agua 💧 al día a través de la respiración"
    )
    return random.choice(datos_curiosos)
