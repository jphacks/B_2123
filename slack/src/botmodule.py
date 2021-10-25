from datetime import time

from slackbot.bot import default_reply, listen_to, respond_to

import func as fx
import slackbot_settings

# 0 通常
# 1 ユーザー登録
# 2 運動記録登録
status = 0
forbitten_list = ["かえる跳び"]
menu_dict = {"腕立て" : "回" , "ランニング" : "分"}
tmp_menu : str= ""

# メンションあり応答
@respond_to('こんにちは')
def greet(message):
    global status
    status = 0
    # メンションして応答
    user_id : str = message.body["user"]
    info = fx.get_user_name(user_id)
    if(info[0]):
        message.reply(f"やぁ，こんにちは {info[1]}")
    else:
        message.reply(f"知らない顔だな，入会しなさい\n「入会」 と返信してくれ")

# メンションなし応答
@respond_to('入会')
def enter(message):
    global status
    user_id : str = message.body["user"]
    if(fx.get_user_name(user_id)[0]):
        message.reply(f"はっはっは、 君はもう仲間じゃないっか")
        status = 0
    else:
        message.reply("入会希望だな，名前を教えてくれ")
        status = 1
    # メンションなしで応答

@respond_to("テスト")
def test(message):
    global status
    status = 0
    print(message.body)
    message.reply("これはテストです")

@respond_to("仲間")
def test(message):
    global status
    status = 0
    l = fx.user_list(" ")
    if(len(l) == 0):
        message.reply(f"ウム、まだ仲間は居ないようだね")
    if(len(l) == 1 and l[0][0] == message.body["user"] ):
        message.reply(f"うん、仲間は君だけなのか\nもっと誘いなよ")
    else:
        message.reply(f"今の仲間は彼らだね\n{ ' '.join([i[1] for i in l]) }")

@respond_to("メニュー")
def menu(message):
    global forbitten_list
    global menu_dict
    message.reply(f"今登録されているメニューは、{' ・'.join([i for i in forbitten_list+list(menu_dict.keys())])} があるよ")

@respond_to("記録")
def test(message):
    global status
    status = 2
    message.reply("記録しに来てくれたか、うれしいじゃないか！\n今日のメニューを教えてくれ")

@default_reply
def my_default_handler(message):
    global status
    global forbitten_list
    global menu_dict
    global tmp_menu

    if (status == 1):
        user_id : str = message.body["user"]
        user_name = message.body["text"]
        message.reply(f"ユーザー名は 「{user_name}」 だね")
        fx.user_add(user_id, user_name)
        status = 0

    elif (status == 2):
        menu_name : str = message.body["text"]
        if (menu_name in forbitten_list):
            message.send("こらっ！ そんなメニューやっちゃだめだぞ\n君のマッスルが泣いてるぜ")
            status = 0
        elif (menu_name in menu_dict.keys()):
            tmp_menu = menu_name
            message.send(f"ほぅ、{menu_name} か、いいじゃないか\n何{menu_dict[menu_name]} ぐらいできたかい？")
            status = 3

    elif (status == 3):
        user_id : str = message.body["user"]
        menu_times : int = int(message.body["text"])
        message.send(f"{tmp_menu} を {menu_times} {menu_dict[tmp_menu]} だね\nしっかり記録しておこう")
        fx.submit_menu(user_id=user_id, menu_name=tmp_menu, time=menu_times)
        status = 0

    else:
        commands = ["こんにちは", "入会", "仲間","メニュー","記録"]
        message.send(f"今あるコマンドは {' '.join(commands)} だね")
        # message.send(slackbot_settings.DEFAULT_REPLY)

