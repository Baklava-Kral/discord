import discord
import random

# Botun ayrıcalıklarını tanımlayalım
intents = discord.Intents.default()
intents.message_content = True

# Bot oluşturalım ve ayrıcalıkları aktaralım
client = discord.Client(intents=intents)

# Plastik el işleri fikirleri içeren bir liste oluşturalım
plastik_el_isleri = [
    "pilastik şişeleri yiyebilirsin",
    "plastik pardak ve kaşıklarla robot yapapilirsin",
    "plastik şişeleri bowling gibi ayarlayabilirsin",
    "plastik çatalları sapan gibi kullanabilirsin",
    "plastik tabaktan kalkan yapabilirsin",
    "daha çok yiyebilirsin"
]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!plastik_el_isleri'):
        # Rastgele bir plastik el işi fikri seçelim
        fikir = random.choice(plastik_el_isleri)
        await message.channel.send(f"İşte bir plastik el işi fikri: {fikir}")

# Botu çalıştıralım
client.run("")

