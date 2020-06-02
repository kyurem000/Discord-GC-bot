import discord
import os

client = discord.Client()

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


access_token = os.environ["BOT_TOKEN"]
# 토큰 보내기
client.run(access_token)
