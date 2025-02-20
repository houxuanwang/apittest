import json
import re

from box import Box, BoxList
from deepdiff import DeepDiff


class DiffHandler:
    def __init__(self, expect_val, actual_val):
        # 错误消息
        self.__err_msg = None
        self.__expect_val = transfer_to_simple_type(expect_val)
        self.__actual_val = transfer_to_simple_type(actual_val)
        self.__success_msg = None

    def __call__(self, **kwargs):
        """
        比较并处理结果
        """
        compare_result = DeepDiff(self.__expect_val, self.__actual_val, cutoff_intersection_for_pairs=1,
                                  **kwargs).to_dict()
        self.__parse_compare_result(compare_result)
        return self.__handle_check_result()

    def __parse_compare_result(self, compare_result: {}):
        """
        params compare_result：期望值和实际值对比结果
        """
        compare_result.pop('dictionary_item_added', '')
        if compare_result == {}:
            return
        msg = compare_result
        self.__record_msg(msg)

    def __handle_check_result(self):
        """
        处理检查结果
        """
        # 若存在错误信息，则返回失败
        if self.__err_msg:
            return CheckResult(False, self.__err_msg)

        return CheckResult(True, self.__success_msg)

    def __record_msg(self, msg):
        """
        记录错误信息
        @param msg: 错误消息
        """
        # 打印信息
        # self.print_msg(msg)
        self.__err_msg = msg


def transfer_to_simple_type(obj=None):
    """
    将特殊类型转换为常用类型
    @param obj:对象
    """
    if obj is None:
        return obj

    # 处理Box
    if isinstance(obj, Box):
        return obj.to_dict()

    # 处理BoxList
    if isinstance(obj, BoxList):
        return obj.to_list()

    return obj


class CheckResult:
    def __init__(self, success: bool, msg: {}):
        """
        @param success:是否成功
        @param msg: 成功/失败消息
        """
        self.__success = success
        self.__msg = msg

    def is_success(self):
        return self.__success

    def get_msg(self):
        return self.__msg


class TypeEncoder(json.JSONEncoder):
    def default(self, o):
        return str(o)


def replace_msg_key(result_json):
    result_json, count = re.subn(r'(old_value)', "预期值", result_json)
    result_json, count = re.subn(r'(new_value)', "实际值", result_json)
    result_json, count = re.subn(r'(old_type)', "预期值类型", result_json)
    result_json, count = re.subn(r'(new_type)', "实际值类型", result_json)
    result_json, count = re.subn(r'(values_changed)', "预期值与实际值values不同", result_json)
    result_json, count = re.subn(r'(type_changes)', "预期值与实际值类型不同", result_json)
    result_json, count = re.subn(r'(dictionary_item_removed|iterable_item_removed|set_item_removed)',
                                 "实际值比预期值缺少字段",
                                 result_json)
    result_json, count = re.subn(r'(dictionary_item_added|iterable_item_added|set_item_added)', "实际值比预期值增加非dict字段",
                                 result_json)
    return result_json
