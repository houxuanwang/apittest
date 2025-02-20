import pytest
import requests

from common.utils import check_values
from dianxiao_api_autotest.fundmanage.services.workspace_service import Workspace


# -*- coding: UTF-8 -*-

@pytest.mark.L4
def test_pendingList():
    """
    校验查询名单库
    @author:王厚轩
    """
    url1 = "https://zkxqw-test.360-jr.com/tmksql"
    payload = {
        "sql": "select number FROM `tmk_roster` where project_id='180daa74425846d996dea45f5b499e31'  and create_date>CURDATE()  order by create_date desc "
               "limit 1;"}
    mingdannumber = requests.request("POST", url1, json=payload, verify=False).json()[0]['number']
    res = Workspace().pendinglist()
    print(res['list'][0]['rosterNumber'])
    exp = mingdannumber
    check_values(exp, res['list'][0]['rosterNumber'], '校验查询名单库')

