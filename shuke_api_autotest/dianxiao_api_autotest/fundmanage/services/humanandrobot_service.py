import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)



class humanAndRobot:
    """humanAndRobot
    """

    def wlhLoanCreditedInfo(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/humanAndRobot/wlhLoanCreditedInfo"

        payload ='custNo=CT6550854205123592192&userNo=UR6550854174421286913'
        res = R(url=url, method='GET', params=payload)
        return res.json()

    def zhiXinLoanList1(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/humanAndRobot/zhiXinLoanList"

        payload ='userNo=UR6550854174421286913&type=1&id=3d7e9a2849ee472ea3e57de53afa24e1'
        res = R(url=url, method='GET', params=payload)
        return res.json()


    def zhiXinLoanList2(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/humanAndRobot/zhiXinLoanList"

        payload ='userNo=UR6550854174421286913&type=0&id=3d7e9a2849ee472ea3e57de53afa24e1'
        res = R(url=url, method='GET', params=payload)
        return res.json()


    def callRecordhistory(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/humanAndRobot/callRecordhistory?id=7d79677f3229489797392dfdb93b5edc&callDateStart=2024-08-11+00:00:00&callDateEnd=2024-09-10+23:59:59&interceptReason=%E6%9C%AA%E6%8B%A6%E6%88%AA&outboundType="

        payload = {}
        res = R(url=url, method='GET', data=payload)
        return res.json()


    def getZhiXinAssistTips(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/humanAndRobot/getZhiXinAssistTips"

        payload ='userNo=UR6550854174421286913'
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def userAmtInfo(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/humanAndRobot/userAmtInfo"

        payload ='custNo=CT6550854205123592192&userNo=UR6550854174421286913&projectId=180daa74425846d996dea45f5b499e31'
        res = R(url=url, method='GET', params=payload)
        return res.json()


    def getCallWishModeRecord(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/humanAndRobot/getCallWishModeRecord"

        payload ={
	"id": "8345ff97c830459a93ac3268530c0600",
	"userNo": "UR6550854174421286913",
	"projectId": "180daa74425846d996dea45f5b499e31",
	"rosterDataId": "dce2cf29f2264ae2ab44f42dced6a5be",
	"shuntType": "0"
}
        res = R(url=url, method='POST', json=payload)
        return res.json()