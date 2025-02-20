import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)


class User:
    """客户信息"""

    def getNamePinyin(self):
        """获取客户姓名拼音"""
        url = SIT_HOST + "/backend/pinyin/getNamePinyin"
        payload = {'name': '金融'}
        # a= R.session.headers['Content-Type']
        # R.session.headers['Content-Type']='application/x-www-form-urlencoded'
        res = R(url=url, method='POST', data=payload)
        # R.session.headers['Content-Type']=a

        print("打印headers")
        print(R.session.headers)
        return res.json()

    def reportSeatStatus(self):
        """切换坐席状态"""
        url = SIT_HOST + "/backend/seatStatusMonitor/reportSeatStatus"
        payload = {'status': 'idle'}
        # a= R.session.headers['Content-Type']
        # R.session.headers['Content-Type']='application/x-www-form-urlencoded'
        res = R(url=url, method='POST', data=payload)
        # R.session.headers['Content-Type']=a
        #
        # print("打印headers")
        # print(R.session.headers)
        return res.json()


    def newIndexData(self):
        """客户详情页用户信息"""
        url = SIT_HOST + "/backend/crm/newIndexData"
        params = 'jid=4970035&projectType=P576&rosterNumber=202408081413439043&rosterType=undefined'
        res = R(url=url, method='POST', params=params)
        return res.json()

    def customerInfoOther(self):
        """客户详情页用户其他信息"""
        url = SIT_HOST + "/backend/crm/customerInfoOther"
        data = {
            'rosterId':'',
            'score': 0.00,
            'jid': 4970035,
            'userNo': 'UR6524057293519327233',
            'custNo': 'CT6524058163501862913',
            'createDateStart': '',
            'rosterSource':'',
            'tmktic_version':''
        }
        res = R(url=url, method='POST', data=data)
        return res.json()

    def queryProductAdjustFeeRate(self):
        """客户详情页用户借条相关信息"""
        url = SIT_HOST + "/backend/crm/queryProductAdjustFeeRate"
        json = {"custNo":"CT6524058163501862913","contractNo":"6524059359427956737","userNo":"UR6524057293519327233","bigProjectCode":"","bigAvailableAmt":"","availableAmt":"100000.01"}

        res = R(url=url, method='POST', json=json)
        return res.json()