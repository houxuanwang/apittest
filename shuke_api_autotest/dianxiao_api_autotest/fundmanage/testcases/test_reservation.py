"""
@Project ：shuke_api_autotest 
@File ：test_reservation.py
@Author ：陈玲玲
@Date ：2021/9/30 11:04 
"""
import pytest
# -*- coding: UTF-8 -*-
from common.utils import check_values
from dianxiao_api_autotest.conftest import change_user
from dianxiao_api_autotest.fundmanage.services.task_service import Task
from dianxiao_api_autotest.fundmanage.services.reservation_service import Reservation
import time
from dianxiao_api_autotest.fundmanage.testdata.jsonservice import InitDataService


@pytest.mark.L0
def test_resrvationlist():
    """
    获取预约管理列表
    @author:陈玲玲
    """
    res = Reservation().reservationlist()
    res.check_state_code(200)


@pytest.mark.L0
@pytest.mark.skip(reason="忽略")
def test_reservationlistjson():
    """
    预约管理--查询
    @author:陈玲玲
    """
    res = Reservation().reservationlistJson()
    exp = "'projectName': '自动化-勿动'"
    check_values( str(res['list']),exp, '校验获取所有坐席接口数据',cmp='in')


@pytest.mark.L0
def test_crmindex():
    """
    预约管理--点击客户按钮
    @author:陈玲玲
    """
    res = Reservation().crmindex()
    check_values('text/html;charset=UTF-8', res.headers['Content-Type'], desc="获取预约管理列表接口成功")

@pytest.mark.L0
@pytest.mark.skip(reason="忽略")
def test_customercredit():
    """
    预约管理-客户详情页-授信列表查询
    @author:陈玲玲
    """
    res = Reservation().customercredit()
    exp = "'custName': '哈哈'"
    check_values(str(res), exp, desc="获取授信列表查询接口成功",cmp='in')


