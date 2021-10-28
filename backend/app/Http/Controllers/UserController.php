<?php

namespace App\Http\Controllers;

use App\Models\Group;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Facades\Validator;

class UserController extends Controller
{
    public function index()
    {
        $users = User::all();
        return response()->json($users);
    }
    public function create(Request $request, User $user, Group $group)
    {
        $params = $request->only(['userId', 'slackName', 'groupId']);
        try {
            $rules = [
                'userId' => ['required', 'string'],
                'slackName' => ['required', 'string'],
                'groupId' => ['required', 'string']
            ];
            $validator = Validator::make($params, $rules);
            if($validator->fails()) {
                throw new \Exception("無効な入力内容があります");
            }
            if($user->userId_check($params['userId'])) {
                throw new \Exception("すでに登録しているユーザーです", 1);
            }
            $result = $user->create($params);
            if($result == null) {
                throw new \Exception("登録に失敗しました");
            }
            $group->create(['groupId' => $params['groupId']]);
        } catch (\Exception $e) {
            return response()->json(['message' => $e->getMessage()], 404);
        }
        return response()->json(['message' => 'ユーザー登録しました'], 200);
    }
    public function index_group($groupId, Group $group, User $user)
    {
        try {
            $group->groupId_check($groupId);
            $users = $user->where('groupId', $groupId)->get();
            return response()->json(['users' => $users]);
        } catch (\Exception $e) {
            return response()->json(['message' => $e->getMessage()], 404);
        }
    }
}
