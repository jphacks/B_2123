<?php

namespace App\Http\Controllers;

use App\Models\Group;
use App\Models\User;
use Illuminate\Http\Request;
use App\Models\UserMenu;
use Illuminate\Support\Facades\Validator;

class UserMenuController extends Controller
{
  public function index(UserMenu $userMenu)
  {
    $ranking = $userMenu->orderBy('numberOfTimes', 'desc')->take(10)->join('users', 'user_menus.userId', '=', 'users.userId')->get();
    return response()->json($ranking);
  }
  public function index_group($groupId, Group $group, User $user)
  {
    try {
      $group->groupId_check($groupId);
      $group_users = $user->where('groupId', $groupId)->get();
      $ranking = $group_users->join('user_menus', 'users.userId', '=', 'user_menus.userId')->orderBy('numberOfTimes', 'desc')->take(5)->get();
      return response()->json($ranking);
    } catch (\Exception $e) {
      return response()->json(['message' => $e->getMessage()], 404);
    }
  }
  public function create(Request $request, UserMenu $userMenu)
  {
    $params = $request->only(['userId', 'menuId', 'numberOfTimes']);
    try {
      // バリデーションルール
      $validator = Validator::make($params, [
        'userId' => ['required', 'integer'],
        'menuId' => ['required', 'integer'],
        'numberOfTimes' => ['required', 'integer']
      ]);
      // バリデーション
      if($validator->fails()) {
        throw new \Exception("入力内容にエラーがあります", 1);
      }
      // メニューの存在チェック
      $result = $userMenu->create($params);
      if(!isset($result)) {
        throw new \Exception("登録に失敗しました", 1);
      }
      return response()->json(['message' => '登録しました'], 200);
    } catch (\Exception $e) {
      return response()->json(['message' => $e->getMessage()], 404);
    }
  }
}
