# nikutai（Slackで動く運動記録アプリ）

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2021/07/JPHACKS2021_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
- コロナ禍によるリモートワークが進む中、通勤・通学がなくなり運動不足になる人が増えた
- リモートワークに Slack などのコミュニケーションツールが導入されている
### 製品説明（具体的な製品の説明）
- 運動不足の解消に向けた、Slack で動作する運動管理ツール
- slack bot の 「nikutai」 との会話で運動を登録できる
- 同じワークスペースの利用者と運動履歴を比較し、表示可能
### 特長
#### 1. slackbotで簡単に登録できる
#### 2. 同じワークスペースの利用者と結果を比較・競争できる

### 解決出来ること
- 運動不足の解消
### 今後の展望
- 運動の強度に合わせたパラメータの作成
- ワークスペースをまたいだ管理などの実装
### 注力したこと（こだわり等）
- Python の開発でできるだけモダンな開発を取り入れるようにしたこと
    - Pyenv & Poetry によるパッケージ管理
    - Docstringの整備
    - Typing (型ヒント）の整備

## 開発技術
### 活用した技術
#### API・データ
* SlackAPI

#### フレームワーク・ライブラリ・モジュール
- Web UI : [doc](web/README.md)
    - TypeScript
    - React
    - @netlify
    
- Back Ground : [doc](backend/README.md)
    - PHP
    - Laravel
    - SQLite
- Slackbot : [doc](slack/README.md)
    - Python
    - Slackbot

### 独自技術
#### ハッカソンで開発した独自機能・技術
   - [botmodule](./slack/src/botmodule.py)
       - 応答メッセージの処理に力を入れました
