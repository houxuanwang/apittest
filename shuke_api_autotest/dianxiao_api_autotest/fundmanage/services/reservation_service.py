"""
@Project ：shuke_api_autotest 
@File ：reservation_service.py
@Author ：陈玲玲
@Date ：2021/9/30 10:57 
"""
import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)


class Reservation:
    """
    预约管理
    """

    def reservationlist(self):
        """
        获取预约管理页面
        :return:
        """
        url = SIT_HOST + "/backend/tmk/reservation/list"
        res = R(url=url, method='GET')
        return res

    def reservationlistJson(self):
        """
        预约管理--查询
        :return:
        """
        url = SIT_HOST + "/backend/tmk/reservation/listJson"
        payload = "?pageNo=1&pageSize=20&orderBy=&dateRange=&disDateRange=&type=NotFollowed&projectName=自动化-勿动&custName="
        url = url + payload
        res = R(url=url, method='POST')
        return res.json()

    def crmindex(self):
        """
        预约管理-点击右侧客户按钮
        :return:
        """
        url = SIT_HOST + "/backend/crm/index"
        payload = "?projectType=090601&id=a26828828f7b4e7e8015bd4389666d35&rosterNumber=20210913171304222&listPageFrom=reservation"
        url = url + payload
        res = R(url=url, method='GET')
        return res

    def customercredit(self):
        """
        预约管理-客户详情页-授信列表查询
        :return:
        """
        url = SIT_HOST + "/backend/crm/customer-credit"
        params = "id=a26828828f7b4e7e8015bd4389666d35&jid=395310&productCode=&applState=&contractStatus=NNR&usedAmt=0.00"
        res = R(url=url, method='POST', params=params)
        return res.json()
