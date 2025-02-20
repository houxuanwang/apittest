import json
import logging
from requests_toolbelt.multipart.encoder import MultipartEncoder
import platform
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST
import time
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)


class crm:
    """CRM
    """

    def customerloan(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/crm/customer-loan"

        payload = 'id=3d7e9a2849ee472ea3e57de53afa24e1&jid=5018529&createDateStart=&createDateEnd=&loanStateFilter=&tmktic_version='
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def customersmeloan(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/crm/customer-smeloan"

        payload = 'id=3d7e9a2849ee472ea3e57de53afa24e1&jid=5018529'
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def customeryingjiloan(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/crm/customer-yingJiloan"

        payload = 'id=3d7e9a2849ee472ea3e57de53afa24e1&jid=5018529'
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def customerplusloan(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/crm/customer-plusloan"

        payload = 'id=3d7e9a2849ee472ea3e57de53afa24e1&jid=5018529'
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def queryCustomerZhiXinAuxiliary(self):
        """查询列表-促动支"""
        url = SIT_HOST + "/backend/crm/queryCustomerZhiXinAuxiliary"

        payload = 'userNo=UR6550854174421286913'
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def customerInfoOther(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/crm/customerInfoOther"

        payload = 'rosterId=&score=0.0&jid=4970035&userNo=UR6524057293519327233&custNo=CT6524058163501862913&createDateStart=&rosterSource=&tmktic_version='
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def queryProductAdjustFeeRate(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/crm/queryProductAdjustFeeRate"

        payload = {"custNo": "CT6524058163501862913", "contractNo": "6524059359427956737",
                   "userNo": "UR6524057293519327233", "bigProjectCode": "", "bigAvailableAmt": "",
                   "availableAmt": "100000.01"}
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def creditquery(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tax/credit/query"

        payload = 'userNo=UR6550854174421286913'
        res = R(url=url, method='GET', params=payload)
        return res.json()

    def codeList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/sys/messageTemplate/codeList"

        payload = 'projectId=180daa74425846d996dea45f5b499e31&userNo=UR6550854174421286913'
        res = R(url=url, method='POST', data=payload)
        return res.json()

    def getTaskList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmkhmc/taskList/getTaskList"

        payload = 'userNo=UR6550854174421286913'
        res = R(url=url, method='GET')
        return res.json()

    def queryRobotListByProjectInfo(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/robotMapping/queryRobotListByProjectInfo"

        payload = {"businessType": "projectFinish", "bussScene": "0"}
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def getUserByName(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/sys/user/getUserByName"

        payload = 'nameOrAccount=&allFlag=1'
        res = R(url=url, method='GET', params=payload)
        return res.json()

    def isShowCancelControlButton(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/crm/isShowCancelControlButton"

        payload = {
            "projectType": "P576",
            "controlCode": "正常",
            "userNo": "UR6550854174421286913"
        }
        res = R(url=url, method='POST', json=payload)
        return res.json()


    def qryUserCancelControlRecord(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/crm/qryUserCancelControlRecord"

        payload = {
	"userNo": "UR6550854174421286913"
}
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def existsC7C8Flow(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/crm/existsC7C8Flow"

        payload = {
	"userNo": "UR6550854174421286913"
}
        res = R(url=url, method='POST', json=payload)
        return res.json()

    def customerhistoryAmt(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/crm/customer-historyAmt"

        payload = 'custNo=CT6550854205123592192&productCode=360JIETIAO'
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def customernewRegHistList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/crm/customer-newRegHistList"

        payload = 'userNo=UR6550854174421286913&productCode=360JIETIAO&projectId=180daa74425846d996dea45f5b499e31'
        res = R(url=url, method='POST', params=payload)
        return res.json()


    def addActuationModelOperateStep(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/actuationModelOperateStep/addActuationModelOperateStep"

        payload = {
	"category": 1,
	"eventStep": 5,
	"status": 0
}
        res = R(url=url, method='POST', json=payload)
        return res.json()


    def selectTmkLineRuleByDashboard(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/line/routing/selectTmkLineRuleByDashboard"

        payload ='lineType=1'
        res = R(url=url, method='POST', params=payload)
        return res.json()

    def alarmevent(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/scene/alarm/event?target=&from=0"

        res = R(url=url, method='GET')
        return res.json()


    def getPerceptionCallSwitch(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmkhmc/perceptionCall/getPerceptionCallSwitch"

        res = R(url=url, method='POST')
        return res.json()


    def selectValidShuntRules(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmkhmc/api/selectValidShuntRules"
        payload={}
        res = R(url=url, method='POST',json=payload)
        return res.json()


    def treeData(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/sys/office/treeData"
        payload={}
        res = R(url=url, method='POST')
        return res

    def unreadCount(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/msg/push/unreadCount"
        payload={}
        res = R(url=url, method='POST')
        return res.json()


    def selectTmkMsgPushManger(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/msg/push/selectTmkMsgPushManger"
        payload={}
        res = R(url=url, method='POST')
        return res.json()

    def typeList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/msg/push/typeList"
        payload='pageNo=1&pageSize=20&orderBy='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def getMsgList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/msg/push/getMsgList"
        payload='pageNo=1&pageSize=20&orderBy=&userId=&msgTitle=&msgTypeId=&operator=&dateRange%5B0%5D=Tue+Aug+20+2024+00%3A00%3A00+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&dateRange%5B1%5D=Wed+Sep+18+2024+00%3A00%3A00+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&beginTime=2024-08-20+00%3A00%3A00&endTime=2024-09-18+23%3A59%3A59'
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def getMsgByUserId(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/msg/push/getMsgByUserId"
        payload="pageNo=1&pageSize=20&orderBy=&isRead='0'&sendLoginName=&userNo="
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def userList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/msg/push/userList"
        payload="pageNo=1&pageSize=20&orderBy=&isRead='0'&sendLoginName=&userNo="
        res = R(url=url, method='POST')
        return res.json()

    def page(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/scene/page"
        payload={
	"pageNum": 1,
	"pageSize": 20,
	"gs": "",
	"ms": ""
}
        res = R(url=url, method='POST',json=payload)
        return res.json()


    def junior1(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/scene/junior"
        payload='type=1&target='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def junior2(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/scene/junior"
        payload='type=3&target=76527977495a4103b77fa7b8e1bf3148'
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def senior1(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/scene/junior"
        payload='type=1&target='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def senior2(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/scene/junior"
        payload='type=3&target=76527977495a4103b77fa7b8e1bf3148'
        res = R(url=url, method='POST',params=payload)
        return res.json()



    def getGroupUsers(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/group/getGroupUsers"
        payload='type=3&target=76527977495a4103b77fa7b8e1bf3148'
        res = R(url=url, method='POST')
        return res.json()


    def getGroupById(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/group/getGroupById"
        payload='type=3&target=76527977495a4103b77fa7b8e1bf3148'
        res = R(url=url, method='POST')
        return res.json()

    def list(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/group/list"
        payload='pageNo=1&pageSize=20&userName=&memberName=&gId=&userId='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def memberIndex(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/group/memberIndex"
        payload='pageNo=1&pageSize=20&userName=&memberName=&gId=116&userId=&groupName=1582182242610'
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def list1(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/customerBoundIvrSummaryRecord/list"
        payload='startDate=&endDate=&operateUsers=&userNo=&pageNo=0&pageSize=10'
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def list2(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/customerSummaryLevel/list"
        payload='startDate=&endDate=&operateUsers=&userNo=&pageNo=0&pageSize=10'
        res = R(url=url, method='POST')
        return res.json()


    def newSearch(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/tmkOutCallHistory/newSearch"
        payload={
	"userNo": "UR6550854174421286913",
	"mobile": "",
	"callId": "",
	"followUserId": "20230814",
	"callState": "dealing",
	"outboundType": "",
	"createDate": ["2024-09-07", "2024-09-13"],
	"pageNo": 1,
	"pageSize": 20,
	"callStartTime": "2024-09-07",
	"callEndTime": "2024-09-13"
}
        res = R(url=url, method='POST',json=payload)
        return res.json()


    def getData(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/tmkProjectOutCallHistory/getData"
        payload='paramType=&paramValue=&disDateRange%5B%5D=2024-09-11&disDateRange%5B%5D=2024-09-18&source=&interceptStatus=&interceptReason=&voicveFlag=&outboundType=&seatId=wanghouxuan&projectId=180daa74425846d996dea45f5b499e31&startTime=2024-09-11+08%3A00%3A00&endTime=2024-09-18+08%3A00%3A00'
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def mobileChangequeryList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/mobileChange/queryList"
        payload = {"userNo":"","updateDate":None,"createBy":"","reason":"","pageNum":1,"pageSize":20,"beginTime":None,"endTime":None}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def queryChangeUserNoRecord(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/change/userNo/queryChangeUserNoRecord"
        payload = {"userNo":"UR6550854174421286913"}
        res = R(url=url, method='POST',json=payload)
        return res.json()


    def tmkOutCallHistorygetData(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/tmkOutCallHistory/getData"
        payload = 'paramType=1&paramValue=UR6550854174421286913&disDateRange%5B%5D=2024-09-04&disDateRange%5B%5D=2024-09-18&source=&interceptStatus=&interceptReason=&voicveFlag=&outboundType=&startTime=2024-09-04+08%3A00%3A00&endTime=2024-09-18+08%3A00%3A00'
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def rosterCustomerPrelist(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/rosterCustomerPre/list"
        payload ='pageNo=1&pageSize=20&timFrame=&rosterNumber=&projectId=&userNo=UR6514985404628992001&custNo=&preSeatId=&total=0&openLoading=false&createDateStart=&createDateEnd='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def queryCtpSmsHistoryList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/smsManager/queryCtpSmsHistoryList"
        payload ={"createTime":["2024-06-30T16:00:00.000Z","2024-08-30T16:00:00.000Z"],"startDateStr":"2024-07-01 00:00:00","endDateStr":"2024-08-31 23:59:59","userNo":"","mobileNo":"18916076589"}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def smsBlackStatus(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/smsManager/smsBlackStatus"
        payload ={"createTime":["2024-06-30T16:00:00.000Z","2024-08-30T16:00:00.000Z"],"startDateStr":"2024-07-01 00:00:00","endDateStr":"2024-08-31 23:59:59","userNo":"","mobileNo":"18916076589"}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def queryList1(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/autoAddBlackRule/queryList"
        payload = 'pageNo=1&pageSize=20&bussType=&thirdStrategy=&projectId='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def queryList2(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/autoAddBlackRule/queryList"
        payload = 'pageNo=1&pageSize=20&bussType=projectFinish&thirdStrategy=&projectId='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def queryList3(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/autoAddBlackRule/queryList"
        payload = 'pageNo=1&pageSize=20&bussType=projectNode&thirdStrategy=&projectId='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def queryList4(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/autoAddBlackRule/queryList"
        payload = 'pageNo=1&pageSize=20&bussType=projectIVR&thirdStrategy=&projectId='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def getProjectByThirdStrategy(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/project/getProjectByThirdStrategy"
        payload = {
	"bussType": "",
	"thirdStrategyList": []
}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def accuratesearch(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/accurate/search"
        payload = 'loading=false&mobile=18916076589'
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def getCustomerCallHistoryList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/accurate/getCustomerCallHistoryList"
        payload = 'pageNo=1&pageSize=20&platform=1&mobile=18916076589&custNo=&userNo=&seatNo=&name=&timeRange%5B%5D=2024-03-23&timeRange%5B%5D=2024-09-19&beginTime=2024-03-23+00%3A00%3A00&endTime=2024-09-19+23%3A59%3A5'
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def abnormalFeedbacklist(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/abnormalFeedback/list"
        payload = 'pageNo=1&pageSize=10'
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def abnormalFeedbackstatistic(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/abnormalFeedback/statistic"
        payload = {"pageNo":1,"pageSize":10}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def fileManagerlist(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/fileManager/list"
        payload = 'pageNo=1&pageSize=10'
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def aiTermlist(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/helper/aiTerm/list?pageNo=1&pageSize=20"
        payload = 'pageNo=1&pageSize=10'
        res = R(url=url, method='GET')
        return res.json()

    def nodelist(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/helper/node/list?nodeId=&sceneId=&status=&pageNo=1&pageSize=20"
        payload = 'pageNo=1&pageSize=10'
        res = R(url=url, method='GET')
        return res.json()

    def sceneslist(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/helper/scenes/list?sceneId=&businessType=&scenePriority=&pageNo=1&pageSize=20"
        payload = 'pageNo=1&pageSize=10'
        res = R(url=url, method='GET')
        return res.json()

    def qualitylist(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/quality/list"
        payload = 'pageNo=1&pageSize=30&orderBy=&qualityDaterange%5B0%5D=Fri+Sep+13+2024+17%3A37%3A50+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&qualityDaterange%5B1%5D=Thu+Sep+19+2024+17%3A37%3A50+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&qualityRuleCategory=&qualitySignType=&groupId=&loginName=&userId=&userNo=&beginDate=2024-09-13+00%3A00%3A00&endDate=2024-09-19+23%3A59%3A59'
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def qualityreceiptList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/quality/receiptList"
        payload = 'pageNo=1&pageSize=30&orderBy=&daterange%5B0%5D=Fri+Sep+13+2024+17%3A38%3A05+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&daterange%5B1%5D=Thu+Sep+19+2024+17%3A38%3A05+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&userNo=&emotionLabel=&userId=a759fd1d9ffb4a2a9e9b860fbcacfe22&pushState=0&status=0&beginPushTime=2024-09-13&endPushTime=2024-09-19'
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def tmkRosterApplyAmtlist(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmk/tmkRosterApplyAmt/list"
        payload = 'pageNo=1&pageSize=30&orderBy=&applyDateRange%5B0%5D=Fri+Sep+13+2024+17%3A44%3A09+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&applyDateRange%5B1%5D=Thu+Sep+19+2024+17%3A44%3A09+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&applyType=&userNo=&applyId=&applyGroup=&applyStatus=&followStatus=&applyMethod=&channelType=&applyBeginDate=2024-09-13+00%3A00%3A00&applyEndDate=2024-09-19+23%3A59%3A59'
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def querySimpleInfoCanvasByRight(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmkrseapi/canvas/querySimpleInfoCanvasByRight"
        payload = {}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def querySimpleList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmkrseapi/concurrencyGroup/querySimpleList"
        payload = {}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def queryConcurrencyCanvasPageList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmkrseapi/concurrencyGroup/queryConcurrencyCanvasPageList"
        payload = {
	"id": "",
	"canvasId": "",
	"pageNum": 1,
	"pageSize": 10
}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def queryConcurrencyGroupPageList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/tmkrseapi/concurrencyGroup/queryConcurrencyGroupPageList"
        payload = {
	"id": "",
	"canvasId": "",
	"pageNum": 1,
	"pageSize": 10
}
        res = R(url=url, method='POST',json=payload)
        return res.json()

    def crosslistData(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/roster/cross/listData"
        payload = 'pageNo=1&pageSize=30&orderBy=&custName=&userNo=&dateTime=&createDateStart=&createDateEnd=&followStatus=&delFlag=&userId=&beUserId=&createUser=&configType=&operationType=&configName=&projectName=&crossSaleConfigType='
        res = R(url=url, method='POST',params=payload)
        return res.json()

    def xiexiaopeizhigetUserByName(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/sys/user/getUserByName?source=xiexiaopeizhi&nameOrAccount="
        res = R(url=url, method='GET')
        return res.json()


    def getManualConfigList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/manual/crossSale/getManualConfigList"
        payload = 'createDateStart=&createDateEnd=&ownStatus=&pageNo=1&pageSize=20&configName=&configType=&runType=&createById=&projectId='
        res = R(url=url, method='POST',params=payload)
        return res.json()


    def configList(self):
        """查询校验客户其他信息"""
        url = SIT_HOST + "/backend/roster/cross/configList"
        payload = 'createDateStart=&createDateEnd=&crossStatus=&pageNo=1&pageSize=20&configName=&configType=&operationType=&crossSaleConfigType=&runType='
        res = R(url=url, method='POST',params=payload)
        return res.json()