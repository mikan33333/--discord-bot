import random

import discord
from discord import Message
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents) 
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.listen('on_message')
async def on_message(message: Message):
    if message.author.bot:
        return

    where = random.sample(["運動会で",
"ボードゲームで",
"ギャンブルで",
"お葬式で",
"修学旅行で",
"卒業式で",
"バレンタインで",
"コンビニで",
"映画館で",
"メイド喫茶で",
"結婚式で",
"部活動で",
"合コンで",
"サバイバルで",
"オリンピックで",
"誘拐で",
"実家で",
"「好きなアニメ」で",
"海で",
"RPGで",
"クリスマスで",
"カラオケで",
"銭湯で",
"トイレで",
"テストで",
"面接で",
"電車で",
"「好きなマンガ」で",
"海外旅行で",
"寿司屋で",
"アイドルで",
"裁判で",
"ファッションで",
"野球で",
"水泳で",
"数学で",
"文化祭で",
"飛行機で",
"「好きなゲーム」で",
"キャンプで",
"誕生日で",
"服屋で",
"カフェで",
"バーベキューで",
"公園で",
"ラーメン屋で",
"図書館で",
"美容室で",
"お参りで",
"占いで",
"夏祭りで",
"タクシーで",
"サッカーで",
"相撲で",
"同窓会で",
"デパートで",
"SNSで",
"美術館で",
"告白で",
"バイトで",
"エレベーターで",
"テニスで",
"授業中で",
"ホテルで",
"デートで",
"プールで",
"「好きな映画」で",
"お正月で",
"遊園地で",
"レストランで",
"睡眠中で",
"体育で",
"ライブで",
"お風呂で",
"給食で",
"おばけ屋敷で",
"ハロウィンで",
"病院で",
"動物園で",
"料理番組で"], 1)
    emotion = random.sample(["うれしいランキング",
"むかつくことランキング",
"はずかしいことランキング",
"こわいことランキング",
"かなしいことランキング"], 1)
    for wheres, emotions in zip(where, emotion): 
         whereemotion = "【" + wheres + emotions + "】"

    if message.content in ["スタート3", "s3"]:
        await message.channel.send("ーーーーーー担当ーーーーーーー")
        members = ["親", "参加者A", "参加者A","参加者B","参加者B"]
        s = random.sample(["１", "２", "３", "４", "５"], 5)
        for who, sss in zip(members, s):
            whosss = who + "・・・||" + sss + "||位\n-"
            await message.channel.send (whosss) 
        await message.channel.send("ーーーーーーお題ーーーーーーー")
        await message.channel.send (whereemotion)
        return

    if message.content in ["スタート4", "s4"]:
        await message.channel.send("ーーーーーー担当ーーーーーーー")
        members = ["親", "参加者A", "参加者B", "参加者C"]
        s = random.sample(["A", "B", "C", "D"], 4)
        for who, sss in zip(members, s):
             whosss = who + "・・・||" + sss + "||\n-"
             await message.channel.send (whosss)
        await message.channel.send("ーーーーーーお題ーーーーーーー")
        await message.channel.send (whereemotion)     
        return    

    if message.content in ["スタート5", "s5"]:
        await message.channel.send("ーーーーーー担当ーーーーーーー")
        members = ["親", "参加者A", "参加者B", "参加者C", "参加者D"]
        s = random.sample(["１", "２", "３", "４", "５"], 5)
        for who, sss in zip(members, s):
            whosss = who + "・・・||" + sss + "||位\n-"
            await message.channel.send (whosss)
        await message.channel.send("ーーーーーーお題ーーーーーーー")
        await message.channel.send (whereemotion)
        return    

    if message.content in ["スタート6", "s6"]:
        await message.channel.send("ーーーーーー担当ーーーーーーー")
        members = ["親", "参加者A", "参加者B", "参加者C", "参加者D", "参加者E"]
        s = random.sample(["１", "２", "３", "４", "５", "６"], 6)
        for who, sss in zip(members, s):
            whosss = who + "・・・||" + sss + "||位\n-"
            await message.channel.send (whosss)
        await message.channel.send("ーーーーーーお題ーーーーーーー")
        await message.channel.send (whereemotion)
        return    

    if message.content in ["変更", "c", "!c", "！c"]:
        deleted = await message.channel.purge(limit=2)
        await message.channel.send (whereemotion)
        return
    
    if message.content in ["t"]:
        await message.channel.send("m!wind to 0:00")
        await message.channel.send("m!pause")
            

if __name__ == "__main__":
    bot.run((""), root_logger=True)
    
