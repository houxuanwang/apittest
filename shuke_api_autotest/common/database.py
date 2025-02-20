import logging

import records
from box import BoxList
from records import Database
from retrying import retry

#from zijin_api_autotest.shuke_settings import db_global_config, DB_RETRY

logger = logging.getLogger(__name__)


# @singleton
class DataBase(Database):
    def __init__(self, _db_config='sit_db', **kwargs):
        """
        数据库操作
        :param _db_config dict or string
        e.g.
            _db_config = {'host': '', ....}
            _db_config = 'mysql://172.16.101.1 :password@host:port/database'
        数据库配置 dialect+driver://username:password@host:port/database
        """

        if isinstance(_db_config, dict) and _db_config is not None:
            self.database_url = self.build_sql_url(_db_config)
        elif isinstance(_db_config, str):
            self.database_url = self.build_sql_url(db_global_config.get(_db_config))
        else:
            raise Exception(f'Invalid db_cfg:{_db_config}')

        logger.info(f'[数据库配置]：{self.database_url}')
        super().__init__(self.database_url, **kwargs)

    @retry(stop_max_attempt_number=DB_RETRY)
    def execute_sql(self, query: str, fetchall=False, need_retry=True, **params) -> records.RecordCollection:
        """
        【update delete insert 使用本方法】

        @return list
        e.g.
            rows = db.execute_sql(select * from test)
            name = rows[0].name
            email = rows[0].email
        """
        logger.info(f'[准备执行sql]：{query}')
        try:
            execute_result = self.query(query, fetchall=fetchall, **params)
        except Exception as e:
            pass
            #assert False, f'[执行sql失败]:{query},{e}'
        else:
            logger.info(f'[执行sql成功]!:{execute_result}')
            return execute_result

    def execute_sql2dict(self, query: str, fetchall=False, need_retry=True, **params) -> BoxList:
        """
        【仅限于select操作】

        执行sql且返回Box对象，可以通过点号访问属性
        @query:str db sql
        @fetchall: bool Fetch all results if desired.
        return dict
        e.g.
            r = BoxList([{'uid':1, 'b': {'c':1}, 'c':[1,2,3]}])
            uid = r[0].uid
        """
        execute_result = BoxList(self.execute_sql(query, fetchall=fetchall, **params, need_retry=need_retry).as_dict())
        return execute_result

    @classmethod
    def change_db(cls, db_name: str):
        """
        用于更换数据库，一般用于更好数据库名字时使用
        @db_name:str
        """
        logger.info(f'[重建db实例,数据库配置]：{db_name}')
        return cls(db_name)

    def build_sql_url(self, db_dict: dict) -> str:
        user = db_dict.get('user')
        password = db_dict.get('password')
        host = db_dict.get('host')
        _db = db_dict.get('db')
        port = db_dict.get('port') or 3306
        if _db:
            database_url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{_db}?charset=utf8'
        else:
            database_url = f'mysql+pymysql://{user}:{password}@{host}:{port}'
        return database_url


if __name__ == '__main__':
    db_config = {
        "host": "10.220.185.210",
        "port": 3307,
        "user": "capitalms",
        "password": "7b7f2f28384788bd"
    }

    db = DataBase(db_config)
    # db = DataBase(db_cfg)
