from pathlib import Path
import os
import pickle


BASE_DIR = Path(__file__).resolve().parent.parent
PICKLE_FILE = os.path.join(BASE_DIR, "data.pickle")


def save_object(obj):
    try:
        with open(PICKLE_FILE, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        raise ValueError(
            "Error during pickling object (Possibly unsupported):", ex
        ) from ex


def load_object_from_db() -> object:
    try:
        with open(PICKLE_FILE, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        raise ValueError(
            "Error during unpickling object (Possibly unsupported):", ex
        ) from ex


def generate_dict_of_alarms(*, alarms: list) -> dict:
    return {alarm.iSyncNo: alarm for alarm in alarms}


def seperate_new_alarms(*, alarms_in_db: dict, incoming_alarms: dict) -> list:
    new_alarm_IDs = set(incoming_alarms).difference(set(alarms_in_db))
    return [incoming_alarms.get(ID) for ID in new_alarm_IDs]


def separate_resolved_alarms(*, alarms_in_db: dict, incoming_alarms: dict) -> list:
    resolved_alarm_IDs = set(alarms_in_db).difference(set(incoming_alarms))
    return [alarms_in_db.get(ID) for ID in resolved_alarm_IDs]
