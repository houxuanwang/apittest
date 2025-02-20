from box import Box
import requests
from typing import Dict
from pathlib import Path
import os

HERE = os.path.abspath(os.path.dirname(__file__))


class InitDataService:
    """InitDataService for auto load json file services"""

    def __init__(self, group: str = None, response: requests.Response = None):
        """
        @param group:E.g.
        @param response: None
        """
        self.group = group
        self.response = response
        if self.group:
            self.cfg_datas = self.get_all_json(self.group)
        else:
            self.cfg_datas = self.get_all_json()

    def get_cfg_data(self, key: str) -> Box:
        """
        通过文件名获取对应配置数据
        @param key:
        @return:Box
        """
        return self.cfg_datas.get(key)

    def get_all_json(self, group: str = None) -> Dict[str, Box]:
        """
        读取所有配置文件以文件名作为key
        @param group:
        @return: {"AddFlash":{"id":1....}}
        """
        group = group or self.group
        json_data = Box({k: Box.from_json(filename=v) for k, v in self.find_all_json_files(group).items()})
        return json_data

    @staticmethod
    def find_all_json_files(group: str = None) -> dict:
        """
        获取指定模块testdata下所有配置文件
        @param group: e.g.
        @return:
        """
        if group:
            cfg_path = Path(HERE).parent / f"zijin_api_autotest/{group}/testdata/"
            assert cfg_path.is_dir(), f'不是有效的目录,请检查 group:{group},cfg_path:{cfg_path}'
        else:
            cfg_path = Path(HERE).parent / f"testdata/"

        json_files = {f.stem: f for f in cfg_path.rglob('*.json') if f.is_file()}
        assert len(json_files), f'没有发现可用配置文件,请检查!'
        return json_files


if __name__ == '__main__':
    bs = InitDataService()
    print(bs.find_all_json_files())
    # print(bs.get_all_json())
    # print(bs.cfg_datas)
    # print(bs.get_cfg_data('AddFlash').img)
