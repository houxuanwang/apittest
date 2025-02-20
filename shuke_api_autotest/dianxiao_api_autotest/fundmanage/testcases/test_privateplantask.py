import pytest
import requests

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.privateplantask_service import privatePlanTask


# -*- coding: UTF-8 -*-

@pytest.mark.L4
def test_queryPrivatePlanTaskList1():
    """
    校验个人销售任务查询接口-促动支
    @author:王厚轩
    """

    res = privatePlanTask().queryPrivatePlanTaskList1()
    print(res['flag'])
    exp = 0
    check_values(exp, res['total'], '校验个人销售任务查询接口-促动支', cmp='gt')


@pytest.mark.L4
def test_queryPrivatePlanTaskList2():
    """
    校验个人销售任务查询接口-促完件
    @author:王厚轩
    """

    res = privatePlanTask().queryPrivatePlanTaskList2()
    exp = 0
    check_values(exp, res['total'], '校验个人销售任务查询接口-促完件', cmp='gt')

@pytest.mark.L4
def test_selectData():
    """
    校验查询任务组数据
    @author:王厚轩
    """

    res = privatePlanTask().selectData()
    exp = '自动化测试'
    check_values( str(res['data']),exp, '校验查询任务组数据', cmp='in')
