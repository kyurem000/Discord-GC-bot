import discord
client = discord.Client()

# 준비
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("heroku에서 조종중")
    # 현재 상태 나타내기
    await client.change_presence(status=discord.Status.online, activity=game)
# 반응 이벤트
@client.event
async def on_message(message):
    if message.content.startswith("!명령어"):
        await message.channel.send("!인사, !뭐해")
    if message.content.startswith("!인사"):
        await message.channel.send("꾸벅")
    if message.content.startswith("!뭐해"):
        await message.channel.send("일해")
# 토큰 보내기
client.run("NzE3NDcwNzk1NzkzOTU2OTE1.XtbcjA.IIfSHT3IwViHXpn0nXOLYYD9AVc")
