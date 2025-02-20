import pytest

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.userinfo_service import User


# -*- coding: UTF-8 -*-

@pytest.mark.L4
def test_getNamePinyin():
    """
    校验获取客户姓名拼音
    @author:王厚轩
    """
    res = User().getNamePinyin()
    exp = ["jīn","róng"]
    check_values(exp, res['data'], '校验获取客户姓名拼音')


@pytest.mark.L4
def test_reportSeatStatus():
    """
    校验切换坐席状态，将坐席状态切为小休
    @author:王厚轩
    """
    res = User().getNamePinyin()
    exp = 'S'
    check_values(exp, res['flag'], '校验切换坐席状态，将坐席状态切为小休')

@pytest.mark.L4
def test_newIndexData():
    """
    校验客户详情页用户信息
    @author:王厚轩
    """
    res = User().newIndexData()
    print('打印')
    print(res['data']['crmCustomerInfo']['userNo'])
    exp = 'UR6524057293519327233'
    check_values(exp, res['data']['crmCustomerInfo']['userNo'], '校验客户详情页用户信息')


@pytest.mark.L4
def test_customerInfoOther():
    """
    校验客户详情页其他用户信息
    @author:王厚轩
    """
    res = User().customerInfoOther()
    exp = True
    check_values(exp, res['tieFlag'], '校验客户详情页其他用户信息')

@pytest.mark.L4
def test_queryProductAdjustFeeRate():
    """
    校验客户详情页用户借条相关信息
    @author:王厚轩
    """
    res = User().queryProductAdjustFeeRate()
    exp = "分期(借条)"
    check_values(exp, res['productModel'][0]['productType'], '校验客户详情页用户借条相关信息')