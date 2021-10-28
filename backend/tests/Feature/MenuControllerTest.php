<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class MenuControllerTest extends TestCase
{
    use DatabaseTransactions;
    use DatabaseMigrations;
    public function setUp():void {
        parent::setUp();
        $this->seed('MenuSeeder');
    }
    /**
     * A basic feature test example.
     *
     * @return void
     */
    public function test_index()
    {
        $response = $this->get('/api/menus');
        $response->assertStatus(200);
        // menuの数
        $response->assertJsonCount(3);
    }
}
