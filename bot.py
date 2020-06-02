import discord

client = discord.Client()
# 토큰
token = "NzE3NDcwNzk1NzkzOTU2OTE1.Xtay7A.l3JrYnlnmGoTR0XoLKAEn9n7AT8"

# 준비
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("밤낮이 없어요")

    # 현재 상태 나타내기
    await client.change_presence(status=discord.Status.online, activity=game)

# 반응 이벤트
@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("헬 로우")


# 토큰 보내기
client.run(token)
