import pytest
import requests

BASE_URL = "https://zkxms-test.360-jr.com"  # 请替换为实际的API基础URL

# 测试查询任务列表
def test_query_task_list():
    url = f"{BASE_URL}/message/task/manage/index"
    payload = {
        "pageSize": 20,
        "pageNo": 0,
        "taskName": "string",
        "taskCode": "string",
        "taskSource": 0,
        "projectId": [0],
        "channelIds": [0],
        "status": [0],
        "strategyTarget": 0,
        "taskType": 0,
        "updateBy": "string",
        "updateTimeStart": "string",
        "updateTimeEnd": "string",
        "taskStartTimeStart": "string",
        "taskStartTimeEnd": "string",
        "taskEndTimeStart": "string",
        "taskEndTimeEnd": "string",
        "actualEndTimeStart": "string",
        "actualEndTimeEnd": "string",
        "sort": "string"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试新增任务
def test_add_task():
    url = f"{BASE_URL}/message/task/manage/save"
    payload = {
        "id": 0,
        "taskCode": "string",
        "taskSource": 0,
        "allotTaskCode": "string",
        "allotTaskId": 0,
        "taskName": "string",
        "channelId": 0,
        "channelName": "string",
        "status": 0,
        "projectId": 0,
        "projectName": "string",
        "targetPlan": 0,
        "strategyTarget": 0,
        "planExplain": "string",
        "customerCount": 0,
        "seatCount": 0,
        "taskSort": 0,
        "tagFlag": 0,
        "actualEndTime": "string",
        "endType": 0,
        "execDays": 0,
        "createBy": "string",
        "createDate": "string",
        "updateBy": "string",
        "updateName": "string",
        "updateDate": "string",
        "taskStartTime": "string",
        "taskEndTime": "string",
        "qwAllotTaskVo": {
            "id": 0,
            "taskId": "string",
            "taskName": "string",
            "taskSource": 0,
            "allotScene": 0,
            "addWechatChannelCode": "string",
            "shortMsgCode": "string",
            "shortMsgChannelCode": "string",
            "allotType": 0,
            "taskType": 0,
            "ruleName": "string",
            "ruleId": 0,
            "status": 0,
            "updateBy": "string",
            "updateName": "string",
            "executionTime": "string",
            "executionStartTime": "string",
            "executionEndTime": "string",
            "executionType": 0,
            "executionDay": 0,
            "execTime": "string",
            "createBy": "string",
            "createDate": "string",
            "updateDate": "string",
            "groupConfig": [
                {
                    "groupCode": "string",
                    "groupType": 0,
                    "groupName": "string"
                }
            ],
            "userIds": ["string"],
            "ruleVersion": "string"
        },
        "execStatus": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试修改任务
def test_update_task():
    url = f"{BASE_URL}/message/task/manage/update"
    payload = {
        "id": 0,
        "taskCode": "string",
        "taskSource": 0,
        "allotTaskCode": "string",
        "allotTaskId": 0,
        "taskName": "string",
        "channelId": 0,
        "channelName": "string",
        "status": 0,
        "projectId": 0,
        "projectName": "string",
        "targetPlan": 0,
        "strategyTarget": 0,
        "planExplain": "string",
        "customerCount": 0,
        "seatCount": 0,
        "taskSort": 0,
        "tagFlag": 0,
        "actualEndTime": "string",
        "endType": 0,
        "execDays": 0,
        "createBy": "string",
        "createDate": "string",
        "updateBy": "string",
        "updateName": "string",
        "updateDate": "string",
        "taskStartTime": "string",
        "taskEndTime": "string",
        "qwAllotTaskVo": {
            "id": 0,
            "taskId": "string",
            "taskName": "string",
            "taskSource": 0,
            "allotScene": 0,
            "addWechatChannelCode": "string",
            "shortMsgCode": "string",
            "shortMsgChannelCode": "string",
            "allotType": 0,
            "taskType": 0,
            "ruleName": "string",
            "ruleId": 0,
            "status": 0,
            "updateBy": "string",
            "updateName": "string",
            "executionTime": "string",
            "executionStartTime": "string",
            "executionEndTime": "string",
            "executionType": 0,
            "executionDay": 0,
            "execTime": "string",
            "createBy": "string",
            "createDate": "string",
            "updateDate": "string",
            "groupConfig": [
                {
                    "groupCode": "string",
                    "groupType": 0,
                    "groupName": "string"
                }
            ],
            "userIds": ["string"],
            "ruleVersion": "string"
        },
        "execStatus": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试发布任务
def test_publish_task():
    url = f"{BASE_URL}/message/task/manage/publish"
    payload = {
        "id": 0,
        "taskCode": "string",
        "taskSource": 0,
        "allotTaskCode": "string",
        "allotTaskId": 0,
        "taskName": "string",
        "channelId": 0,
        "channelName": "string",
        "status": 0,
        "projectId": 0,
        "projectName": "string",
        "targetPlan": 0,
        "strategyTarget": 0,
        "planExplain": "string",
        "customerCount": 0,
        "seatCount": 0,
        "taskSort": 0,
        "tagFlag": 0,
        "actualEndTime": "string",
        "endType": 0,
        "execDays": 0,
        "createBy": "string",
        "createDate": "string",
        "updateBy": "string",
        "updateName": "string",
        "updateDate": "string",
        "taskStartTime": "string",
        "taskEndTime": "string",
        "qwAllotTaskVo": {
            "id": 0,
            "taskId": "string",
            "taskName": "string",
            "taskSource": 0,
            "allotScene": 0,
            "addWechatChannelCode": "string",
            "shortMsgCode": "string",
            "shortMsgChannelCode": "string",
            "allotType": 0,
            "taskType": 0,
            "ruleName": "string",
            "ruleId": 0,
            "status": 0,
            "updateBy": "string",
            "updateName": "string",
            "executionTime": "string",
            "executionStartTime": "string",
            "executionEndTime": "string",
            "executionType": 0,
            "executionDay": 0,
            "execTime": "string",
            "createBy": "string",
            "createDate": "string",
            "updateDate": "string",
            "groupConfig": [
                {
                    "groupCode": "string",
                    "groupType": 0,
                    "groupName": "string"
                }
            ],
            "userIds": ["string"],
            "ruleVersion": "string"
        },
        "execStatus": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试任务详情
def test_task_detail():
    url = f"{BASE_URL}/message/task/manage/detail"
    payload = {
        "id": 0,
        "taskCode": "string",
        "taskSource": 0,
        "allotTaskCode": "string",
        "allotTaskId": 0,
        "taskName": "string",
        "channelId": 0,
        "channelName": "string",
        "status": 0,
        "projectId": 0,
        "projectName": "string",
        "targetPlan": 0,
        "strategyTarget": 0,
        "planExplain": "string",
        "customerCount": 0,
        "seatCount": 0,
        "taskSort": 0,
        "tagFlag": 0,
        "actualEndTime": "string",
        "endType": 0,
        "execDays": 0,
        "createBy": "string",
        "createDate": "string",
        "updateBy": "string",
        "updateName": "string",
        "updateDate": "string",
        "taskStartTime": "string",
        "taskEndTime": "string",
        "qwAllotTaskVo": {
            "id": 0,
            "taskId": "string",
            "taskName": "string",
            "taskSource": 0,
            "allotScene": 0,
            "addWechatChannelCode": "string",
            "shortMsgCode": "string",
            "shortMsgChannelCode": "string",
            "allotType": 0,
            "taskType": 0,
            "ruleName": "string",
            "ruleId": 0,
            "status": 0,
            "updateBy": "string",
            "updateName": "string",
            "executionTime": "string",
            "executionStartTime": "string",
            "executionEndTime": "string",
            "executionType": 0,
            "executionDay": 0,
            "execTime": "string",
            "createBy": "string",
            "createDate": "string",
            "updateDate": "string",
            "groupConfig": [
                {
                    "groupCode": "string",
                    "groupType": 0,
                    "groupName": "string"
                }
            ],
            "userIds": ["string"],
            "ruleVersion": "string"
        },
        "execStatus": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试删除任务
def test_delete_task():
    url = f"{BASE_URL}/message/task/manage/delete"
    payload = {
        "id": 0,
        "taskCode": "string",
        "taskSource": 0,
        "allotTaskCode": "string",
        "allotTaskId": 0,
        "taskName": "string",
        "channelId": 0,
        "channelName": "string",
        "status": 0,
        "projectId": 0,
        "projectName": "string",
        "targetPlan": 0,
        "strategyTarget": 0,
        "planExplain": "string",
        "customerCount": 0,
        "seatCount": 0,
        "taskSort": 0,
        "tagFlag": 0,
        "actualEndTime": "string",
        "endType": 0,
        "execDays": 0,
        "createBy": "string",
        "createDate": "string",
        "updateBy": "string",
        "updateName": "string",
        "updateDate": "string",
        "taskStartTime": "string",
        "taskEndTime": "string",
        "qwAllotTaskVo": {
            "id": 0,
            "taskId": "string",
            "taskName": "string",
            "taskSource": 0,
            "allotScene": 0,
            "addWechatChannelCode": "string",
            "shortMsgCode": "string",
            "shortMsgChannelCode": "string",
            "allotType": 0,
            "taskType": 0,
            "ruleName": "string",
            "ruleId": 0,
            "status": 0,
            "updateBy": "string",
            "updateName": "string",
            "executionTime": "string",
            "executionStartTime": "string",
            "executionEndTime": "string",
            "executionType": 0,
            "executionDay": 0,
            "execTime": "string",
            "createBy": "string",
            "createDate": "string",
            "updateDate": "string",
            "groupConfig": [
                {
                    "groupCode": "string",
                    "groupType": 0,
                    "groupName": "string"
                }
            ],
            "userIds": ["string"],
            "ruleVersion": "string"
        },
        "execStatus": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试下线任务
def test_offline_task():
    url = f"{BASE_URL}/message/task/manage/offline"
    payload = {
        "id": 0,
        "taskCode": "string",
        "taskSource": 0,
        "allotTaskCode": "string",
        "allotTaskId": 0,
        "taskName": "string",
        "channelId": 0,
        "channelName": "string",
        "status": 0,
        "projectId": 0,
        "projectName": "string",
        "targetPlan": 0,
        "strategyTarget": 0,
        "planExplain": "string",
        "customerCount": 0,
        "seatCount": 0,
        "taskSort": 0,
        "tagFlag": 0,
        "actualEndTime": "string",
        "endType": 0,
        "execDays": 0,
        "createBy": "string",
        "createDate": "string",
        "updateBy": "string",
        "updateName": "string",
        "updateDate": "string",
        "taskStartTime": "string",
        "taskEndTime": "string",
        "qwAllotTaskVo": {
            "id": 0,
            "taskId": "string",
            "taskName": "string",
            "taskSource": 0,
            "allotScene": 0,
            "addWechatChannelCode": "string",
            "shortMsgCode": "string",
            "shortMsgChannelCode": "string",
            "allotType": 0,
            "taskType": 0,
            "ruleName": "string",
            "ruleId": 0,
            "status": 0,
            "updateBy": "string",
            "updateName": "string",
            "executionTime": "string",
            "executionStartTime": "string",
            "executionEndTime": "string",
            "executionType": 0,
            "executionDay": 0,
            "execTime": "string",
            "createBy": "string",
            "createDate": "string",
            "updateDate": "string",
            "groupConfig": [
                {
                    "groupCode": "string",
                    "groupType": 0,
                    "groupName": "string"
                }
            ],
            "userIds": ["string"],
            "ruleVersion": "string"
        },
        "execStatus": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试结束任务
def test_end_task():
    url = f"{BASE_URL}/message/task/manage/endTask"
    payload = {
        "id": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试修改任务排序
def test_update_task_sort():
    url = f"{BASE_URL}/message/task/manage/updateTaskSort"
    payload = {
        "id": 0,
        "taskSort": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试修改任务打标标识
def test_update_tag_flag():
    url = f"{BASE_URL}/message/task/manage/updateTagFlag"
    payload = {
        "id": 0,
        "tagFlag": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试查询团队跟进数据--汇总
def test_qry_team_data_summary():
    url = f"{BASE_URL}/message/task/manage/qryTeamDataSummary"
    payload = {
        "id": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试查询团队跟进数据--列表
def test_qry_team_data_list():
    url = f"{BASE_URL}/message/task/manage/qryTeamDataList"
    payload = {
        "pageSize": 20,
        "pageNo": 0,
        "id": 0,
        "userIdList": ["string"],
        "startFollowRate": 0,
        "endFollowRate": 0,
        "execStatus": 0,
        "startActualEndTime": "string",
        "endActualEndTime": "string",
        "endType": 0
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试查询坐席跟进数据--汇总
def test_qry_seat_data_summary():
    url = f"{BASE_URL}/message/task/manage/qrySeatDataSummary"
    payload = {
        "taskCode": "string",
        "userId": "string"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200

# 测试查询坐席跟进数据--列表
def test_qry_seat_data_list():
    url = f"{BASE_URL}/message/task/manage/qrySeatDataList"
    payload = {
        "pageSize": 20,
        "pageNo": 0,
        "taskCode": "string",
        "userId": "string",
        "customerId": "string",
        "followStatus": 0,
        "startLastFollowTime": "string",
        "endLastFollowTime": "string"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200