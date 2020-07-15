'''
@Author: zjk
@Date: 2020-04-26 09:43:48
@LastEditTime: 2020-04-30 12:19:08
@LastEditors: zjk
@Description: 读取外层xml文件并抽取内层html，提取主诉等内容
'''


from lxml import etree
import os
import sys
import shutil
import regex
import pymysql
from traverse import gethtml, getxml
from xmltohtml import xmltohtml
from extract_admissionRecord import extract_text
from extract_dischargeRecord import extract_dischargeRecord
from extrac_dischargeRecord_2 import extract_dischargeRecord2
from extract_firstCourseRecord import extract_firstCourseRecord
from extract_dischargeCertificate import extract_dischargeCertificate
from ToDatabase import *
from tqdm import tqdm


# xml files dir
input_dir = "G:\毕业设计\中医药大学数据9068\Data1"
destination_dir = "./Data2"
# destination_dir = "./data"
# destination_dir ="./Data4"
error_dir = "./首次病程记录error"
index = 0

file_xml = getxml(input_dir)

#转义初次使用时，讲源数据xml格式中的转义字符转化为html格式
# for line in file_xml:
#     xmltohtml(line,destination_dir)

file_html = gethtml(destination_dir)

i = 0
for file in tqdm(file_html):
    # item_list = extract_text(file)#入院记录
    # item_list = extract_dischargeRecord2(file)#出院记录
    # item_list = extract_dischargeCertificate(file)#出院证明书
    item_list = extract_firstCourseRecord(file)  #首次病程记录


    index = index + 1


    try:
        insert_database(index, item_list)
    except Exception as e:
        i = i + 1
        # print('insert error : HIS id is ' + item_list[6])#入院记录
        # print('insert error : HIS id is ' + item_list[9])#出院记录
        # print('insert error : HIS id is ' + item_list[0])#出院证明书
        print('insert error : HIS id is ' + item_list[0])#首次病程记录


        print(e)
        
        # save files with error to the error_dir,将错误文件复制到error_dir
        if not os.path.exists(error_dir):
            os.makedirs(error_dir)
        try:
            fpath,fname=os.path.split(file)
            f_dst = os.path.join(error_dir, fname)
            shutil.copy(file, f_dst)
        except Exception as e:
            print('move_file ERROR:',e)

print('error num : ' + str(i))
connection.close()

    #将结果保存在本地
    # with open('result.output','a+',encoding='utf-8') as f:
    #     output = extract_text(file)
    #     for item in output:
    #         f.write(item)
    #         f.write(',')
    #     f.write('\n')
