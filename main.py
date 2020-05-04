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
from extract_text import extract_text
from ToDatabase import *
from tqdm import tqdm
# import csv
# import numpy as np
# import pandas as ps

# xml files dir
input_dir = "F:/毕业设计/2.病历分割提取/脚本/Data1"
# desitination html path dir
destination_dir = "./Data2"
# error file dir
error_dir = "./Data3"
index = 0

file_xml = getxml(input_dir)

#转义
for line in file_xml:
    xmltohtml(line,destination_dir)

file_html = gethtml(destination_dir)

i = 0
for file in tqdm(file_html):
    item_list = extract_text(file)
    index = index + 1

    # insert_database(index, item_list)

    try:
        insert_database(index, item_list)
    except Exception as e:
        i = i + 1
        print('insert error : HIS id is ' + item_list[1])
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


    # with open('result.output','a+',encoding='utf-8') as f:
    #     output = extract_text(file)
    #     for item in output:
    #         f.write(item)
    #         f.write(',')
    #     f.write('\n')
