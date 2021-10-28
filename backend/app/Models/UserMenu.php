<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class UserMenu extends Model
{
    use HasFactory;
    protected $table = 'user_menus';
    protected $fillable = [
        'userId',
        'menuId',
        'numberOfTimes'
    ];
    // リレーションシップ
    public function user()
    {
        return $this->belongsTo('\App\Models\User', 'userId');
    }
    public function menu()
    {
        return $this->belongsTo('\App\Models\Menu', 'menuId');
    }
}
