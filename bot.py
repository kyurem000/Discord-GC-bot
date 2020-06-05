#모듈
import asyncio
import discord
from discord.ext import commands

client = discord.Client()

# 구동되었을때 동작
@client.event
async def on_ready():
    print("logged in as")
    print(client.user.name)
    print(client.user.id)
    print("ready")
    print("==========")
    # 디스코드가 어떤 게임을 플레이하고 있는지
    game = discord.Game("아무것도 안 ")
    await client.change_presence(status=discord.Status.online, activity=game)

# 반응 이벤트
@client.event
async def on_message(message):

    # 메시지를 보낸사람이 봇일때
    if message.author.bot:
    # 동작 무시
        return None
    if message.content.startswith("-명령어"):
        await message.channel.send("-인사, -뭐해")
    if message.content.startswith("-인사"):
        await message.channel.send("(--) (__) 꾸벅")
    if message.content.startswith("-뭐해"):
        await message.channel.send("아무것도 안하고 있워요.")

# 비밀 반응 명령어
    if message.content.startswith("게임"):
        await message.channel.send("게임 그만해")
    if message.content.startswith("https://gall.dcinside.com/"):
        await message.channel.send("디시, 또 너야?")
    if message.content.startswith("캬루"):
        await message.channel.send("캬루, 또 너야?")
    if message.content.startswith("와"):
        await message.channel.send(' "샌즈" ')
    if message.content.startswith("엄"):
        await message.channel.send("준식")
# 임베드
    if message.content.startswith("embed"):
        embed = discord.Embed(title="자기소개서", description="저는_로봇_이에요", color=0x00ff56)
        embed.set_author(name="제작자-Divide", url=" ",
                         icon_url="https://optimal.inven.co.kr/upload/2016/01/19/bbs/i11797314981.png")
        embed.set_thumbnail(url="https://optimal.inven.co.kr/upload/2016/01/19/bbs/i11797314981.png")
        embed.add_field(name="경력", value="없음", inline=False)
        embed.add_field(name="학벌", value="없음", inline=False)
        embed.add_field(name="자격증", value="없음", inline=False)
        embed.add_field(name="적성능력", value="나쁜말 지우기", inline=False)
        embed.set_footer(text="==========")
        await message.channel.send(embed=embed)


@client.event
async def on_message(message):
# 나쁜말 금지
        message_content = message.content
        bad = message_content.find("개새")
        print(bad)
        if bad >= 0:
            await message.channel.send("나쁜말 하지마 - 개새x")
            await message.delete()
        await client.process_commands(message)

        bad2 = message_content.find("씨발")
        print(bad2)
        if bad2 >= 0:
            await message.channel.send("나쁜말 하지마 - 씨x")
            await message.delete()
        await client.process_commands(message)

# 토큰 보내기
client.run("NzE3NDcwNzk1NzkzOTU2OTE1.Xtp3Gw.J1oeLA86HHM6EQJpqcgvu7a46j8")
