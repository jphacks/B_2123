<?php

namespace App\Models;

use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
use Illuminate\Support\Facades\Log;
use Laravel\Sanctum\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens, HasFactory, Notifiable;


    // プライマリーキーのカラム名
    protected $primaryKey = 'userId';

    // プライマリーキーの型
    protected $keyType = 'string';

    // プライマリーキーは自動連番か？
    public $incrementing = false;

    /**
     * The attributes that are mass assignable.
     *
     * @var string[]
     */
    protected $fillable = [
        'userId',
        'slackName',
        'groupId',
    ];
    public function userId_check($userId)
    {
        $res = $this->where('userId', $userId)->first();
        if(isset($res)) {
            return true;
        } else {
            return false;
        }
    }
    // リレーションシップ
    public function menus()
    {
        return $this->hasMany(UserMenu::class, 'userId');
    }
}
