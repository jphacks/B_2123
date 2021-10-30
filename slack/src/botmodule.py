import json
import os
import re
from pathlib import Path
from typing import Union

from slackbot.bot import default_reply, respond_to

import func as fx

# 0 通常
# 1 ユーザー登録
# 2 運動記録登録
# 3 数値入力
status = 0
user_status: dict[str, int] = {}
commands = ["こんにちは", "入会", "仲間", "メニュー", "記録", "ランキング"]

forbitten_list = ["かえる跳び"]
tmp_menu: str = ""

os.chdir(Path(__file__).parents[2])
print(os.getcwd())
# menus = requests.request("GET", base_url + "/api/menus").json()
menu_dict: dict[str, dict[str, Union[int, str]]] = json.load(
    open("menu_list.json", "r")
)

print(menu_dict)


@respond_to(r".+")
def all_respond_func(message):
    global user_status
    global forbitten_list
    global menu_dict
    global tmp_menu
    global commands

    process: int = 0

    group_id: str = message.body["source_team"]
    user_id: str = message.body["user"]
    content: str = message.body["text"]

    print(f"{content}")

    if user_id in user_status.keys():
        if user_status[user_id] == 1:
            process = 1
            user_name = content
            message.reply(f"ユーザー名は 「{user_name}」 だね")
            fx.user_add(group_id=group_id, user_id=user_id, user_name=user_name)
            user_status[user_id] = 0

        elif user_status[user_id] == 2:
            process = 1
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
                message.reply(
                    f"おっと，私の知らないメニューか，勉強しておこう\nメニュー : {'・'.join(menu_dict.keys())}から選んでくれたまえ\n"
                )
        elif user_status[user_id] == 3:
            process = 1
            try:
                matched_item = re.match("[0-9]+", re.sub(",", "", content)).group()
                # matched_item: str = re.search(pattern, content)
                menu_times = int(matched_item)

                message.reply(
                    f"{tmp_menu} を {menu_times} {menu_dict[tmp_menu]['unit']} だね\nしっかり記録しておこう"
                )
                fx.submit_menu(
                    user_id=user_id, menu_id=menu_dict[tmp_menu]["id"], time=menu_times
                )
                user_status[user_id] = 0
            except ValueError:
                message.reply("おっと！ 数値を入力してくれよ")
        # else:
        #     message.send(f"今あるコマンドは {' '.join(commands)} だね\n私の知っている言葉で頼むよ")
    if not process:
        user_status[user_id] = 0
        if "こんにちは" in content:
            try:
                info = fx.get_user_name(user_id)
                message.reply(f"やぁ，こんにちは {info}")
            except ValueError:
                message.reply(f"知らない顔だな，入会しなさい\n「入会」 と返信してくれ")

        elif "入会" in content:
            try:
                fx.get_user_name(user_id)[0]
                message.reply("はっはっは、 君はもう仲間じゃないっか")
            except ValueError:
                message.reply("入会希望だな，名前を教えてくれ")
                user_status[user_id] = 1
                print("入会")

        elif "仲間" in content:
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
            message.reply(
                f"記録しに来てくれたか、うれしいじゃないか！\n今日のメニュー「{'・'.join(menu_dict.keys())}」から教えてくれ"
            )

        elif "ランキング" in content:
            message.reply(
                f"そう，走る王様はこの私...\n君たちのグループのランキングはこれだね\n{fx.ranking(group_id= group_id)}"
            )

        elif "メニュー" in content:
            message.reply(f"今登録されているメニューは、{'・'.join(menu_dict.keys())} があるよ")

        elif "テスト" in content:
            print(message.body)
            message.reply(f"これはテストです\n{message.body}")

        else:
            message.send(f"今あるコマンドは {' '.join(commands)} だね\n私の知っている言葉で頼むよ")
        # message.send(slackbot_settings.DEFAULT_REPLY)


# @default_reply
# def my_default_handler(message):
#     text = message.body["text"]  # メッセージを取り出す
#     # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
#     msg = "あなたの送ったメッセージは\n```" + text + "```"
#     message.reply(msg)  # メンション
