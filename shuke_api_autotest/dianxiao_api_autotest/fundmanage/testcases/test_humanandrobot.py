import pytest

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.humanandrobot_service import humanAndRobot


# -*- coding: UTF-8 -*-

@pytest.mark.L4
def test_wlhLoanCreditedInfo():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = humanAndRobot().wlhLoanCreditedInfo()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')


@pytest.mark.L4
def test_wlhLoanCreditedInfo():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = humanAndRobot().wlhLoanCreditedInfo()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')


@pytest.mark.L4
def test_zhiXinLoanList1():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = humanAndRobot().zhiXinLoanList1()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')

@pytest.mark.L4
def test_zhiXinLoanList2():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = humanAndRobot().zhiXinLoanList2()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')


@pytest.mark.L4
def test_callRecordhistory():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = humanAndRobot().callRecordhistory()
    exp = 'Ob59b64028c3046f7a1486b4db0bab295'
    check_values( str(res['callRecordhistory']),exp, '校验查询拆分列表1.0列表',cmp='in')


@pytest.mark.L4
def test_getZhiXinAssistTips():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = humanAndRobot().getZhiXinAssistTips()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')


@pytest.mark.L4
def test_userAmtInfo():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = humanAndRobot().userAmtInfo()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')

@pytest.mark.L4
def test_getCallWishModeRecord():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = humanAndRobot().getCallWishModeRecord()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')
