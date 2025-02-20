from pathlib import Path, PurePosixPath

import pytest
import os
import yaml
import logging.config
import sys

if __name__ == '__main__':

    yaml.warnings({'YAMLLoadWarning': False})
    package_path = str(Path().resolve())
    print(package_path)
    logging_cfg_file = PurePosixPath(str(package_path)).joinpath('logging.yaml')
    print(logging_cfg_file)
    with open(logging_cfg_file, 'r', encoding='utf-8') as logging_cfg:
        # logging_conf = yaml.load(logging_cfg, Loader=yaml.FullLoader)
        print(logging_cfg)
        print("1" * 100)
        # logging_conf = yaml.load(logging_cfg)
        logging_conf = yaml.load(logging_cfg, Loader=yaml.FullLoader)
        print(logging_conf)
        logging.config.dictConfig(logging_conf)

    logger = logging.getLogger(__name__)

    logger.info("*" * 100)

    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(['--alluredir', '../allure-results', '-m', 'L3'])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ../allure-results -o ../allure-report --clean')
