import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)


class operateStrategy:
    """operateStrategy
    """

    def queryList(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/operateStrategy/queryList"

        payload = {
            "strategyName": "",
            "strategyStatus": "",
            "updateBy": "",
            "date": None,
            "updateDateStart": None,
            "updateDateEnd": None,
            "pageNum": 1,
            "pageSize": 20
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def listMessageTemplate(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/operateStrategy/listMessageTemplate"
        res = R(url=url, method='POST')
        return res.json()

    def updateStatus1(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/operateStrategy/updateStatus"

        payload = {
            "id": 83,
            "status": 1
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def updateStatus2(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/operateStrategy/updateStatus"

        payload = {
            "id": 83,
            "status": 0
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def addOrUpdate(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/operateStrategy/addOrUpdate"

        payload = {
            "id": 83,
            "strategyCode": "",
            "strategyName": "常规策略1",
            "bussType": 1,
            "versionType": 1,
            "canvasIdList": [],
            "taskList": [{
                "canvasId": 0,
                "taskId": 35531,
                "taskName": "0705"
            }],
            "triggerMethod": 2,
            "triggerCondition": {
                "addCallTimesFlag": 0,
                "addCallTimesPeriod": ""
            },
            "reachTypeList": [1],
            "strategyStatus": 0,
            "strategyType": 1,
            "updateBy": "a759fd1d9ffb4a2a9e9b860fbcacfe22",
            "updateByName": "王厚轩",
            "updateDate": "2024-08-21 10:10:51",
            "createBy": "a759fd1d9ffb4a2a9e9b860fbcacfe22",
            "createByName": "王厚轩",
            "createDate": "2024-08-21 10:10:50",
            "smsTemplate": "",
            "phoneSplitRule": {},
            "smsSplitRule": {},
            "localLimitCheck": "Y",
            "taskIdList": ["35531"],
            "groupIdList": []
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()


    def selectValidShuntRules(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/tmkhmc/api/selectValidShuntRules"

        payload = {
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()