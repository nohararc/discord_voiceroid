import discord
import asyncio

from discord.ext import commands
from text2wav import text2wav
import private


def main():
    bot = commands.Bot(command_prefix="/")
    token = private.token


    @bot.event
    async def on_ready():
        print("ready")

    @bot.event
    async def on_message(message):
        # bot自身のメッセージは何もしない
        if message.author.bot:
            return

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


        source = discord.FFmpegPCMAudio(text2wav(message.content))
        voice_client.play(source)

    bot.run(token)


if __name__ == "__main__":
    main()