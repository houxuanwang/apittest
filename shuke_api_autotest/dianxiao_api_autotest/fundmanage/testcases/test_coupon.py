import pytest

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.coupon_service import coupon
from dianxiao_api_autotest.shuke_settings import R, SIT_HOST


# -*- coding: UTF-8 -*-

@pytest.mark.L4
def test_checkUserCouponCount():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = coupon().checkUserCouponCount()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')


@pytest.mark.L4
def test_checkAvailableCoupon():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = coupon().checkAvailableCoupon()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')


@pytest.mark.L4
def test_checkAvailableQw():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = coupon().checkAvailableQw()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')


@pytest.mark.L4
def test_getUserCouponRecord1():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = coupon().getUserCouponRecord1()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')

@pytest.mark.L4
def test_getUserCouponRecord2():
    """
    校验查询拆分列表1.0列表
    @author:王厚轩
    """
    res = coupon().getUserCouponRecord2()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询拆分列表1.0列表')

BASE_URL = "http://sit-tmk.360-jr.com/backend"
@pytest.mark.L9
def test_get_name_pinyin_success():
    # 测试成功场景
    response = R(url=f"{BASE_URL}/pinyin/getNamePinyin", method='GET', params={"name": "张三"})
    assert response.status_code == 200
    assert response.json() == {"code": 200, "message": "success", "data": ["zhang", "san"]}




