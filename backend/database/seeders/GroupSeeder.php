<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class GroupSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        // データのクリア
        DB::table('groups')->truncate();
        $groups = [
            [
                'groupId' => '1'
            ]
        ];
        foreach ($groups as $group) {
            DB::table('groups')->insert($group);
        }
    }
}
