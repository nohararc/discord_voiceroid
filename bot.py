import discord
import asyncio

from discord.ext import commands
from text2wav import text2wav
import private
import re
import pyvcroid2

def main():
    bot = commands.Bot(command_prefix="!")
    token = private.token

    # voiceroid2 client
    vc = pyvcroid2.VcRoid2()
    lang_list = vc.listLanguages()
    if "standard" in lang_list:
        vc.loadLanguage("standard")
    else:
        raise Exception("No language library")

    voice_list = vc.listVoices()
    if 0 < len(voice_list):
        vc.loadVoice(voice_list[0])
    else:
        raise Exception("No voice library")
    vc.param.volume = 1.0
    vc.param.speed = 1.0
    vc.param.pitch = 1.0
    vc.param.emphasis = 1.0
    vc.param.pauseMiddle = 80
    vc.param.pauseLong = 100
    vc.param.pauseSentence = 200
    vc.param.masterVolume = 1.0

    @bot.event
    async def on_ready():
        print("ready")

    @bot.command()
    async def leave(ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect()


    @bot.event
    async def on_message(message):
        # bot自身のメッセージは何もしない
        if message.author.bot:
            return

        # 通話から抜ける
        if message.content in ["bye", "leave"]:
            voice_client = message.guild.voice_client
            await voice_client.disconnect()
            return

        # ユーザーidが含まれる場合ユーザー名に変換する
        pattern = r"<@!(?P<user_id>\d+)>"
        m = re.match(pattern, message.content)
        if m:
            user_name = bot.get_user(int(m.group("user_id"))).name
            message.content = re.sub(pattern, user_name, message.content)


        # 文字が長すぎると区切る
        max_length = 30
        if len(message.content) > max_length:
            message.content = message.content[:max_length] + " 以下略"

        # 通話に参加
        voice_client = message.guild.voice_client
        if not voice_client:
            voice_client = await bot.get_channel(private.voice_channel_id).connect()

        # 喋っている途中は待つ
        while voice_client.is_playing():
            await asyncio.sleep(0.5)


        # テキストをwavファイルに変換してボイチャに流す
        source = discord.FFmpegPCMAudio(text2wav(vc, message.content))
        voice_client.play(source)

    bot.run(token)


if __name__ == "__main__":
    main()
