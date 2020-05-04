'''
@Author: zjk
@Date: 2020-04-27 11:36:44
@LastEditTime: 2020-04-27 13:10:52
@LastEditors: zjk
@Description: 批量写入数据库
'''
import pymysql
from variables import workstation_host, workstation_passwd, workstation_user,workstation_port

connection = pymysql.connect(host=workstation_host,
                                 port=workstation_port,
                                 user='root',
                                 password=workstation_passwd,
                                 db='xyl',
                                 charset='utf8')

def insert_database(index, list):
    # effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))
    cursor = connection.cursor()
    effect_row1 = cursor.execute('INSERT INTO `medical_EHR` (`HIS`,`BAH`,`BLH`,`ZYH`,`JZH`,`Chief_complaint`,`HPI`,`Past_history`,`Personal_history`,`HYS`,`family_history`) VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s)',(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10]))
    #effect_row2 = cursor.execute('INSERT INTO `medical_EHR` (`id`,`BAH`,`HIS`,`Chief_complaint`) VALUES ( %s, %s, %s, %s)', (str(index),list[0],list[1],list[2]))
    #effect_row3 = cursor.execute('INSERT INTO `medical_EHR` (`gerenshi`,`hunyushi`) VALUES (%s, %s)', (list[5],list[6]))
    connection.commit()
