import pytest

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.list_service import List


# -*- coding: UTF-8 -*-

@pytest.mark.L4
def test_queryPublicTaskList():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = List().getlist()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')



@pytest.mark.L4
def test_fileUpload():
    """
    校验上传名单到拆分列表1.0列表
    @author:王厚轩
    """
    res = List().fileupload()
    exp = 'S'
    check_values(exp, res['flag'], '校验上传名单到拆分列表1.0列表')



@pytest.mark.L4
def test_split():
    """
    校验手动拆分
    @author:王厚轩
    """
    res = List().spilt()
    exp = 'S'
    check_values(exp, res['flag'], '校验手动拆分')


@pytest.mark.L4
def test_allotAjax():
    """
    校验名单分配是否锁定中
    @author:王厚轩
    """
    res = List().allotAjax()
    exp = 0
    check_values(exp, res['code'], '校验手动拆分')

@pytest.mark.L4
def test_distributionPreservation():
    """
    校验名单分配是否锁定中
    @author:王厚轩
    """
    res = List().distributionPreservation()
    exp = 'S'
    check_values(exp, res['flag'], '校验手动拆分')