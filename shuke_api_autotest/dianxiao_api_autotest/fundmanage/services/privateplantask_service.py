import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)



class privatePlanTask:
    """个人销售任务
    """
    def queryPrivatePlanTaskList1(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/tmkhmc/privatePlanTask/queryPrivatePlanTaskList"

        payload = {
            "bussType": "1",
            "taskType": "",
            "taskStatus": "1",
            "taskName": "",
            "taskCategory": "",
            "outboundType": "",
            "pageNum": 1,
            "pageSize": 20
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()


    def queryPrivatePlanTaskList2(self):
        """查询列表-促完件"""
        url = SIT_HOST + "/backend/tmkhmc/privatePlanTask/queryPrivatePlanTaskList"

        payload = {
            "bussType": "2",
            "taskType": "",
            "taskStatus": "1",
            "taskName": "",
            "taskCategory": "",
            "outboundType": "",
            "pageNum": 1,
            "pageSize": 20
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def selectData(self):
        """查询任务组数据"""
        url = SIT_HOST + "/backend/tmkhmc/taskGroup/selectData"

        payload = {
            "bussType": "2",
            "taskType": "",
            "taskStatus": "1",
            "taskName": "",
            "taskCategory": "",
            "outboundType": "",
            "pageNum": 1,
            "pageSize": 20
        }
        res = R(url=url, method='GET')
        return res.json()
