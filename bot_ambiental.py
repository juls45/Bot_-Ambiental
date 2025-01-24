import discord
from discord.ext import commands
import random

description = "Un bot ecológico para ayudarte a entender y reducir la contaminación."

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)
# con un punto el bot imprime instrucciones
@bot.command(name='instrucciones')
async def instrucciones(ctx):
    "instrucciones para usar el bot"
    await ctx.send("Tienes que generar una conversacion con tu bot mediante palabas como: hola, instrucciones, contaminacion, consejo, reciclaje")

#comando para saludar
@bot.command(name='hola')
async def hola(ctx):
    "hola:)"
    await ctx.send("Hola, el diá de hoy vamos a tratar un tema super importante, LA CONTAMINACIÓN")

# Comando para explicar qué es la contaminación
@bot.command(name='contaminacion')
async def contaminacion(ctx):
    "Explica qué es la contaminación."
    await ctx.send("La contaminación es la presencia de sustancias o elementos dañinos en el medio ambiente, como el aire, el agua o el suelo. Estos contaminantes pueden afectar la salud de las personas, los animales y las plantas, causando problemas a largo plazo para el planeta.")

# Comando para dar consejos para reducir la contaminación
@bot.command(name='consejo')
async def consejos(ctx):
    "Ofrece consejos para reducir la contaminación."
    consejos_lista = [
        "1. Usa menos plástico: Lleva bolsas reutilizables cuando hagas compras.",
        "2. Ahorra energía: Apaga las luces y los aparatos electrónicos cuando no los uses.",
        "3. Usa el transporte público, bicicleta o camina siempre que sea posible.",
        "4. Recicla y separa correctamente los residuos.",
        "5. Planta árboles o cuida las áreas verdes cerca de tu casa.",
        "6. Evita quemar basura y otros materiales tóxicos."
    ]
    await ctx.send("\n".join(consejos_lista))

#comando para reciclaje
@bot.command(name='reciclaje')
async def reciclaje(ctx):
    "Reciclaje una manera de aliviarle el dolor al planeta"
    await ctx.send("El reciclaje transforma materiales desechados en nuevos productos, reduciendo residuos y conservando recursos. Es clave para cuidar el planeta y minimizar la contaminación.")

#@bot.command(name='imagen')
#async def img(ctx):
 #   with open(f'imagenes/{random.randint(1,4)}.jpg', 'rb') as f:
  #      # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
   #     picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    #await ctx.send(file=picture)
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user} (ID: {bot.user.id})')
    print('-----------')

# Inicia el bot
bot.run('MTMyOTk3NDU0ODIxMjQ4NjE0NA.G-xK1m.tB2iN73k7mp2mu05K4z06ayx4_IKbR8raeIMCU')

