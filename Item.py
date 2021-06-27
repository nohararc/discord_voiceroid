from dataclasses import dataclass
import discord

@dataclass
class Item:
    text_channel: discord.TextChannel = None
    voice_channel: discord.VoiceChannel = None
