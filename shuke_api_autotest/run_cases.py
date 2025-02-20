from pathlib import Path, PurePosixPath
import pytest
import os
import yaml
import logging.config
import sys

if __name__ == '__main__':
    yaml.warnings({'YAMLLoadWarning': False})  # 加载yaml文件时，看有些不影响功能的警告，但我不想看到他，把警告关掉
    package_path = Path().resolve()  # 获取绝对路径
    logging_cfg_file = package_path.joinpath('logging.yaml')  # 获取yaml文件的路径
    
    with open(logging_cfg_file, 'r', encoding='utf-8') as logging_cfg:
        logging_conf = yaml.load(logging_cfg, Loader=yaml.FullLoader)
        logging.config.dictConfig(logging_conf)

    logger = logging.getLogger(__name__)
    logger.info("*" * 100)

    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    #pytest_args = ['--alluredir', '../allure-results', '-m', 'L4 or L0 or L1 or L2 or L3']
    pytest_args = ['--alluredir', '../allure-results', '-m', 'L9']

    pytest.main(pytest_args)

    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    os.system('allure generate ../allure-results -o ../allure-report --clean')