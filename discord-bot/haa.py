import random

import discord
from discord import File, Message
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents) 
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@client.event
async def on_message(message):
    if message.content ==('変更'):
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    return

@bot.listen('on_message')
async def on_message(message: Message):

    if message.content in ["スタート", "!s","！s","スタ〜ト","スタ~ト","スタ∼ト","スタ一ト"]:
        await message.channel.send("ーーーーーー担当ーーーーーーー")
        members = [member.mention for member in message.author.voice.channel.members ]
        s = random.sample(["・・・||  Ａ  ||"+"\n-", "・・・||  Ｂ  ||\n-", "・・・||  Ｃ  ||\n-", "・・・||  Ｄ  ||\n-", "・・・||  Ｅ  ||\n-", "・・・||  Ｆ  ||\n-", "・・・||  Ｇ  ||\n-", "・・・||  Ｈ  ||\n-"], len(members))
        for who, sss in zip(members, s):
         whosss = who + sss
         await message.channel.send (whosss)
         

        await message.channel.send("ーーーーーー順番ーーーーーーー")
        hito = [members.display_name for members in message.author.voice.channel.members ]
        random.shuffle(hito)
        await message.channel.send('\n'.join(hito))

        await message.channel.send("ーーーーーーお題ーーーーーーー")
        path = random.choice(["media/2023-02-01_12-49-19_845.jpg",
"media/2023-02-01_12-49-31_810.jpg",
"media/2023-02-01_12-49-42_272.jpg",
"media/2023-02-01_12-50-46_647.jpg",
"media/2023-02-01_12-50-53_955.jpg",
"media/2023-02-01_12-51-00_976.jpg",
"media/2023-02-01_12-51-07_422.jpg",
"media/2023-02-01_12-51-14_340.jpg",
"media/2023-02-01_12-51-22_858.jpg",
"media/2023-02-01_12-51-29_321.jpg",
"media/2023-02-01_12-51-35_594.jpg",
"media/2023-02-01_12-51-42_466.jpg",
"media/2023-02-01_12-51-48_492.jpg",
"media/2023-02-01_12-51-54_863.jpg",
"media/2023-02-01_12-52-00_362.jpg",
"media/2023-02-01_12-52-05_852.jpg",
"media/2023-02-01_12-52-11_384.jpg",
"media/2023-02-01_12-52-25_350.jpg",
"media/2023-02-01_12-52-36_883.jpg",
"media/2023-02-01_12-52-43_026.jpg",
"media/2023-02-01_12-52-49_483.jpg",
"media/2023-02-01_12-52-54_316.jpg",
"media/2023-02-01_12-53-00_557.jpg",
"media/2023-02-01_12-53-06_075.jpg",
"media/2023-02-01_12-53-11_673.jpg",
"media/2023-02-01_12-53-32_404.jpg",
"media/2023-02-01_12-53-51_742.jpg",
"media/2023-02-01_12-53-58_286.jpg",
"media/2023-02-01_12-54-04_445.jpg",
"media/2023-02-01_12-54-10_705.jpg",
"media/2023-02-01_12-54-19_169.jpg",
"media/2023-02-01_12-54-24_665.jpg",
"media/2023-02-01_12-54-28_643.jpg",
"media/2023-02-01_12-54-33_031.jpg",
"media/2023-02-01_12-54-38_233.jpg",
"media/2023-02-01_12-54-42_744.jpg",
"media/2023-02-01_12-54-47_514.jpg",
"media/2023-02-01_12-54-52_045.jpg",
"media/2023-02-01_12-54-55_959.jpg",
"media/2023-02-01_12-55-00_210.jpg",
"media/2023-02-01_12-55-05_107.jpg",
"media/2023-02-01_12-55-10_766.jpg",
"media/2023-02-01_12-55-18_811.jpg",
"media/2023-02-01_12-55-24_250.jpg",
"media/2023-02-01_12-55-29_439.jpg",
"media/2023-02-01_12-55-34_707.jpg",
"media/2023-02-01_12-55-39_180.jpg",
"media/2023-02-01_12-58-37_363.jpg",
"media/2023-02-01_12-58-41_460.jpg",
"media/2023-02-01_12-58-45_579.jpg",
"media/2023-02-01_12-58-48_952.jpg",
"media/2023-02-01_12-58-52_504.jpg",
"media/2023-02-01_12-59-02_517.jpg",
"media/2023-02-01_12-59-06_330.jpg"])
        await message.channel.send(file=File(path))
        return

    if message.content in ["変更","!c","！c"]:
        deleted = await message.channel.purge(limit=2)
        path = random.choice(["media/2023-02-01_12-49-19_845.jpg",
"media/2023-02-01_12-49-31_810.jpg",
"media/2023-02-01_12-49-42_272.jpg",
"media/2023-02-01_12-50-46_647.jpg",
"media/2023-02-01_12-50-53_955.jpg",
"media/2023-02-01_12-51-00_976.jpg",
"media/2023-02-01_12-51-07_422.jpg",
"media/2023-02-01_12-51-14_340.jpg",
"media/2023-02-01_12-51-22_858.jpg",
"media/2023-02-01_12-51-29_321.jpg",
"media/2023-02-01_12-51-35_594.jpg",
"media/2023-02-01_12-51-42_466.jpg",
"media/2023-02-01_12-51-48_492.jpg",
"media/2023-02-01_12-51-54_863.jpg",
"media/2023-02-01_12-52-00_362.jpg",
"media/2023-02-01_12-52-05_852.jpg",
"media/2023-02-01_12-52-11_384.jpg",
"media/2023-02-01_12-52-25_350.jpg",
"media/2023-02-01_12-52-36_883.jpg",
"media/2023-02-01_12-52-43_026.jpg",
"media/2023-02-01_12-52-49_483.jpg",
"media/2023-02-01_12-52-54_316.jpg",
"media/2023-02-01_12-53-00_557.jpg",
"media/2023-02-01_12-53-06_075.jpg",
"media/2023-02-01_12-53-11_673.jpg",
"media/2023-02-01_12-53-32_404.jpg",
"media/2023-02-01_12-53-51_742.jpg",
"media/2023-02-01_12-53-58_286.jpg",
"media/2023-02-01_12-54-04_445.jpg",
"media/2023-02-01_12-54-10_705.jpg",
"media/2023-02-01_12-54-19_169.jpg",
"media/2023-02-01_12-54-24_665.jpg",
"media/2023-02-01_12-54-28_643.jpg",
"media/2023-02-01_12-54-33_031.jpg",
"media/2023-02-01_12-54-38_233.jpg",
"media/2023-02-01_12-54-42_744.jpg",
"media/2023-02-01_12-54-47_514.jpg",
"media/2023-02-01_12-54-52_045.jpg",
"media/2023-02-01_12-54-55_959.jpg",
"media/2023-02-01_12-55-00_210.jpg",
"media/2023-02-01_12-55-05_107.jpg",
"media/2023-02-01_12-55-10_766.jpg",
"media/2023-02-01_12-55-18_811.jpg",
"media/2023-02-01_12-55-24_250.jpg",
"media/2023-02-01_12-55-29_439.jpg",
"media/2023-02-01_12-55-34_707.jpg",
"media/2023-02-01_12-55-39_180.jpg",
"media/2023-02-01_12-58-37_363.jpg",
"media/2023-02-01_12-58-41_460.jpg",
"media/2023-02-01_12-58-45_579.jpg",
"media/2023-02-01_12-58-48_952.jpg",
"media/2023-02-01_12-58-52_504.jpg",
"media/2023-02-01_12-59-02_517.jpg",
"media/2023-02-01_12-59-06_330.jpg"])
        await message.channel.send(file=File(path))  
    return
    
if __name__ == "__main__":
    bot.run(("MTA2ODUzMTUzNDExOTg0MTg1Mw.GU8OFI.63oKoRxRHNELB1Y4LNZkkW--Py3fYm4G5D-V44"), root_logger=True)
    