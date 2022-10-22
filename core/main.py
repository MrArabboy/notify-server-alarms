import requests
import time
from datetime import datetime

from api.converter import  Item

from .services import (
    generate_dict_of_alarms,
    save_object,
    load_object_from_db,
    separate_resolved_alarms,
    seperate_new_alarms,
)
from .selectors import get_all_incoming_alarms

import env


def send_message():
    alarm: Item
    incoming_alarms = generate_dict_of_alarms(alarms=get_all_incoming_alarms())
    try:
        alarms_in_db = load_object_from_db()
    except:
        save_object(incoming_alarms)
        alarms_in_db = load_object_from_db()
    new_alarms = seperate_new_alarms(
        alarms_in_db=alarms_in_db, incoming_alarms=incoming_alarms
    )
    resolved_alarms = separate_resolved_alarms(
        alarms_in_db=alarms_in_db, incoming_alarms=incoming_alarms
    )

    for num_of_request, alarm in enumerate(new_alarms):
        params = {
            "chat_id": env.CHANNEL_ID,
            "text": (
                "🔴\n"
                f"<b>Level:</b> {alarm.iAlarmLevel}\n"
                f"<b>Name:</b> {alarm.svAlarmName}\n"
                f"<b>Info:</b> {alarm.svAdditionalInfo}\n"
                f"<b>Cause:</b> {alarm.svAlarmCause}\n"
                f"<b>Type:</b> {alarm.svMoc}\n"
                f"<b>Object:</b> {alarm.urnByName}\n"
                f"<b>Time:</b> {datetime.fromtimestamp(int(alarm.dtOccurTime)//1000)}\n"
            ),
            "parse_mode": "html",
        }

        if num_of_request != 0 and num_of_request % 20 == 0:
            time.sleep(40)

        response = requests.get(
            url=f"https://api.telegram.org/bot{env.BOT_TOKEN}/sendMessage",
            params=params,
        )
        alarm.message_id = response.json()["result"]["message_id"]

    for alarm in resolved_alarms:
        try:
            alarms_in_db.pop(alarm.iSyncNo)
        except:
            pass
        params = {
            "chat_id": env.CHANNEL_ID,
            "text": (
                "🟢\n"
                f"<b>Resolved:</b> {alarm.svAlarmName}\n"
                f"<b>Info:</b> {alarm.svAdditionalInfo}\n"
                f"<b>Cause:</b> {alarm.svAlarmCause}\n"
                f"<b>Type:</b> {alarm.svMoc}\n"
                f"<b>Object:</b> {alarm.urnByName}\n"
                f"<b>Time:</b> {datetime.fromtimestamp(int(alarm.dtOccurTime)//1000)}\n"
            ),
            "parse_mode": "html",
        }
        response = requests.get(
            url=f"https://api.telegram.org/bot{env.BOT_TOKEN}/sendMessage",
            params=params,
        )
    alarms_in_db.update(generate_dict_of_alarms(alarms=new_alarms))
    save_object(alarms_in_db)


