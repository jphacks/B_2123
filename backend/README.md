
## 開発技術
### 活用した技術
#### API・データ
* 

#### フレームワーク・ライブラリ・モジュール
* Laravel

#### デバイス
* 

## ドメイン
https://test-use-domain.net

## API URL

|情報|METHOD|URL|クエリ|
|:---:|:---:|:---:|:---:|
|ユーザー情報取得|GET|/api/users|userId -> string型|
|ユーザー登録|POST|/api/users|userId -> string型<br>slackName -> string型<br>groupId -> string型|
|ユーザーグループ一覧|GET|/api/users/{groupId}|無し|
|メニュー一覧|GET|/api/menus|無し|
|記録のランキング|GET|/api/records/{groupId}|無し|
|記録登録|POST|/api/records|userId -> string型<br>menuId -> int型<br>numberOfTimes -> int型|


