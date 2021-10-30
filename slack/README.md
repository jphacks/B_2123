# nikutai の slackbot の 説明
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

## コダワリ
- Python の Project としての環境整備を行った点
    - Poetry などの仮想環境の整備
    - 型ヒント の追加

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

## 使い方
### 話しかけ方
- チャンネルでメンション付きで投稿
- ダイレクトメッセージで投稿
### コマンド
- こんにちは
   - nikutai 君に挨拶をします。登録されていないと入会を勧められます。
- 入会
   - 筋トレに入会します。後で名前を入力します
- 仲間
   - 筋トレに参加しているメンバーを確認します。人数が少ないと勧誘されます。
- メニュー
   - いま nikutai 君が知っているメニューが表示されます。個々にあるメニューを登録できます
- 記録
   - 自分の運動記録を登録します。
- ランキング
   - グループ内の運動記録を確認します。外部サイトへ飛びます。