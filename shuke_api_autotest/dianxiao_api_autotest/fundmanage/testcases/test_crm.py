import pytest
import requests

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.crm_service import crm


# -*- coding: UTF-8 -*-

@pytest.mark.L4
def test_customerloan():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().customerloan()
    print(res['loanList'])
    exp = 'LP6550896610539474945'
    check_values(str(res['loanList']), exp, '校验查询借条借据', cmp='in')


@pytest.mark.L4
def test_customersmeloan():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().customersmeloan()
    print(res['code'])
    exp = 1
    check_values(res['code'], exp, '校验查询借条借据')


@pytest.mark.L4
def test_customeryingjiloan():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().customeryingjiloan()
    print(res['code'])
    exp = 1
    check_values(res['code'], exp, '校验查询借条借据')


@pytest.mark.L4
def test_customerplusloan():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().customerplusloan()
    print(res['code'])
    exp = 1
    check_values(res['code'], exp, '校验查询借条借据')


@pytest.mark.L4
def test_queryCustomerZhiXinAuxiliary():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryCustomerZhiXinAuxiliary()
    exp = 'S'
    check_values(res['flag'], exp, '校验查询借条借据')


@pytest.mark.L4
def test_customerInfoOther():
    """
    校验客户其他信息
    @author:王厚轩
    """

    res = crm().customerInfoOther()
    exp = '可外呼'
    check_values(res['callStatus'], exp, '校验客户其他信息')


@pytest.mark.L4
def test_queryProductAdjustFeeRate():
    """
    校验客户其他信息
    @author:王厚轩
    """

    res = crm().queryProductAdjustFeeRate()
    exp = '分期(借条)'
    check_values(str(res['productModel']), exp, '校验客户其他信息', cmp='in')


@pytest.mark.L4
def test_creditquery():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().creditquery()
    exp = 'S'
    check_values(res['flag'], exp, '校验查询借条借据')


@pytest.mark.L4
def test_codeList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().codeList()
    exp = 1
    check_values(res['code'], exp, '校验查询借条借据')


@pytest.mark.L4
def test_getTaskList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getTaskList()
    exp = 'S'
    check_values(res['flag'], exp, '校验查询借条借据')


@pytest.mark.L4
def test_queryRobotListByProjectInfo():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryRobotListByProjectInfo()
    exp = 'lv0507001机器人'
    check_values(str(res['data']), exp, '校验查询借条借据', cmp='in')


@pytest.mark.L4
def test_getUserByName():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getUserByName()
    exp = '系统管理员'
    check_values(str(res['data']), exp, '校验查询借条借据', cmp='in')


@pytest.mark.L4
def test_isShowCancelControlButton():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().isShowCancelControlButton()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_qryUserCancelControlRecord():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().qryUserCancelControlRecord()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_existsC7C8Flow():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().existsC7C8Flow()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_customerhistoryAmt():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().customerhistoryAmt()
    exp = 'AJ6550873531436240896batch'
    check_values(str(res['historyAmtList']), exp, '校验查询借条借据', cmp='in')


@pytest.mark.L4
def test_customernewRegHistList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().customernewRegHistList()
    exp = 'aed89b21dc5d49418a2d8cfd2efe38a2'
    check_values(str(res['applQueryHisList']), exp, '校验查询借条借据', cmp='in')


@pytest.mark.L4
def test_customernewRegHistList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().customernewRegHistList()
    exp = 'aed89b21dc5d49418a2d8cfd2efe38a2'
    check_values(str(res['applQueryHisList']), exp, '校验查询借条借据', cmp='in')


@pytest.mark.L4
def test_addActuationModelOperateStep():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().addActuationModelOperateStep()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_selectTmkLineRuleByDashboard():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().selectTmkLineRuleByDashboard()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_alarmevent():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().alarmevent()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_getPerceptionCallSwitch():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getPerceptionCallSwitch()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_selectValidShuntRules():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().selectValidShuntRules()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_treeData():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().treeData()
    exp = '360金融'
    check_values(str(res), exp, '校验查询借条借据', cmp='in')


@pytest.mark.L4
def test_unreadCount():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().unreadCount()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_selectTmkMsgPushManger():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().selectTmkMsgPushManger()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_typeList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().typeList()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_getMsgList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getMsgList()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_getMsgByUserId():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getMsgByUserId()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def page():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().page()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_userList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().userList()
    exp = '统管理员(thinkgem)'
    check_values(str(res['data']), exp, '校验查询借条借据', cmp='in')


@pytest.mark.L4
def test_junior1():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().junior1()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_junior2():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().junior2()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_senior1():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().senior1()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_senior2():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().senior2()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_getGroupUsers():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getGroupUsers()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_getGroupById():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getGroupById()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_list():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().list()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_memberIndex():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().memberIndex()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_list1():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().list1()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_list2():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().list2()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_newSearch():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().newSearch()
    exp = 'O6054340ea45b4e6290d4715956af437c'
    check_values(str(res), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_getData():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getData()
    exp = 'O0e9988096a984f4080d9cb632d1e2cc9'
    check_values(str(res), exp, '校验查询借条借据',cmp='in')

@pytest.mark.L4
def test_mobileChangequeryList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().mobileChangequeryList()
    exp = 'UR6416384180921565185'
    check_values(str(res), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_queryChangeUserNoRecord():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryChangeUserNoRecord()
    exp = "'beforeUserNo': 'UR6524057293519327233'"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_tmkOutCallHistorygetData():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().tmkOutCallHistorygetData()
    exp = "O0e9988096a984f4080d9cb632d1e2cc9"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_rosterCustomerPrelist():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().rosterCustomerPrelist()
    exp = "UR6514985404628992001"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_queryCtpSmsHistoryList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryCtpSmsHistoryList()
    exp = "彩舟"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')



@pytest.mark.L4
def test_smsBlackStatus():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().smsBlackStatus()
    exp = "UR6550854174421286913"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_queryList1():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryList1()
    exp = 1
    check_values((res['pageNo']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_queryList2():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryList2()
    exp = 1
    check_values((res['pageNo']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_queryList3():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryList3()
    exp = 1
    check_values((res['pageNo']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_queryList4():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryList4()
    exp = 1
    check_values((res['pageNo']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_getProjectByThirdStrategy():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getProjectByThirdStrategy()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')



@pytest.mark.L4
def test_accuratesearch():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().accuratesearch()
    exp = "金融"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')

@pytest.mark.L4
def test_getCustomerCallHistoryList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getCustomerCallHistoryList()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_abnormalFeedbacklist():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().abnormalFeedbacklist()
    exp = "张江A组组员01"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')

@pytest.mark.L4
def test_abnormalFeedbackstatistic():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().abnormalFeedbackstatistic()
    exp = "话类-未处理"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_fileManagerlist():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().fileManagerlist()
    exp = "肖超宇2"
    check_values(str(res), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_aiTermlist():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().aiTermlist()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_nodelist():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().nodelist()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_sceneslist():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().sceneslist()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_qualitylist():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().qualitylist()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_qualityreceiptList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().qualityreceiptList()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_tmkRosterApplyAmtlist():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().tmkRosterApplyAmtlist()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_querySimpleInfoCanvasByRight():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().querySimpleInfoCanvasByRight()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_querySimpleList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().querySimpleList()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_queryConcurrencyCanvasPageList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryConcurrencyCanvasPageList()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_queryConcurrencyGroupPageList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().queryConcurrencyGroupPageList()
    exp = 'S'
    check_values((res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_crosslistData():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().crosslistData()
    exp = '金融'
    check_values(str((res['list'])), exp, '校验查询借条借据',cmp='in')



@pytest.mark.L4
def test_xiexiaopeizhigetUserByName():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().xiexiaopeizhigetUserByName()
    exp = '系统管理员'
    check_values(str((res['data'])), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_getManualConfigList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().getManualConfigList()
    exp = '协销222'
    check_values(str((res['list'])), exp, '校验查询借条借据',cmp='in')


@pytest.mark.L4
def test_configList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = crm().configList()
    exp = '名单库协销'
    check_values(str((res['list'])), exp, '校验查询借条借据',cmp='in')
