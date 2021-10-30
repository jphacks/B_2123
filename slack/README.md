## 動作方法
1. slack bot の作成
- hubot を slack ワークスペースに追加
- [参考サイト](https://miyabikno-jobs.com/entrance-labotlatori/#Slackbot%E7%94%A8%E3%81%AEAPI%E3%83%88%E3%83%BC%E3%82%AF%E3%83%B3%E3%82%92%E5%8F%96%E5%BE%97%E3%81%99%E3%82%8B) の "Slackbot用のAPIトークンを取得する" を参考にしてください
2. API key を slackbot_settings.py の API_TOKEN に代入
3. python 環境の構築
- pyenv, poetry を追加
- `cd slack && pyenv install 3.9.6 && poetry install`
4. 実行
- `poetry shell && python src/main.py`

## 仕様
- Python 3.9.6
- ライブラリ
    - slackbot
    - requests
    - その他標準ライブラリ

## ファイル構成
```
src/
  ├ botmodule.py : bot 応答方法が記録されている
  ├ func.py : サーバーとの通信周りの実装
  ├ main.py : bot 起動用プログラム
  └ slackbot_settings.py : bot の設定ファイル
├ pyproject.toml : python の環境セットアップファイル
└ README.md : この資料
```
