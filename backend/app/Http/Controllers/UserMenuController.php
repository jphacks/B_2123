<?php

namespace App\Http\Controllers;

use App\Models\Group;
use App\Models\Menu;
use App\Models\User;
use Illuminate\Http\Request;
use App\Models\UserMenu;
use Illuminate\Support\Facades\Validator;

class UserMenuController extends Controller
{
  public function index(Request $request, UserMenu $userMenu)
  {
    $userId = $request->userId;
    $records = $userMenu->where('userId', $userId)->get();
    return response()->json($records);
  }
  public function index_group($groupId, Group $group, UserMenu $userMenu)
  {
    try {
      $group->groupId_check($groupId);
      $ranking = $userMenu->orderBy('numberOfTimes', 'desc')->join('users', 'user_menus.userId', '=', 'users.userId')->where('groupId', $groupId)->take(5)->get();
      return response()->json($ranking);
    } catch (\Exception $e) {
      return response()->json(['message' => $e->getMessage()], 400);
    }
  }
  public function create(Request $request, UserMenu $userMenu)
  {
    $params = $request->only(['userId', 'menuId', 'numberOfTimes']);
    try {
      // バリデーションルール
      $validator = Validator::make($params, [
        'userId' => ['required', 'string', 'exists:users,userId'],
        'menuId' => ['required', 'integer', 'exists:menus,id'],
        'numberOfTimes' => ['required', 'integer', 'min:1']
      ]);
      // バリデーション
      if($validator->fails()) {
        throw new \Exception("入力内容にエラーがあります", 1);
      }
      $result = $userMenu->create($params);
      if(!isset($result)) {
        throw new \Exception("登録に失敗しました", 1);
      }
      return response()->json(['message' => '登録しました'], 200);
    } catch (\Exception $e) {
      return response()->json(['message' => $e->getMessage()], 400);
    }
  }
}
