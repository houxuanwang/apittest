import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)


class coupon:
    """Coupon
    """

    def check_available_coupon(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/coupon/checkAvailableCoupon"

        payload = {
            "id": "83fb6cb7003c4318bac6ba0f6bf9a9b9",
            "projectList": "P576",
            "rosterNumbers": "202408081413439043",
            "userNo": "UR6550854174421286913",
            "createDate": "2024-08-08 14:13:45",
            "custNo": "CT6550854205123592192",
            "contractNo": "6550855119494451200"
        }
        logger.info(f"Sending request to {url} with payload {payload}")
        res = R(url=url, method='POST', json=payload)
        logger.info(f"Received response: {res.json()}")
        return res.json()

    def check_available_qw(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/coupon/checkAvailableQw"

        payload = {
            "projectList": "P576",
            "rosterJid": 4970035,
            "userNo": "UR6550854174421286913"
        }
        logger.info(f"Sending request to {url} with payload {payload}")
        res = R(url=url, method='POST', json=payload)
        logger.info(f"Received response: {res.json()}")
        return res.json()

    def check_user_coupon_count(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/coupon/checkUserCouponCount"

        payload = {
            "projectType": "P576",
            "userNo": "UR6550854174421286913",
            "createDate": "2024-08-08 14:13:45"
        }
        logger.info(f"Sending request to {url} with payload {payload}")
        res = R(url=url, method='POST', json=payload)
        logger.info(f"Received response: {res.json()}")
        return res.json()

    def _get_user_coupon_record(self, status, used_flag):
        """私有方法，用于获取用户优惠券记录"""
        url = SIT_HOST + "/backend/coupon/getUserCouponRecord"

        payload = f'status={status}&usedFlag={used_flag}&userNo=UR6550854174421286913'
        logger.info(f"Sending request to {url} with payload {payload}")
        res = R(url=url, method='POST', params=payload)
        logger.info(f"Received response: {res.json()}")
        return res.json()

    def get_user_coupon_record1(self):
        """查询列表-促动支"""
        return self._get_user_coupon_record(status=0, used_flag='N')

    def get_user_coupon_record2(self):
        """查询列表-促动支"""
        return self._get_user_coupon_record(status=0, used_flag='Y')