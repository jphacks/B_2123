import json
import os
from pathlib import Path
from typing import Union

from slackbot.bot import default_reply, listen_to, respond_to

import func as fx

# 0 通常
# 1 ユーザー登録
# 2 運動記録登録
# 3 数値入力
status = 0
user_status: dict[str, int] = {}

forbitten_list = ["かえる跳び"]

os.chdir(Path(__file__).parents[2])
print(os.getcwd())
# menus = requests.request("GET", base_url + "/api/menus").json()
menu_dict: dict[str, dict[str, Union[int, str]]] = json.load(
    open("menu_list.json", "r")
)

print(menu_dict)

tmp_menu: str = ""


# メンションあり応答
@respond_to("こんにちは")
def greet(message):
    global status
    # メンションして応答
    user_id: str = message.body["user"]
    user_status[user_id] = 0
    try:
        info = fx.get_user_name(user_id)
        message.reply(f"やぁ，こんにちは {info[1]}")
    except ValueError:
        message.reply(f"知らない顔だな，入会しなさい\n「入会」 と返信してくれ")


# メンションなし応答
@respond_to("入会")
def enter(message):
    global status
    user_id: str = message.body["user"]
    try:
        fx.get_user_name(user_id)[0]
        message.reply("はっはっは、 君はもう仲間じゃないっか")
        user_status[user_id] = 0
    except ValueError:
        message.reply("入会希望だな，名前を教えてくれ")
        user_status[user_id] = 1
        print("入会")
    # メンションなしで応答


@respond_to("テスト")
def test(message):
    global status
    user_status[user_id] = 0
    print(message.body)
    message.reply("これはテストです")


@respond_to("メニュー")
def menu(message):
    global forbitten_list
    global menu_dict
    message.reply(f"今登録されているメニューは、{' ・'.join(menu_dict.keys())} があるよ")


@default_reply
def my_default_handler(message):
    global status
    global forbitten_list
    global menu_dict
    global tmp_menu

    group_id: str = message.body["source_team"]
    user_id: str = message.body["user"]
    content: str = message.body["text"]

    print(content)

    if user_id in user_status.keys():
        if user_status[user_id] == 1:
            user_name = content
            message.reply(f"ユーザー名は 「{user_name}」 だね")
            fx.user_add(group_id=group_id, user_id=user_id, user_name=user_name)
            user_status[user_id] = 0

        elif user_status[user_id] == 2:
            menu_name: str = content
            if menu_name in forbitten_list:
                message.send("こらっ！ そんなメニューやっちゃだめだぞ\n君のマッスルが泣いてるぜ")
                user_status[user_id] = 0
            elif menu_name in menu_dict.keys():
                tmp_menu = menu_name
                message.send(
                    f"ほぅ、{menu_name} か、いいじゃないか\n何{menu_dict[menu_name]['unit']} ぐらいできたかい？"
                )
                user_status[user_id] = 3

            else:
                message.reply("おっと，私の知らないメニューか，勉強しておこう\nメニューから選んでくれたまえ\n")
        elif user_status[user_id] == 3:
            try:
                menu_times: int = int(content)
                message.reply(
                    f"{tmp_menu} を {menu_times} {menu_dict[tmp_menu]['unit']} だね\nしっかり記録しておこう"
                )
                fx.submit_menu(
                    user_id=user_id, menu_id=menu_dict[tmp_menu]["id"], time=menu_times
                )
                user_status[user_id] = 0
            except ValueError:
                message.reply("おっと！ 数値を入力してくれよ")

    else:
        if "仲間" in content:
            l: dict[str, str] = fx.user_list(group_id=group_id)
            print(l)
            if len(l) == 0:
                message.reply(f"ウム、まだ仲間は居ないようだね\nさぁ，入会するんだ")
            if len(l) == 1 and l.keys()[0] == user_id:
                message.reply(f"うん、仲間は君だけなのか\nもっと誘いなよ")
            else:
                message.reply(f"今の仲間は彼らだね\n{ ', '.join(l.values() )}")
        elif "記録" in content:
            user_status[user_id] = 2
            message.reply("記録しに来てくれたか、うれしいじゃないか！\n今日のメニューを教えてくれ")

        elif "ランキング" in content:
            message.send(f"君たちのグループのランキングはこれだね\n{fx.ranking(group_id)}")

        else:
            commands = ["こんにちは", "入会", "仲間", "メニュー", "記録", "ランキング"]
            message.send(f"今あるコマンドは {' '.join(commands)} だね")
        # message.send(slackbot_settings.DEFAULT_REPLY)
