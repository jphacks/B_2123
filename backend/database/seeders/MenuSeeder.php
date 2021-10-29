<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class MenuSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        // データのクリア
        DB::table('menus')->truncate();
        $menusName = ['腕立て', '腹筋', '懸垂'];
        foreach ($menusName as $menuName) {
            DB::table('menus')->insert(['menuName' => $menuName]);
        }
    }
}
