import hashlib
import json
import logging
import operator
import os
import platform
import threading
import time
from functools import reduce, wraps
from typing import Callable
from common.diff_handler import DiffHandler, TypeEncoder, replace_msg_key

import jsonpath_rw
import sure  # noqa
from box import Box
from dateutil.relativedelta import relativedelta
from sure import expect

from common.file_utils import FileUtils

lock = threading.Lock()

logger = logging.getLogger(__name__)
sure.version  # noqa


def get_from_dict(map_data: dict, json_path: str) -> any:
    """
    通过json_path从map_data中获取目标值
    @param map_data:
    @param json_path:
    @return:
    """
    if json_path.startswith('_Response'):
        json_path = json_path.split('.')[1:]
    else:
        json_path = json_path.split('.')
    try:
        return reduce(operator.getitem, json_path, map_data)
    except Exception:
        pass
    return jsonpath_rw.parse(('.'.join(json_path))).find(map_data)[0].value


def get_md5(string: str) -> str:
    return hashlib.md5(string.encode()).hexdigest()


def get_os_system():
    return platform.system()


# 具体用例参考 tests/common_tests.py/test_check_values_func
def check_values(expect_val=None, actual_val=None, desc: str = None, cmp: str = 'eq', **kwargs) -> None:
    """
    用于比较两个对象支持多种类型
    @param expect_val: 预期值
    @param actual_val: 实际值
    @param desc: 描述检查信息
    @param cmp: 比较类型，支持以下类型比较
            e.g.
                # eq [equal] 相等
                # gt [greater than] (大于>)
                # ge [greater and equal]（大于等于>=）
                # lt [less than]（小于<）
                # le [less and equal]（小于等于<=）
                # tr [True] (默认检查True)
                # fl [False] (默认检查False, False、[]、None等所有false对象)
                # in [contains] (包含)
                # ne [not equal] (不等于 !=) 
    @return: None
    """

    cmp_type = ['eq', 'gt', 'ge', 'lt', 'le', 'tr', 'fl', 'in', 'ne']
    assert cmp in cmp_type, f'[暂无该cmp:{cmp}比较类型,已有[cmp_type]:{cmp_type}]'

    logger.info(f'[检查点]：{desc}')
    desc_short_succeeded = f'[{desc}成功,{{}} check success]'

    if cmp == 'eq':  # 等于
        diff_handler = DiffHandler(expect_val, actual_val)
        result = diff_handler(**kwargs)

        result_msg = result.get_msg()
        result_json = None
        if result_msg:
            result_json = json.dumps(result_msg, indent=4, separators=(',', ':'), ensure_ascii=False, cls=TypeEncoder)
            result_json = replace_msg_key(result_json)

        desc = desc if desc else ""
        msg = '\n' + desc + '\n' + (
            result_json if result_json else '校验成功')

        # 断言失败
        if not result.is_success():
            assert False, msg
        else:
            print_msg(msg)

    elif cmp == 'gt':  # 大于
        actual_val.should.be.greater_than(expect_val)
        logger.info(desc_short_succeeded.format(f'{actual_val} > {expect_val}'))
    elif cmp == 'ge':  # 大于等于
        actual_val.should.be.greater_than_or_equal_to(expect_val)
        logger.info(desc_short_succeeded.format(f'{actual_val} >= {expect_val}'))
    elif cmp == 'lt':  # 小于
        actual_val.should.be.lower_than(expect_val)
        logger.info(desc_short_succeeded.format(f'{actual_val} < {expect_val}'))
    elif cmp == 'le':  # 小于等于
        actual_val.should.be.lower_than_or_equal_to(expect_val)
        logger.info(desc_short_succeeded.format(f'{actual_val} <= {expect_val}'))
    elif cmp == 'tr':  # True,所有True对象
        actual_val.should.be.true  # noqa
        logger.info(desc_short_succeeded.format(actual_val))
    elif cmp == 'fl':  # []、False、()所有空对象
        actual_val.should.be.false  # noqa
        logger.info(desc_short_succeeded.format(actual_val))
    elif cmp == 'in':  # 包含
        expect_val.should.contain(actual_val)
        logger.info(desc_short_succeeded.format(f'{actual_val} in {expect_val}'))
    elif cmp == 'ne':
        expect(actual_val).to.not_be.equal(expect_val)
        logger.info(desc_short_succeeded.format(f'{actual_val} != {expect_val}'))


def print_msg(msg=None):
    """
    打印信息
    @param msg:信息
    """
    print(msg)
    logger.info(msg)


def read_file(file_path, file_type=''):
    """
    读文件，仅支持json，csv、txt和yaml文件类型
    @param file_path:  文件路径
    @param file_type: 文件类型，可不传，不传默认取文件后缀获取文件类型
    @return: 读取的文件数据
    """
    file_data = FileUtils(file_path=file_path, file_type=file_type).common_read_file()
    return file_data



