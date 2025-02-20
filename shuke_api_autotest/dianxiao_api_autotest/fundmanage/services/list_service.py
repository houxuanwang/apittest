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


class List:
    """名单管理"""

    def getlist(self):
        """查询拆分列表1.0列表"""
        url = SIT_HOST + "/backend/sync/syncRosterStateNew/getList"
        payload = {
            "batchName": "",
            "tmkStatus": "",
            "projectCode": "",
            # 项目：促完件1.0-自动化
            "projectId": "180daa74425846d996dea45f5b499e31",
            "dateRange": ["2024-06-17T05:45:21.547Z", "2024-06-17T05:45:21.547Z"],
            "pageNo": 1,
            "pageSize": 10,
            "datetimeStart": "2024-06-17 13:45:21",
            "datetimeEnd": "2024-06-17 23:59:59"
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def fileupload(self):
        """上传名单"""
        url = SIT_HOST + "/backend/sync/syncRosterStateNew/file/upload"
        # 项目：促完件1.0-自动化
        #       payload = {'projectId': '180daa74425846d996dea45f5b499e31',
        #                  'title': ''}
        #       files = [
        #          ('roster_file', (
        #               'user_list.csv', open('dianxiao_api_autotest/fundmanage/testdata/user_list.csv', 'rb'),
        #               'application/octet-stream'))
        #       ]
        #       R.session.headers['Content-Type'] = 'multipart/form-data; boundary=52ff6387b11b45082e114f3862402f0e'

        #        res = R(url=url, method='POST', data=payload, files=files)
        #        R.session.headers['Content-Type'] = 'application/json;charset=UTF-8'
        #        res = uploadfile(SIT_HOST, "/backend/sync/syncRosterStateNew/file/upload", 'user_list.csv', all_filename="dianxiao_api_autotest/fundmanage/testdata/user_list.csv")

        m = MultipartEncoder(
            fields={
                'projectId': '180daa74425846d996dea45f5b499e31',
                'title': '',  # 字段2
                'roster_file': (
                    'user_list.csv', open('dianxiao_api_autotest/fundmanage/testdata/user_list.csv', 'rb'),
                    'multipart/form-data')
            }
        )

        res = R(url=url, method='POST', data=m, headers={'Content-Type': m.content_type})
        print(res.text)

        return res.json()

    def spilt(self):
        """手动拆分"""
        url = SIT_HOST + "/backend/sync/syncRosterStateNew/split"
        # 默认全随机、人工、拆至促完件1.0-自动化
        # 查名单id
        url1 = "https://zkxqw-test.360-jr.com/chaifensql"
        payload = {
            "sql": "select id FROM `sync_roster_state` where project_code='P576'  and create_date>CURDATE() order by datetime desc "
                   "limit 1;"}
        mingdanid = requests.request("POST", url1, json=payload, verify=False).json()[0]['id']
        payload = {"sql": "select batch_name FROM `sync_roster_state` where project_code='P576'  and "
                          "create_date>CURDATE() order by datetime desc  limit 1;"}
        mingdanbatchNumber = requests.request("POST", url1, json=payload, verify=False).json()[0]['batch_name']
        payload = {
            "id": mingdanid,
            # whx
            "adminId": "a759fd1d9ffb4a2a9e9b860fbcacfe22",
            "batchNumber": mingdanbatchNumber,
            "productType": "12",
            "splitType": "1",
            "ruleB": "0",
            "allSplitSize": {
                "total": 1,
                "totalB": 0,
                "totalA": 0
            },
            "total": 1,
            "productIdListByDialMode": [
            ],
            "productIdList": [
            ],
            "lstProjects": [{
                # 拆分至促完件1.0-自动化
                "productId": "180daa74425846d996dea45f5b499e31",
                "mode": 1,
                "total": "1",
                "groupA": "1",
                "groupB": 0,
                "adjustFlag": "N",
                "rosterLevel": "",
                "ruleARate": "20",
                "ruleBRate": "1"
            }],
            "lstRules": [],
            "adjustFlag": "N",
            "rosterLevel": "",
            "splitDetailNo": "4fd939ec-8a95-4008-acc2-290f75d4edb7",
            "splitOrderBy": "byAmount"

        }
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def spilt1(self):
        """手动拆分"""
        url = SIT_HOST + "/backend/sync/syncRosterStateNew/split"
        # 默认全随机、人工、拆至促完件1.0-自动化
        # 查名单id
        url1 = "https://zkxqw-test.360-jr.com/chaifensql"
        payload = {
            "sql": "select id FROM `sync_roster_state` where project_code='P576'  and create_date>CURDATE() order by datetime desc "
                   "limit 1;"}
        mingdanid = requests.request("POST", url1, json=payload, verify=False).json()[0]['id']
        payload = {"sql": "select batch_name FROM `sync_roster_state` where project_code='P576'  and "
                          "create_date>CURDATE() order by datetime desc  limit 1;"}
        mingdanbatchNumber = requests.request("POST", url1, json=payload, verify=False).json()[0]['batch_name']
        payload = {
            "id": mingdanid,
            # whx
            "adminId": "a759fd1d9ffb4a2a9e9b860fbcacfe22",
            "batchNumber": mingdanbatchNumber,
            "productType": "12",
            "splitType": "1",
            "ruleB": "0",
            "allSplitSize": {
                "total": 1,
                "totalB": 0,
                "totalA": 0
            },
            "total": 1,
            "productIdListByDialMode": [
            ],
            "productIdList": [
            ],
            "lstProjects": [{
                # 拆分至促完件1.0-自动化
                "productId": "180daa74425846d996dea45f5b499e31",
                "mode": 1,
                "total": "1",
                "groupA": "1",
                "groupB": 0,
                "adjustFlag": "N",
                "rosterLevel": "",
                "ruleARate": "20",
                "ruleBRate": "1"
            }],
            "lstRules": [],
            "adjustFlag": "N",
            "rosterLevel": "",
            "splitDetailNo": "4fd939ec-8a95-4008-acc2-290f75d4edb7",
            "splitOrderBy": "byAmount"

        }
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def allotAjax(self):
        """名单分配是否锁定中"""
        url = SIT_HOST + "/backend/roster/allot/allotAjax"
        payload = 'id='

        url1 = "https://zkxqw-test.360-jr.com/tmksql"
        payload1 = {
            "sql": "select id FROM `tmk_roster` where project_id='180daa74425846d996dea45f5b499e31'  and create_date>CURDATE()  order by create_date desc "
                   "limit 1;"}
        mingdanid = requests.request("POST", url1, json=payload1, verify=False).json()[0]['id']

        payload = payload + mingdanid
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def distributionPreservation(self):
        """名单分配是否锁定中"""
        url = SIT_HOST + "/backend/roster/distributionPreservation"
        payload = 'id='

        url1 = "https://zkxqw-test.360-jr.com/tmksql"
        payload = {
            "sql": "select number FROM `tmk_roster` where project_id='180daa74425846d996dea45f5b499e31'  and create_date>CURDATE()  order by create_date desc "
                   "limit 1;"}
        mingdannumber = requests.request("POST", url1, json=payload, verify=False).json()[0]['number']

        payload1 = {
            "sql": "select id FROM `tmk_roster` where project_id='180daa74425846d996dea45f5b499e31'  and create_date>CURDATE()  order by create_date desc "
                   "limit 1;"}
        mingdanid = requests.request("POST", url1, json=payload1, verify=False).json()[0]['id']

        payload2 = {
            "sql": "select title FROM `tmk_roster` where project_id='180daa74425846d996dea45f5b499e31'  and create_date>CURDATE()  order by create_date desc "
                   "limit 1;"}
        mingdantitle = requests.request("POST", url1, json=payload2, verify=False).json()[0]['title']

        payload3 = {
            "sql": "select create_date FROM `tmk_roster` where project_id='180daa74425846d996dea45f5b499e31'  and create_date>CURDATE()  order by create_date desc "
                   "limit 1;"}
        mingdancreate_date = requests.request("POST", url1, json=payload3, verify=False).json()[0]['create_date']
        mingdantitle = '[促完件1.0-自动化]' + mingdannumber
        payload = {
            "id": mingdanid,
            "rosterName": mingdantitle,
            "batchName": mingdannumber,
            "createDate": mingdancreate_date,
            "allocationType": "0",
            "allocationTypeName": "按实际可用额度",
            "pushType": "1",
            "pushObject": [{
                "id": "a759fd1d9ffb4a2a9e9b860fbcacfe22",
                "percent": 100,
                "userName": "王厚轩",
                "loginNo": "wanghouxuan"
            }],
            "total": "1",
            "projectTitle": "促完件1.0-自动化",
            "projectCode": "P576",
            "objectIds": "a759fd1d9ffb4a2a9e9b860fbcacfe22",
            "group": "",
            "groupIds": [],
            "preAllotStatus": "0",
            "effectiveDay": "12",
            "dayCount": "",
            "allotQwType": "0",
            "rosterLevel": "",
            "assignType": "",
            "benchmarkingProject": "0",
            "list": [{
                "userId": "a759fd1d9ffb4a2a9e9b860fbcacfe22",
                "proportion": 100,
                "total": 1,
                "loginNo": "wanghouxuan",
                "userName": "王厚轩"
            }]
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()
