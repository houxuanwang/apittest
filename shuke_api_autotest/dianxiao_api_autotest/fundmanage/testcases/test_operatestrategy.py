import pytest
import requests

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.operatestrategy_service import operateStrategy


# -*- coding: UTF-8 -*-

@pytest.mark.L4
def test_queryList():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = operateStrategy().queryList()
    exp = '常规策略1'
    check_values(str(res['data']), exp, '校验查询借条借据',cmp='in')

@pytest.mark.L4
def test_updateStatus1():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = operateStrategy().updateStatus1()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')


@pytest.mark.L4
def test_updateStatus2():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = operateStrategy().updateStatus2()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_addOrUpdate():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = operateStrategy().addOrUpdate()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_listMessageTemplate():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = operateStrategy().listMessageTemplate()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')

@pytest.mark.L4
def test_selectValidShuntRules():
    """
    校验查询借条借据
    @author:王厚轩
    """

    res = operateStrategy().selectValidShuntRules()
    exp = 'S'
    check_values(str(res['flag']), exp, '校验查询借条借据')