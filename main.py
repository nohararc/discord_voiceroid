import pyvcroid2
from discord.ext import commands

import private
from bot import VoiceroidTTSBot


def main():
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

    token = private.token
    bot = commands.Bot(command_prefix=commands.when_mentioned_or("."))

    @bot.event
    async def on_ready():
        print("ready")

    bot.add_cog(VoiceroidTTSBot(bot, vc))
    bot.run(token)


if __name__ == "__main__":
    main()
