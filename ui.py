import discord
from typing import List

from Item import Item


class TextChannelButton(discord.ui.Button["SelectTextChannel"]):
    def __init__(self, label: str, text_channel: discord.TextChannel):
        super().__init__(style=discord.ButtonStyle.secondary, label=None)
        self.text_channel = text_channel
        self.label = label

    async def callback(self, interaction: discord.Interaction):
        content = f"{self.label}を読み上げます"
        for child in self.view.children:
            child.disabled = True
        self.view.stop()

        Item.text_channel = self.text_channel

        await interaction.response.edit_message(content=content, view=self.view)


class SelectTextChannel(discord.ui.View):
    def __init__(self, text_channels: List[discord.TextChannel]):
        super().__init__()
        for tc in text_channels:
            self.add_item(TextChannelButton(label=tc.name, text_channel=tc))


class VoiceChannelButton(discord.ui.Button["SelectVoiceChannel"]):
    def __init__(self, label: str, voice_channel: discord.VoiceChannel):
        super().__init__(style=discord.ButtonStyle.secondary, label=None)
        self.voice_channel = voice_channel
        self.label = label

    async def callback(self, interaction: discord.Interaction):
        content = f"{self.label}で読み上げます"
        for child in self.view.children:
            child.disabled = True
        self.view.stop()

        Item.voice_channel = self.voice_channel

        await interaction.response.edit_message(content=content, view=self.view)


class SelectVoiceChannel(discord.ui.View):
    def __init__(self, voice_channels: List[discord.VoiceChannel]):
        super().__init__()
        for vc in voice_channels:
            self.add_item(VoiceChannelButton(label=vc.name, voice_channel=vc))