<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;

class UserMenuSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        // データのクリア
        DB::table('user_menus')->truncate();
        $records = [
            [
                'userId' => 'a1',
                'menuId' => 1,
                'numberOfTimes' => 1,
            ]
        ];
        foreach ($records as $record) {
            DB::table('user_menus')->insert($record);
        }
    }
}
