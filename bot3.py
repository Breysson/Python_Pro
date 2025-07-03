import discord
import requests

UNSPLASH_ACCESS_KEY = "x"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def buscar_imagen_unsplash(query):
    url = "https://api.unsplash.com/photos/random"
    params = {
        "query": query,
        "client_id": UNSPLASH_ACCESS_KEY,
        "orientation": "landscape"
    }
    respuesta = requests.get(url, params=params)

    if respuesta.status_code != 200:
        print(f"Error API Unsplash: {respuesta.status_code} - {respuesta.text}")
        raise Exception("Error al obtener imagen de Unsplash")

    data = respuesta.json()
    if "urls" in data and "regular" in data["urls"]:
        return data["urls"]["regular"]
    else:
        print(f"Respuesta inesperada de Unsplash: {data}")
        raise Exception("No se encontró la url de la imagen")

@client.event
async def on_ready():
    print(f"Hemos iniciado sesión como {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hola"):
        await message.channel.send("¡Hola! para conocer mas comandos escriba **help!**")

    if message.content.startswith("help!"):
        await message.channel.send("Este bot es un generador de imagenes de animales(pero puede generar otras) para generar una imagen se escribe el comando **$animal x**  (x = animal de su preferencia) si al genera la imagen no genera un animal pruebe con **$animal animal x**(x = aimal de su preferencia) ")

    elif message.content.startswith("$animal"):
        animal = message.content.replace("$animal", "").strip()
        if not animal:
            await message.channel.send("❗ Escribe el nombre de un animal. Ejemplo: `$animal gato`")
            return
        try:
            imagen = buscar_imagen_unsplash(animal)
            await message.channel.send(imagen)
        except Exception as e:
            print(f"Error en on_message: {e}")
            await message.channel.send("❌ No se pudo obtener la imagen.")




client.run("x")
