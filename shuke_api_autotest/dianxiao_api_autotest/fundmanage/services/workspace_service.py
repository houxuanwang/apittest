import json
import logging
import random

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform

from common.api_uploadfile import uploadfile
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta
from requests_toolbelt import MultipartEncoder

logger = logging.getLogger(__name__)


class Workspace:
    """工作台"""

    def pendinglist(self):
        """查询名单库数据"""
        url = SIT_HOST + "/backend/roster/task/pending-list"
        payload = payload = ('pageNo=1&pageSize=30&projectType=&outCallStrategyId=&modelType=0&note=&mobile=&custNo'
                             '=&userNo=UR6524057293519327233&custName=&applState=&zhifuLoanState=&wlhState=&qwStatus'
                             '=&projectIdListStr=&fourthStrategy=&dateRange=&userId=a759fd1d9ffb4a2a9e9b860fbcacfe22'
                             '&groupId=&trackStr=&antiFraudScore=&tags=&serveTag=&groupTypes=&label=&trackDateType=2'
                             '&trackDateRange=&finishedStatus=&crossSaleTable=false&crossSaleId=&completionModelScore'
                             '=&starCountValue=&scoreStart=&scoreEnd=&scoreStartOp=&scoreEndOp=&apiChannelFlag'
                             '=&clueSubmit=')
        res = R(url=url, method='POST', json=payload)
        return res.json()

