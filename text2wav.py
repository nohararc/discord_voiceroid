import requests
import json


def main():
    url = "http://127.0.0.1:8080/api/speechtext/"
    text = "おいおいおいおい"
    json_dict = {
        "Text": text,
        "Kana" : text,
        "Speaker": {
            "Volume": 2,
            "Speed": 2,
            "Pitch" : 1,
            "Emphasis": 1,
            "PauseMiddle" : 100,
            "PauseLong" : 200,
            "PauseSentence" : 0
        }
    }
    res = requests.post(url, data=json.dumps(json_dict))
    print(res.json())
    with open("temp.wav", "wb") as file:
        file.write(res.content)


def text2wav(text):
    url = f"http://127.0.0.1:8080/api/speechtext/{text}"
    res = requests.get(url)
    filename = "temp.wav"
    with open(filename, "wb") as file:
        file.write(res.content)
    return filename


if __name__ == "__main__":
    main()
