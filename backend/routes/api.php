<?php

use App\Http\Controllers\MenuController;
use App\Http\Controllers\UserController;
use App\Http\Controllers\UserMenuController;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

// ユーザー情報
Route::get('/users', [UserController::class, 'index']);
// ユーザー登録
Route::post('/users', [UserController::class, 'create']);
// グループのユーザー一覧
Route::get('/users/{groupId}', [UserController::class, 'index_group']);
// メニュー一覧
Route::get('/menus', [MenuController::class, 'index']);
// 筋トレ記録登録
Route::post('/records', [UserMenuController::class, 'create'])->middleware('is_created_user');
// グループの記録のランキング
Route::get('/records/{groupId}', [UserMenuController::class, 'index_group']);

