import importlib
import inspect
import logging
import sys

# coding: utf-8
import json
import requests


def dingding_robot(data):
    # 机器人的webhooK 获取地址参考：https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq
    # 小分队

    webhook = "https://oapi.dingtalk.com/robot/send?access_token" \
              "=4aa0e1e5a81162c0ad50a8979ca3743980ef7bb164c6a1f3f703e2feb5ce20fc "
    # 资金系统
    webhook1 = "https://oapi.dingtalk.com/robot/send?access_token" \
               "=673216ea9e22e942ab2558a3a408b33695ed54c35d20294430286466d659467f "
    # 接口自动化群
    webhook2 = "https://oapi.dingtalk.com/robot/send?access_token" \
               "=33c33d7d9dfecc5227db627a661fcb3a2e8d133c17f9e84248f3e53e6a7309ef "
    # 智客星
    webhook3 = "https://im.360teams.com/api/qfin-api/rce-app/robot/send?access_token" \
               "=487bcbb120b644de8bd8f756c0cb34739d37feb848af45d5847ad654fefea40e "
    headers = {'content-type': 'application/json'}  # 请求头
    r = requests.post(webhook3, headers=headers, data=json.dumps(data))
    r.encoding = 'utf-8'
    return (r.text)


import click
# noinspection PyUnresolvedReferences
import pytest
from box import Box

sys.path.append('.')

from common.utils import read_file  # noqa

logger = logging.getLogger(__name__)


@click.command()
@click.option('-f', '--file', help='file', default='.report.json')
@click.option('-j', '--job', help='job')
# @click.option('-t', '--trigger', help='trigger')
def notify_autotest_result(file: str, job: str) -> None:
    """
    @param file: json report file path

    钉钉自动化结果消息通知
    """
    import os
    print(os.getcwd())
    report_path = file or '.report.json'
    report_result = Box.from_json(filename=report_path)
    duration = report_result.duration
    total = report_result.summary.get('total') or '0'
    passed_ = report_result.summary.get('passed') or '0'
    rerun = report_result.summary.get('rerun') or '0'
    passed = int(passed_) + int(rerun)
    failed = report_result.summary.get('failed') or '0'
    skipped = report_result.summary.get('skipped') or '0'
    error = report_result.summary.get('error') or '0'
    failed = int(error) + int(failed)  # 把错误的用例和失败的用例统一为failed用例
    jenkins_auto = "http://jenkins-test.qihoo.net/jenkins/view/APITest/job/shuke_gongdan/{}/allure/"
    print(passed)
    print(total)
    print(failed)
    jenkins_auto = "http://jenkins-test.qihoo.net/jenkins/view/Autotest/job/shuke_gongdan/{}/allure/"
    url = jenkins_auto.format(job),
    print(url)
    print(url)
    print(url)

    body = {
        "msgtype": "text",
        "text": {
             # "title": "非上市资金、权限、极光、上市资金、新电销、上市财务接口自动化测试报告",
            "content": "工单接口自动化测试报告：\n" +
                    f"> 【用例总数】：{total:<9}\n\n" +
                    f"> 【成功用例数】：{passed:<9}\n\n" +
                    f"> 【失败用例数】：{failed:<9}\n\n" +
                    f"> 【跳过用例数】：{skipped:<9}\n\n" +
                    f"> [请点击报告链接查看详情!]http://jenkins-test.qihoo.net/jenkins/view/Autotest/job/shuke_gongdan/{job}/allure/ \n "
        },

    }

    res = dingding_robot(body)
    print(res)


def send_message_case_failed(notify_key: str, file_name: str):
    """
    企业微信通知case错误
    @param notify_key: 对接群
    @param file_name: 报告文件
    """

    # 读取执行结果报告中数据
    report_file_json = read_file(file_name)

    # 如果文件为空直接返回
    if not report_file_json:
        return
    case_list = report_file_json["tests"]
    # 查找错误case
    failed_cases = [case.get("nodeid").replace("/", ".").split(".py::") for case in case_list if
                    case.get("outcome") == "error" or case.get("outcome") == "failed"]

    if not failed_cases or len(failed_cases) > 10:
        logger.info(f"无错误case or 错误case{len(failed_cases)}")
        return
    author_ids = []
    contents = []
    for failed_case in failed_cases:
        # 动态载入，获取描述
        failed_case_name_origin = failed_case[-1]
        contents.append(failed_case_name_origin)

        if failed_case[0] == 'manga_api_autotest.pay.testcases.test_buy_card':
            continue
        module = importlib.import_module(failed_case[0])
        module_fun = getattr(module, (failed_case_name_origin.split("["))[0])
        # 描述转为字典获取作者
        author = inspect.getdoc(module_fun).split("@author:")[-1]
        author = author.strip()
        try:
            author_ids.append(authors[author])
        except KeyError as exc:
            logger.warning(f"未查询到用户:{exc}")

    contents = ',\n'.join(contents).rstrip("\n")
    # 用户列表去重并发送消息
    text_message = TextMessage(content=f"{contents}\n用例错误请检查！",
                               mentioned_mobile_list=list(set(author_ids)))
    WechatService(notify_key).send_message(text_message)


if __name__ == '__main__':
    notify_autotest_result()
