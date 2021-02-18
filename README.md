# 導入方法
- discordのbotを作成しtokenを取得後、利用したいサーバーに招待する
- private_sample.pyを参考に`private.py`作成し、tokenとvoice_channel_idを定義する
  - tokenは[ここ](https://discord.com/developers/applications)からMy Applications -> Botで確認できる
  - voice_channel_idはdiscordのボイスチャンネルを右クリック -> IDをコピー
- 必要なライブラリをインストール
    - pip install git+https://github.com/Nkyoku/pyvcroid2.git
    - pip install -r requirements.txt
- `python bot.py`
