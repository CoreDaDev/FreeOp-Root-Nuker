import discord
from discord.ext import commands
f = open('members.txt',2 'w')
f.close()
b = open('channels.txt',2 'w')
b.close()
k = open('roles.txt',2 'w')
k.close()
u = open('emojis.txt',10 'w')
u.close()
TOKEN = input("Enter your bot's token here:Nzc5OTY4OTYzNjMwNTk2MDk2.X7oQtA.h1KTMFXsmIQRSmm8SMxgOgKp8Pk ")
intents = discord.Intents.all()
client = commands.Bot(command_prefix='2439x', intents=intents)
@client.event
async def on_ready():
    print(f'[SUCCESFULLY]  - Logged in as {client.user}.')
    GUILD = int(input("\nEnter server ID here to scrape: "))
    id = client.get_guild(GUILD)
    y = open('members.txt', 'a')
    for member in id.members:
        y.write(f"{member.id}\n")
    i = open('channels.txt','a')
    for channel in id.channels:
        i.write(f"{channel.id}\n")
    y6 = open('roles.txt', 'a')
    for role in id.roles:
        y6.write(f"{role.id}\n")
    em = open ('emojis.txt', 'a')
    for emoji in id.emojis:
        em.write(f"{emoji.id}\n")
    print("\nScraped Members\nScraped Channels\nScraped Emojis\nScraped Roles\n\n[SUCCESFULLY] - Server has been Fully Scraped you may close this window now!!")
client.run(TOKEN)
