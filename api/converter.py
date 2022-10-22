from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class Item:
    iDisplay: str
    dtArrivedTime: str
    dtOccurTime: str
    dtClearTime: str
    objectUrn: str
    svAdditionalInfo: str
    svAlarmName: str
    iSyncNo: int
    iParse: int
    svAlarmCause: str
    iAlarmCategory: str
    svClearAlarmUserName: str
    objectType: str
    iClearType: str
    svMoc: str
    dtUpdateTime: str
    svLocationInfo: str
    iAlarmLevel: str
    iAffectOpFlag: str
    iSerialNo: int
    svEventType: str
    urnByName: str
    svAlarmID: str
    iAutoClear: str

    @staticmethod
    def from_dict(obj: Any) -> "Item":
        _iDisplay = str(obj.get("iDisplay"))
        _dtArrivedTime = str(obj.get("dtArrivedTime"))
        _dtOccurTime = str(obj.get("dtOccurTime"))
        _dtClearTime = str(obj.get("dtClearTime"))
        _objectUrn = str(obj.get("objectUrn"))
        _svAdditionalInfo = str(obj.get("svAdditionalInfo"))
        _svAlarmName = str(obj.get("svAlarmName"))
        _iSyncNo = int(obj.get("iSyncNo"))
        _iParse = int(obj.get("iParse"))
        _svAlarmCause = str(obj.get("svAlarmCause"))
        _iAlarmCategory = str(obj.get("iAlarmCategory"))
        _svClearAlarmUserName = str(obj.get("svClearAlarmUserName"))
        _objectType = str(obj.get("objectType"))
        _iClearType = str(obj.get("iClearType"))
        _svMoc = str(obj.get("svMoc"))
        _dtUpdateTime = str(obj.get("dtUpdateTime"))
        _svLocationInfo = str(obj.get("svLocationInfo"))
        _iAlarmLevel = str(obj.get("iAlarmLevel"))
        _iAffectOpFlag = str(obj.get("iAffectOpFlag"))
        _iSerialNo = int(obj.get("iSerialNo"))
        _svEventType = str(obj.get("svEventType"))
        _urnByName = str(obj.get("urnByName"))
        _svAlarmID = str(obj.get("svAlarmID"))
        _iAutoClear = str(obj.get("iAutoClear"))
        return Item(
            _iDisplay,
            _dtArrivedTime,
            _dtOccurTime,
            _dtClearTime,
            _objectUrn,
            _svAdditionalInfo,
            _svAlarmName,
            _iSyncNo,
            _iParse,
            _svAlarmCause,
            _iAlarmCategory,
            _svClearAlarmUserName,
            _objectType,
            _iClearType,
            _svMoc,
            _dtUpdateTime,
            _svLocationInfo,
            _iAlarmLevel,
            _iAffectOpFlag,
            _iSerialNo,
            _svEventType,
            _urnByName,
            _svAlarmID,
            _iAutoClear,
        )


@dataclass
class Root:
    total: int
    updateFlag: int
    viewId: int
    pageno: int
    itemSize: int
    items: List[Item]

    @staticmethod
    def from_dict(obj: Any) -> "Root":
        _total = int(obj.get("total"))
        _updateFlag = int(obj.get("updateFlag"))
        _viewId = int(obj.get("viewId"))
        _pageno = int(obj.get("pageno"))
        _itemSize = int(obj.get("itemSize"))
        _items = [Item.from_dict(y) for y in obj.get("items")]
        return Root(_total, _updateFlag, _viewId, _pageno, _itemSize, _items)
