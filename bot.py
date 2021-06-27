from ui import SelectTextChannel, SelectVoiceChannel
import discord
import asyncio

from discord.ext import commands
from text2wav import text2wav
from Item import Item
import pyvcroid2

class VoiceroidTTSBot(commands.Cog):
    def __init__(self, bot, vc):
        self.bot: commands.Bot = bot
        self.vcroid: pyvcroid2.VcRoid2 = vc
        self.voice_channel: discord.VoiceChannel = None
        self.voice_client: discord.VoiceClient = None

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:  # bot自身のメッセージは何もしない
            return
        if Item.text_channel is None: # 初期設定
            # text channel選択画面出す
            text_channels = message.guild.text_channels
            await message.channel.send(
                "読み上げるテキストチャンネルを選んでください",
                view=SelectTextChannel(text_channels=text_channels[:5])
            )

            # voice channel選択画面出す
            voice_channels = message.guild.voice_channels
            await message.channel.send(
                "ボイスチャンネルを選んでください",
                view=SelectVoiceChannel(voice_channels=voice_channels[:5])
            )
        else:
            # ここに読み上げの処理を書く
            if not self.voice_client:
                self.voice_client = await Item.voice_channel.connect()
            if message.channel == Item.text_channel:
                # 喋っている途中は待つ
                while self.voice_client.is_playing():
                    await asyncio.sleep(0.1)
                print(message.content)
                source = discord.FFmpegPCMAudio(text2wav(self.vcroid, message.content))
                self.voice_client.play(source)

    @commands.command()
    async def d(self, ctx: commands.Context):
        print(f"debug: {Item.text_channel, Item.voice_channel}")
