'''
@Author: zjk
@Date: 2020-04-26 11:55:39
@LastEditTime: 2020-04-30 16:12:21
@LastEditors: zjk
@Description: 抽取主诉、病史、病案号等
'''
import regex
# import pandas as pd
# import numpy as np
from lxml import etree
from pyquery import PyQuery


def extract_text(file):
    
    # print(file)
    # myhtml = etree.HTML(file)
    with open(file, 'r', encoding='utf-8') as htmlfile:
        myhtml = htmlfile.read()

    # pandas数组暂存输出结果
    text = []
    # myhtml_b = bytes(bytearray(file, encoding='utf-8'))
    # myhtml = etree.HTML(myhtml)
    # result = myhtml.xpath('//*[@id="Mandala"]/table/tbody/tr[1]/td[1]/font/text()')
    # print(result)

    # 病案号
    his_record_number = r'<病案号.*?>.*?</病案号>'  
    his_record_number_temp = regex.findall(his_record_number, myhtml)
    if his_record_number_temp:
        modified_number = r'\d{6}(?=</病案号>)'
        text.append(regex.findall(modified_number, his_record_number_temp[0])[0])
    else:
        text.append('null')

    # 就诊号
    his_record_number = r'<就诊号.*?>.*?</就诊号>'  
    his_record_number_temp = regex.findall(his_record_number, myhtml)
    if his_record_number_temp:
        modified_number = r'(?<=>).*?(?=</就诊号>)'
        text.append(regex.findall(modified_number, his_record_number_temp[0])[0])
    else:
        text.append('null')
    
    # 住院号
    his_record_number = r'<住院号.*?>.*?</住院号>'  
    his_record_number_temp = regex.findall(his_record_number, myhtml)
    if his_record_number_temp:
        modified_number = r'(?<=>).*?(?=</住院号>)'
        text.append(regex.findall(modified_number, his_record_number_temp[0])[0])
    else:
        text.append('null')

     # 病历号
    his_record_number = r'(?<=病历号:)\d{6}'  
    his_record_number_temp = regex.findall(his_record_number, myhtml)
    if his_record_number_temp:
        text.append(his_record_number_temp[0])
    else:
        text.append('null')
    



    # HIS内部标识
    medical_record_number = r'<HIS内部标识.*?>.*?</HIS内部标识>'
    medical_record_number_temp = regex.findall(medical_record_number, myhtml)
    if medical_record_number_temp:
        modified_number = r'(?<=>).*?(?=</HIS内部标识>)'
        # print("病案号：", regex.findall(modified_number, medical_record_number_temp[0]))
        text.append(regex.findall(modified_number, medical_record_number_temp[0])[0])
    else:
        # print("病案号：", "*")
        text.append('null')

    try:
        # 不匹配xml
        htmlexecxml = r'</XML><XML id="1">.*?家族史.*?</P>'
        wushi = regex.search(htmlexecxml, myhtml)
        #print(wushi)

        chiefandhistory = PyQuery(wushi[0])

        # print(wushi)
        #
        # # 从主诉一直拉取到月经及婚育史（re方法）
        # wushizz = r'主诉.*?(?=((情况属实 患方签字)|(患方签字)|(患者签字)))'
        # chiefandhistory = regex.findall(wushizz, wushi)

        if chiefandhistory:
            chiefandhistory_text = PyQuery(chiefandhistory[0])
            if chiefandhistory_text.text():
                # clean the chief and history compliant text, get rid of \n,:,：
                p1 = r'\n|:|：| |\t'
                chiefandhistory_clean = regex.sub(p1, '', str(chiefandhistory_text.text()))
                # print(chiefandhistory_clean)
                if chiefandhistory_clean:

                    # 拉取主诉
                    chief = regex.search(r'(?<=(主诉)|(主 诉)|(主[\t]*诉)).*?(?=现病史)', chiefandhistory_clean)
                    # print(chief)
                    if chief:
                        text.append(chief[0])
                    else:
                        text.append('*')

                    # 拉取现病史
                    hpi = regex.findall(r'(?<=现病史).*?(?=既往史)', chiefandhistory_clean)
                    if hpi:
                        text.append(hpi[0])
                    else:
                        text.append('*')

                    # 拉取既往史
                    item = regex.findall(r'(?<=既往史).*?(?=个人史)', chiefandhistory_clean)
                    if item:
                        text.append(item[0])
                    else:
                        text.append('*')

                    # 拉取个人史
                    item = regex.search(r'(?<=个人史).*?(?=(婚育及月经史)|(婚育史)|(婚育史)|(生育史)|(生育史)|(月经及婚育史)|(月经史及婚育史))',
                                        chiefandhistory_clean)
                    if item:
                        text.append(item[0])
                    else:
                        text.append('*')

                    # 拉取月经和婚育
                    item = regex.search(r'(?<=(婚育及月经史)|(婚育史)|(生育史)|(月经及婚育史)|(月经史及婚育史)).*?(?=家族史)',
                                        chiefandhistory_clean)
                    if item:
                        text.append(item[0])
                    else:
                        text.append('*')

                    # 拉取家族史
                    item = regex.findall(r'(?<=家族史).*', chiefandhistory_clean)
                    if item:
                        text.append(item[0])
                    else:
                        text.append('*')
                else:
                    text.append('null')
        else:
            text.append('null')
            text.append('null')
            text.append('null')
            text.append('null')
            text.append('null')
            text.append('null')
            text.append('null')
            text.append('null')
    except:
        print( '去除 xml error HIS id is '+ text[1])

    htmlfile.close()
    return text
