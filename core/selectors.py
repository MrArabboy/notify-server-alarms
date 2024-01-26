from api.client import Client
from api.converter import Root
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def get_all_incoming_alarms():
    client = Client()
    alarms = client.alarms(offset=0, limit=100)
    root = Root.from_dict(alarms)
    required_num_of_request = root.total // 100
    items = [item for item in root.items if item.iAlarmLevel == "Critical"]
    for page_num in range(1, required_num_of_request + 1):
        alarms = client.alarms(offset=page_num * 100, limit=100)
        new_root = Root.from_dict(alarms)
        items.extend([item for item in new_root.items if item.iAlarmLevel == "Critical"])
    return items
