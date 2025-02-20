import csv
import json
import logging

import yaml

from pathlib import Path
file_path_root = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)


class FileUtils:
    """
    读写文件
    """

    def __init__(self, file_path, data=None, file_type='', mode='w'):
        # 文件路径
        self.file_path = file_path_root.joinpath(file_path)
        # 写入数据
        self.data = data
        # 文件类型
        self.file_type = self.file_path.suffix[1:] if not file_type else file_type
        # 文件读写模式
        self.mode = mode

    def common_read_file(self):
        """
        读取文件
        @return file_data: 返回读取结果，文件中没有内容则返回None
        """
        if self.file_type == 'json':
            file_data = self.__read_file_json()
        elif self.file_type == 'csv':
            file_data = self.__read_file_csv()
        elif self.file_type == 'txt':
            file_data = self.__read_file_txt()
        elif self.file_type == 'yaml':
            file_data = self.__read_file_yaml()
        else:
            assert False, f"您写的文件类型不包含在'json,csv,txt,yaml'中，暂不支持哦"

        return file_data

    def common_write_file(self):
        """
        写入文件
        """
        # 判断是否有文件路径，没有就创建，有就跳过
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self.file_path.touch()
        logger.info(f"创建{self.file_path}文件成功或已存在")

        if self.file_type in ('json', 'txt'):
            self.__write_file_json_or_txt()
        elif self.file_type == 'csv':
            self.__write_file_csv()
        elif self.file_type == 'yaml':
            self.__write_file_yaml()
        else:
            assert False, f"您写的文件类型不包含在'json,csv,txt,yaml'中，暂不支持哦"

    def __read_file_json(self):
        """
        json文件读取
        @return: 读取json文件内容
        """
        with open(str(self.file_path)) as f:
            try:
                file_json = json.load(f)
                logger.info(f"读取{self.file_path}文件成功：{file_json}")
            except json.decoder.JSONDecodeError:
                file_json = {}
        return file_json

    def __read_file_csv(self):
        """
        csv文件读取
        @return: 读取csv文件内容
        """
        file_csv_data = []
        with open(str(self.file_path), encoding='utf8') as f:
            file_csv = csv.reader(f, delimiter='\t')
            for row in file_csv:
                file_csv_data.extend(row)
            logger.info(f"读取{self.file_path}文件成功：{file_csv}")

        return file_csv_data

    def __read_file_txt(self):
        """
        txt文件读取
        @return: 读取txt文件内容
        """
        file_txt = self.file_path.read_text(encoding='utf8')
        logger.info(f"读取{self.file_path}文件成功：{file_txt}")

        return file_txt

    def __read_file_yaml(self):
        """
        yaml文件读取
        """
        with open(str(self.file_path), encoding='utf8') as f:
            res = yaml.load(f)
            return res

    def __write_file_json_or_txt(self):
        """
        json和txt文件写入
        """
        with open(str(self.file_path), mode=self.mode, encoding='utf8') as f:
            if isinstance(self.data, dict):
                self.data = json.dumps(self.data)
            f.write(self.data)
            logger.info(f"{self.data}写入{self.file_path}文件成功")

    def __write_file_csv(self):
        """
        csv文件写入
        """
        with open(str(self.file_path), mode=self.mode, encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            if isinstance(self.data, list):
                for row in self.data:
                    writer.writerow([row])
            else:
                writer.writerow(self.data)

    def __write_file_yaml(self):
        """
        yaml文件写入
        """
        with open(str(self.file_path), mode=self.mode, encoding='utf8') as f:
            res = yaml.dump(self.data, f)
            return res
