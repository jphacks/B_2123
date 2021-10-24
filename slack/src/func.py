import requests


db : dict[str, str]= {}

def user_add(user_id : str, user_name : str) -> bool:
    db[user_id] = user_name
    return True

def get_user_name(user_id : str ):
    if (user_id in list(db.keys())):
        return [True, db[user_id]]
    else:
        return [False, None]

def user_list(group_id : int) -> bool:
    return True

def submit_menu(user_id : str, menu_name : str, time : int) -> bool:
    return True
