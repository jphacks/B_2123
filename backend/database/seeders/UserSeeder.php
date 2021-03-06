<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        // データのクリア
        DB::table('users')->truncate();
        $users = [
            [
                'userId' => 'a1',
                'groupId' => '1',
                'slackName' => 'testuser'
            ],
            [
                'userId' => 'b1',
                'groupId' => '1',
                'slackName' => 'testuser2'
            ],
        ];
        foreach ($users as $user) {
            DB::table('users')->insert($user);
        }
    }
}
