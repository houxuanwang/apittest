from api_request import ApiRequest
import pytest


@pytest.mark.L0
def test_2():
    a = ApiRequest()
    b = a(url="https://zkxms-test.360-jr.com/message/qw/customer/customerList/condition", method='POST')
    c = a(url="https://www.baidu.com", method='POST')
    print(f'a的类型是：{type(a)}')
    print(callable(a))
    print(f'b的类型是：{type(b)}')
    print(callable(b))

    def f1():
        return 1

    c = f1()
    print(f'c的类型是：{type(c)}')
    print(callable(c))
    # print(dir(b))
    # print(dir(a))
    # print(b.json())
    # print(type(a))
    # print(b.rep)
    # print(help(b))
