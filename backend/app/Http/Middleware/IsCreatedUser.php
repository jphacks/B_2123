<?php

namespace App\Http\Middleware;

use App\Models\User;
use Closure;
use Illuminate\Http\Request;

class IsCreatedUser
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle(Request $request, Closure $next)
    {
        $user = new User;
        $userId = $request->userId;
        if($user->userId_check($userId)) {
            return $next($request);
        } else {
            return response()->json(['message' => 'このユーザーIDは無効です'], 400);
        }
    }
}
