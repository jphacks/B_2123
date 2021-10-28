<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Group extends Model
{
    use HasFactory;
    
    // プライマリーキーのカラム名
    protected $primaryKey = 'groupId';

    // プライマリーキーの型
    protected $keyType = 'string';

    // プライマリーキーは自動連番か？
    public $incrementing = false;

    protected $table = 'groups';
    protected $fillable = [
        'groupId',
    ];
    public function groupId_check($groupId)
    {
        $res = $this->where('groupId', $groupId)->first();
        if(empty($res)) {
            throw new \Exception("このグループIDは存在しません", 1);
        }
    }
    public function users()
    {
        return $this->hasMany(User::class, 'groupId', 'groupId');
    }
}
