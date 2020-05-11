'''
@Author: zjk
@Date: 2020-04-27 11:36:44
@LastEditTime: 2020-04-27 13:10:52
@LastEditors: zjk
@Description: 批量写入数据库
'''
import pymysql
from variables import workstation_host, workstation_passwd, workstation_user, workstation_port

connection = pymysql.connect(host=workstation_host,
                             port=workstation_port,
                             user='root',
                             password=workstation_passwd,
                             db='zjkhmr',
                             charset='utf8')


def insert_database(index, list):
    # effect_row = cursor.execute('INSERT INTO `users` (`name`, `age`) VALUES (%s, %s)', ('mary', 18))
    cursor = connection.cursor()

    #入院记录中所有字段入库
    # effect_row1 = cursor.execute(
    #     'INSERT INTO `hospital_admission_record` (`his`,`bah`,`blh`,`zyh`,`jzh`,`name`,`age`,`gender`,`nation`,`marial_status`,'
    #     '`onset_solar_term`,`admission_time`,`record_time`,`hospital_admit_location`,`hospital_admit_department`,'
    #     '`chief_complaint`,`present_history`,`past_history`,`personal_history`,`menstrual_history`,`family_history`,'
    #     '`chinese_medicine_diagnosis`,`physical_examination`,`auxiliary_examination`,`primary_diagnosis`) '
    #     'VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
    #     (list[6], list[0], list[3], list[2], list[1], list[7], list[9], list[8], list[13], list[11], list[10], list[12],
    #      list[14], list[4], list[5], list[15],list[16], list[17], list[18], list[19], list[20], list[21], list[22],
    #      list[23], list[24]))

    #出院记录所有字段入库

    effect_row1 = cursor.execute(
        'INSERT INTO `discharge_record` (`his`,`bah`,`blh`,`zyh`,`ch`,`name`,`age`,`gender`,`admission_time`,`discharge_time`,`hospital_discharge_location`,`hospital_discharge_department`,'
        '`operation_time`,`operation_name`,`admission_statu`,`admission_diagnosis`,`treatment_process`,`discharge_diagnosis`,`discharge_statu`,`discharge_order`) '
        'VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (list[9], list[0], list[3], list[2], list[1], list[4], list[5], list[6], list[10], list[11],list[7], list[8], list[12],
         list[13], list[14], list[15], list[16],list[17], list[18], list[19]))


    connection.commit()
