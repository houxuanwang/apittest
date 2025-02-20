import pytest

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.task_service import Task


# -*- coding: UTF-8 -*-


@pytest.mark.L0
def test_gettaskgrouplist():
    """
    获取组别管理数据
    @author:王厚轩
    """
    res = Task().gettaskgrouplist()
    exp = '1'
    check_values(exp, res['code'], '校验获取组别管理数据接口数据')


# @pytest.mark.L0
def test_getcrosssalelist():
    """
    获取所有坐席
    @author:王厚轩
    """
    res = Task().getcrosssalelist()
    res.check_state_code(200)



@pytest.mark.L0
@pytest.mark.skip(reason="忽略")
def test_getTaskHandleUserList():
    """
    列表处理人数据范围
    @author:王厚轩
    """
    res = Task().getTaskHandleUserList()
    exp = 'lv001'
    check_values(exp, res['list'][0]['loginName'], '校验列表处理人数据范围接口数据')


@pytest.mark.L0
def test_gettmkscreenfilterlist():
    """
    查询条件过滤器
    @author:王厚轩
    """
    res = Task().gettmkscreenfilterlist()
    exp = 200
    check_values(exp, res['code'], '校验查询条件过滤器接口数据')


#@pytest.mark.L0
def test_pendinglist():
    """
    顶部搜索栏查询
    @author:王厚轩
    """
    res = Task().pendinglist()
    exp = 1
    check_values(exp, res['pageNo'], '校验顶部搜索栏查询接口数据')


@pytest.mark.L0
def test_codeList():
    """
    获取短信模板
    @author:王厚轩
    """
    res = Task().codeList()
    exp = 1
    check_values(exp, res['code'], '校验获取短信模板接口数据')


@pytest.mark.L0
@pytest.mark.skip(reason='忽略')
def test_getCouponList():
    """
    获取优惠券模板
    @author:王厚轩
    """
    res1 = Task().pendinglist()
    res = Task().getCouponList(projectList=res1['list'][0]['projectType'],
                               rosterNumbers=res1['list'][0]['rosterNumber'], userNo=res1['list'][0]['userNo'],
                               createDate=res1['list'][0]['createDate'])
    exp = 200
    check_values(exp, res['code'], '校验获取优惠券模板接口数据')


@pytest.mark.L0
@pytest.mark.skip(reason="忽略")
def test_sendMsg(db):
    """
    发送短信接口
    @author:王厚轩
    """
    db.execute_sql("delete from tmk_message_record where remarks = '短链测试' order by jid desc;")
    res1 = Task().sendMsg()
    exp = '发送成功'
    db.execute_sql("delete from tmk_message_record where remarks = '短链测试' order by jid desc;")
    check_values(exp, res1['message'], '校验发送短信接口数据')


@pytest.mark.L0
@pytest.mark.skip(reason="忽略")
def test_checkRule():
    """
    拨打电话接口
    @author:王厚轩
    """
    res1 = Task().checkRule()
    exp = 'dce6a38c75283d01744aa746d93c68e4'
    check_values(exp, res1['data']['mobileMD5'], '校验拨打电话接口数据')


@pytest.mark.L0
def test_index():
    """
    客户按钮
    @author:王厚轩
    """
    res = Task().index()
    res.check_state_code(200)


@pytest.mark.L0
def test_regHistList():
    """
    注册列表
    @author:王厚轩
    """
    res = Task().regHistList()
    exp = 1
    check_values(exp, res['code'], '校验注册列表接口数据')


@pytest.mark.L0
def test_credit():
    """
    授信列表查询
    @author:王厚轩
    """
    res = Task().credit()
    exp = 1
    check_values(exp, res['code'], '校验授信列表查询接口数据')


@pytest.mark.L0
def test_loan():
    """
    借款借据-查询
    @author:王厚轩
    """
    res = Task().loan()
    exp = 1
    check_values(exp, res['code'], '校验借款借据-查询接口数据')


@pytest.mark.L0
@pytest.mark.skip(reason="忽略")
def test_callRecordhistory():
    """
    客户详情页-通话记录
    @author:王厚轩
    """
    res = Task().callRecordhistory()
    exp = 1
    check_values(exp, res['code'], '校验客户详情页-通话记录接口数据')


@pytest.mark.L0
def test_historySms():
    """
    历史短信
    @author:王厚轩
    """
    res = Task().historySms()
    exp = 1
    check_values(exp, res['code'], '校验历史短信接口数据')


@pytest.mark.L0
@pytest.mark.skip(reason="忽略")
def test_save(db):
    """
    预约跟进
    @author:王厚轩
    """
    res = Task().save()
    exp = '20211009'
    check_values(exp, res['title'], '校验预约跟进接口数据')
    db.execute_sql('delete from tmk_customer_reservation where note=20211009 order by jid desc limit 1')






















@pytest.mark.L4
def test_queryPublicTaskList():
    """
    预约跟进
    @author:王厚轩
    """
    res = Task().queryPublicTaskList()
    exp = 'S'
    check_values(exp, res['flag'], '校验查询公共任务列表')







# 进详情页开始轮询:
# while 1<2:
#     if (未切到其他页面 ) and (详情页的客户与坐席的通话状态 = 通话) and （flag = 没弹过） and (查询到有流程中的借据)：
#         1.弹视频
#         2.flag置为已弹
#     sleep(5)
#     if 详情页面被销毁： # 轮询结束
#         break
# 关闭详情页，跳出轮询，flag重置为未弹过
#接收到双通事件，flag置为false
# 多个详情页（ABCD）：从A切到B，A停止轮询，切回A，A继续轮询？

