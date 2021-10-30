<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400"></a></p>

<p align="center">
<a href="https://travis-ci.org/laravel/framework"><img src="https://travis-ci.org/laravel/framework.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

## API URL

|情報|METHOD|URL|クエリ|
|:---:|:---:|:---:|:---:|
|ユーザー情報取得|GET|/api/users|userId -> string型|
|ユーザー登録|POST|/api/users|userId -> string型<br>slackName -> string型<br>groupId -> string型|
|ユーザーグループ一覧|GET|/api/users/{groupId}|無し|
|メニュー一覧|GET|/api/menus|無し|
|記録のランキング|GET|/api/records/{groupId}|無し|
|記録登録|POST|/api/records|userId -> string型<br>menuId -> int型<br>numberOfTimes -> int型|