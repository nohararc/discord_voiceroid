def main():
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

    text2wav("おはよう")

def text2wav(vc, text):
    filename = "temp.wav"
    speech, tts_events = vc.textToSpeech(text)

    with open(filename, mode="wb") as f:
        f.write(speech)
    return filename


if __name__ == "__main__":
    main()
