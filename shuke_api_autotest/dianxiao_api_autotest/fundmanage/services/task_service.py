import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)


class Task:
    """借条任务"""

    def gettaskgrouplist(self):
        """获取组别管理数据"""
        url = SIT_HOST + "/backend/roster/task/getTaskGroupList"
        res = R(url=url, method='POST')
        return res.json()

    def getcrosssalelist(self):
        """获取所有坐席"""
        url = SIT_HOST + "/backend/roster/task/getCrossSaleList"
        res = R(url=url, method='POST')
        return res.json()

    def gettmkscreenfilterlist(self):
        """查询条件过滤器"""
        url = SIT_HOST + "/backend/tmk/tmkScreenFilter/getTmkScreenFilterList"
        res = R(url=url, method='POST')
        return res.json()

    def getTaskHandleUserList(self):
        """列表处理人数据范围"""
        url = SIT_HOST + "/backend/roster/task/getTaskHandleUserList?groupId=&filter=l"
        res = R(url=url, method='POST')
        return res.json()

    def pendinglist(self):
        """顶部搜索栏查询"""
        url = SIT_HOST + "/backend/roster/task/pending-list"
        start = (date.today() + timedelta(days=-300)).strftime("%Y-%m-%d")
        start1 = (date.today() + timedelta(days=-300)).strftime("%Y-%m-%d") + " 00:00:00"
        end = (date.today()).strftime("%Y-%m-%d")
        end1 = (date.today()).strftime("%Y-%m-%d") + " 23:59:59"
        payload = '?pageNo=1&pageSize=30&projectType=&outCallStrategyId=&modelType=0&note=&mobile=&custNo=&userNo' \
                  '=&custName=&applState=&wlhState=&projectIdListStr=&dateRange%5B%5D=' + start + '&dateRange%5B%5D' \
                                                                                                  '=' + end + '&userId=&groupId=&trackStr=&antiFraudScore=&tags=&groupTypes=&label=&trackDateType' \
                                                                                                              '=&trackDateRange%5B%5D=' + start + '&trackDateRange%5B%5D=' + end + '&finishedStatus=&crossSaleTable' \
                                                                                                                                                                                   '=false&crossSaleId=&completionModelScore=&starCountValue=&scoreStart=&scoreEnd=&scoreStartOp' \
                                                                                                                                                                                   '=&scoreEndOp=&createDateStart=' + start1 + '&createDateEnd=' + end1 + '&trackDateStart=' + start + '&trackDateEnd=' + end
        url = url + payload
        res = R(url=url, method='POST')
        return res.json()

    def codeList(self):
        """获取短信模板"""
        url = SIT_HOST + "/backend/sys/messageTemplate/codeList"
        res = R(url=url, method='POST')
        return res.json()

    def getCouponList(self, projectList="itceshi02", rosterNumbers="202109282039542", userNo="UR5957615431941443584",
                      createDate="2021-09-28 20:40:12"):
        """获取优惠券模板"""
        url = SIT_HOST + "/backend/coupon/getCouponList"
        payload = {
            "projectList": projectList,
            "rosterNumbers": rosterNumbers,
            "userNo": userNo,
            "createDate": createDate
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def sendMsg(self):
        """发送短信"""
        url = SIT_HOST + "/backend/sys/messageTemplate/sendMsg"
        params = 'noticeType=1&id=521f417854f2485fb20e2d6263386228&content=您已被选为优质客户！360借条借您最高20w，可分12' \
                 '期慢慢还，快来查看額度吧，url。&couponId=&remainderCount' \
                 '=&remainderDay=&couponContent=&rosterCustomerId=1d85042ad9374b97b3858b7e1a569ee4&rosterNumber' \
                 '=202110091107035&mobile=0677a13ec55a5600f01803712dd074f6&loading=true&buttonTxt=发送中... '
        res = R(url=url, method='POST', params=params)
        return res.json()

    def checkRule(self):
        """拨打电话"""
        url = SIT_HOST + "/backend/ob/obLimit/checkRule"
        params = 'rosterNumber=202110091107035&mobile=0677a13ec55a5600f01803712dd074f6&userId=1&custNo=&customerId' \
                 '=1d85042ad9374b97b3858b7e1a569ee4&platform=1&lineCode=0&hmcId= '
        res = R(url=url, method='POST', params=params)
        return res.json()

    def index(self):
        """客户按钮"""
        url = SIT_HOST + "/backend/crm/index"
        params = 'projectType=20211009&jid=395369&rosterType=undefined&rosterNumber=202110091107035'
        res = R(url=url, method='GET', params=params)
        return res

    def regHistList(self):
        """注册列表"""
        url = SIT_HOST + "/backend/crm/customer-regHistList"
        params = 'userNo=UR433454344545'
        res = R(url=url, method='GET', params=params)
        return res.json()

    def credit(self):
        """授信列表查询"""
        url = SIT_HOST + "/backend/crm/customer-credit"
        params = 'id=1d85042ad9374b97b3858b7e1a569ee4&jid=395369&productCode=&applState=&contractStatus=&usedAmt=0.00'
        res = R(url=url, method='POST', params=params)
        return res.json()

    def loan(self):
        """借款借据-查询"""
        url = SIT_HOST + "/backend/crm/customer-loan"
        start = (date.today() + timedelta(days=-180)).strftime("%Y-%m-%d") + " 00:00:00"
        end = (date.today()).strftime("%Y-%m-%d") + " 23:59:59"
        params = 'id=a26828828f7b4e7e8015bd4389666d35&jid=395310&createDateStart=' + start + '&createDateEnd=' + end + '&loanStateFilter='
        res = R(url=url, method='POST', params=params)
        return res.json()

    def callRecordhistory(self):
        """客户详情页-通话记录"""
        url = SIT_HOST + "/backend/humanAndRobot/callRecordhistory"
        params = 'id=1d85042ad9374b97b3858b7e1a569ee4'
        res = R(url=url, method='GET', params=params)
        return res.json()

    def historySms(self):
        """历史短信"""
        url = SIT_HOST + "/backend/crm/customer-historySms"
        start = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
        end = (date.today()).strftime("%Y-%m-%d")
        params = 'pageNo=1&pageSize=10&id=a26828828f7b4e7e8015bd4389666d35&jid=395310&mobileSearch' \
                 '=9d6eba28184fdd76316b5ab9d04458b6&startDateStr=' + start + '&endDateStr=' + end
        res = R(url=url, method='POST', params=params)
        return res.json()

    def save(self):
        """预约跟进"""
        url = SIT_HOST + "/backend/tmk/reservation/save"
        start = (date.today()).strftime("%Y-%m-%d") + " 00:00:00"
        params = 'loading=false&dialogReminderCallVisible=true&followTime=' + start + '&note=20211009&type=NotFollowed&projectName=自动化-勿动&availableCredits=0.00&customerId=1d85042ad9374b97b3858b7e1a569ee4&mobile=0677a13ec55a5600f01803712dd074f6&custName=&userNo=UR433454344545&projectType=20211009&rosterNumber=202110091107035'
        res = R(url=url, method='POST', params=params)
        return res.json()

    def queryPublicTaskList(self):
        """查询公共任务列表"""
        url = SIT_HOST + "/backend/tmkhmc/task/queryPublicTaskList"
        payload = {
            "bussType": "",
            "taskPriority": "",
            "taskStatus": "1",
            "taskName": "",
            "taskId": "",
            "taskCategory": "",
            "outboundType": "",
            "createBy": "",
            "taskGroupId": "",
            "ownStatus": "",
            "pageNum": 1,
            "pageSize": 20,
            "total": 0,
            "bussScene": "",
            "shuntSwitch": ""
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()


