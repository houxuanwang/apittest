import operator

import jsonpath_rw
from functools import reduce, wraps

import requests
import logging

_Response = requests.Response
from box import Box

logger = logging.getLogger(__name__)


class ApiRequest:
    session = requests.Session()

    def __call__(self, host=None, url=None, method='POST', params=None, data=None, json=None, files=None,
                 timeout=123, headers=None, retry=3, *args, **kwargs):
        """
        :param host: root domain
        :param url: view url
        :param method: [GET, POST...]
        :param params: send query data like ?a=1&b=2
        :param data: send form data like {'key1': 'value1', 'key2': 'value2'}
        :param json: send json data
        :param files: send file data
        :param timeout:
        :param headers:
        :param retry: 重试次数
        :param args:
        :param kwargs:
        :return:  Response obj
        """
        self.session.adapters.DEFAULT_RETRIES = retry
        print("__name__")
        print(__name__)
        timeout = timeout
        logger.info("=" * 100)
        logger.info(f'[请求URL]:{url}')
        logger.info(f'[请求方法]: {method}')
        logger.info(f'[请求query数据]: {params}')
        logger.info(f'[请求form数据]: {data}')
        logger.info(f'[请求json数据]: {json}')
        logger.info(f'[请求files数据]: {files}')

        self.rep = self.session.request(url=url, method=method, params=params, data=data, json=json, files=files,
                                        timeout=timeout, headers=headers, verify=False, *args, **kwargs)

        try:
            result = self.rep.json()
        except Exception as exc:
            logger.warning(f'json数据获取失败，使用r.text属性!:{exc}')
            self.rep.encoding = self.rep.apparent_encoding  # 解决中文乱码问题
            result = self.rep.text

        logger.info(f'[响应结果]: {result}')
        logger.info(f'[响应http_code]: {self.rep.status_code}')
        logger.info(f'[响应耗时]: {self.rep.elapsed.total_seconds():0.2f}秒')
        # logger.info(100 * '=')

        if type(result) is list:
            return result
        else:
            return Response(self.rep)


class Response(_Response):
    def __init__(self, rep: requests.Response):
        """
        对原requests的Response对象添加更多操作和属性
        :param rep: requests的响应对象 rep = requests.get(xxx)
        """
        self.rep = rep
        # self.code = code
        # self.data = data
        # self.message = message
        self.__dict__.update(rep.__dict__)

        # try:
        #     self.rep_json = self.rep.json()
        # except Exception:
        #     self.rep_json = dict(code='', data='', message='')
        #
        # self.rep_json = Box(self.rep_json)

    @property
    def code(self):
        return self.rep_json.code

    @property
    def data(self):
        return self.rep_json.data

    @property
    def msg(self):
        return self.rep_json.msg

    @property
    def result(self):
        return self.rep_json

    def check_state_code(self, http_status_code=200):
        """
        check response http status code
        {self.status_code}
        :param http_status_code:
        :return:
        """
        assert self.status_code == http_status_code, f'[校验失败,http_status_code 实际值:{self.status_code} != 预期值:{http_status_code}]'
        logger.info(f'[校验成功,http_status_code 实际值:{self.status_code} == 预期值:{http_status_code}]')
        return self

    def check_body_code(self, check_body_code=0):
        """
        check response body code
        {self.rep.code}
        :param code: response code number
        :return:
        """
        assert self.code == check_body_code, f'[校验失败,response.body.code 实际值:{self.code} != 预期值:{check_body_code}]'
        logger.info(f'[校验成功,response.body.code 实际值:{self.code} == 预期值:{check_body_code}]')
        return self

    def check_value(self, expect_value, json_path_or_value):
        """
        check expect_value equals response data by json path
        @expect_value: 预期结果值
        @json_path:json path
        """
        if '.' in json_path_or_value:
            json_path_or_value = get_from_dict(self.json(), json_path_or_value)
        assert expect_value == json_path_or_value, f'[校验失败,预期结果:{expect_value} != 实际结果:{json_path_or_value}]'
        logger.info(f'[校验成功,预期结果={expect_value},实际结果={json_path_or_value}]')
        return self


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
