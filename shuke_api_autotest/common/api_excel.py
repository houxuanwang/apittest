import logging
import pandas as pd

logger = logging.getLogger(__name__)


def edit_excel(filedir='1.xlsx', locater=12, value='2021-08-22', sheet_name='importTemplate'):
    """
        修改表头 传入：文件路径（区分windows和linux），需要修改的位置（如10：第10列表头），修改后的值，表名

    :param filedir:
    :param locater:
    :param value:
    :return:
    """
    locater1 = locater
    locater = locater - 1
    df = pd.read_excel(filedir)
    old_value = df.columns[locater]
    df.rename(columns={df.columns[locater]: value}, inplace=True)
    new_value = df.columns[locater]
    df.to_excel(filedir, index=False, header=True, sheet_name=sheet_name)
    #df = pd.read_excel(filedir)
    logger.info(f'[{filedir}文件修改成功, 第{locater1}列--原值:{old_value} == 现值:{new_value}]')
    #print(f'[{filedir}文件修改成功, 第{locater1}列--原值:{old_value} == 现值:{new_value}]')


def edit_excel1(filedir='1.xlsx', col='存款类型', locater=1, value='包头', sheet_name='importTemplate'):
    """
        修改表头 传入：文件路径（区分windows和linux），需修改的行名称，需要修改的行位置（如1：第1行），修改后的值,那张表

    :param filedir:
    :param locater:
    :param value:
    :return:
    """
    df = pd.read_excel(filedir)
    old_value = df.loc[locater - 1, col]
    df[col] = df[col].astype(str)
    df.loc[locater - 1, col] = value
    df.to_excel(filedir, index=False, header=True, sheet_name=sheet_name)
    logger.info(f'[{filedir}文件修改成功, {col}第{locater}行--原值:{old_value} == 现值:{value}]')


