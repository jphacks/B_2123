<?php

namespace Tests\Feature;

use App\Models\Group;
use App\Models\User;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Support\Facades\Log;
use Tests\TestCase;

class UserControllerTest extends TestCase
{
    use DatabaseTransactions;
    use DatabaseMigrations;
    /**
     * A basic feature test example.
     *
     * @return void
     */
    public function test_create()
    {
        $user_count = User::count();
        $group_count = Group::count();
        $response = $this->post('/api/users', [
            'userId' => 'aaaaaa',
            'groupId' => 'a1',
            'slackName' => 'userName'
        ]);
        $user_count++;
        $group_count++;
        $this->assertEquals($user_count, User::count());
        $this->assertEquals($group_count, Group::count());
        $response->assertStatus(200);
    }
    public function test_index_group()
    {
        $groupId = 'a10000a';
        Group::create(['groupId' => $groupId]);
        $response = $this->get("/api/users/${groupId}");
        $response->assertOk();
    }
}
