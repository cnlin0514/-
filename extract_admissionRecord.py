'''
@Author: zjk
@Date: 2020-04-26 11:55:39
@LastEditTime: 2020-04-30 16:12:21
@LastEditors: zjk
@Description: 拉取入院记录中的信息，包括xml中his号，病历号，病案号等。
'''
import regex
from pyquery import PyQuery

def extract_text(file):

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



    try:
        # 入院病区
        admission_location = r'(<入院病区.*?>.*?</入院病区>)'
        admission_location_temp = regex.findall(admission_location, myhtml)
        admission_location = r'(?<=">).*?(?=(</入院病区>))'
        admission_location_temp = regex.search(admission_location,admission_location_temp[0])
        if admission_location_temp[0]:
            text.append(admission_location_temp[0])
        else:
            text.append('null')
    except:
        text.append('null')
        print("入院病区为空" + text[6])

    try:
        # 入院科室
        admission_location = r'(<入院科别.*?>.*?</入院科别>)'
        admission_location_temp = regex.findall(admission_location, myhtml)
        if admission_location_temp[0]:
            hospital_admission_depatrment = r'((?<=">).*?(?=</入院科别>))'
            hospital_admission = regex.findall(hospital_admission_depatrment, admission_location_temp[0])
            #print(hospital_admission[0])
            text.append(hospital_admission[0])
        else:
            text.append('null')
    except:
        text.append('null')
        print("入院科室为空" + text[6])

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
    # 不匹配xml
    htmlexecxml = r'</XML><XML id="1">.*?首次病程记录.*?</P>'
    wushi = regex.search(htmlexecxml, myhtml)
    try:
        if wushi:

            chiefandhistory = PyQuery(wushi[0])
            p1 = r'\n|:|：| |\t'
            chiefandhistory_clean = regex.sub(p1, '', str(chiefandhistory.text()))
            # 去除住院病人授权委托书
            #print(chiefandhistory_clean)

            weituo = '(?<=入院记录).*?(?=首次病程记录)'
            chiefandhistory_text = regex.search(weituo, chiefandhistory_clean)

            #print(chiefandhistory_text[0])

            # print(wushi)
            #
            # # 从主诉一直拉取到月经及婚育史（re方法）
            # wushizz = r'主诉.*?(?=((情况属实 患方签字)|(患方签字)|(患者签字)))'
            # chiefandhistory = regex.findall(wushizz, wushi)

            if chiefandhistory_text[0]:
                # 拉取姓名
                chief = regex.search(r'(?<=姓名).*?(?=出生地)', chiefandhistory_text[0])
                # print(chief[0])
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')
                # 拉取性别
                chief = regex.search(r'(?<=性别).*?(?=家庭住址)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                    # print(chief[0])
                else:
                    text.append('*')

                # 提取年龄
                chief = regex.search(r'(?<=年龄).*?(?=发病节气)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')
                # 拉取发病节气
                chief = regex.search(r'(?<=发病节气).*?(?=婚姻状况)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')

                # 拉取婚姻状况
                chief = regex.search(r'(?<=婚姻状况).*?(?=入院处时间)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')
                # 拉取入院处时间
                chief = regex.search(r'(?<=入院处时间).*?(?=民族)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')
                # 拉取民族
                chief = regex.search(r'(?<=民族).*?(?=记录时间)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')
                # 拉取记录时间
                chief = regex.search(r'(?<=记录时间).*?(?=职业)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')

                # 拉取主诉
                chief = regex.search(r'(?<=(主诉)|(主 诉)|(主[\t]*诉)).*?(?=现病史)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')

                # 拉取现病史
                hpi = regex.findall(r'(?<=现病史).*?(?=既往史)', chiefandhistory_text[0])
                if hpi:
                    text.append(hpi[0])
                else:
                    text.append('*')

                # 拉取既往史
                item = regex.findall(r'(?<=既往史).*?(?=个人史)', chiefandhistory_text[0])
                if item:
                    text.append(item[0])
                else:
                    text.append('*')

                # 拉取个人史
                item = regex.search(r'(?<=个人史).*?(?=(婚育及月经史)|(婚育史)|(婚育史)|(生育史)|(生育史)|(月经及婚育史)|(月经史及婚育史))',
                                    chiefandhistory_text[0])
                if item:
                    text.append(item[0])
                else:
                    text.append('*')

                # 拉取月经和婚育
                item = regex.search(r'(?<=(婚育及月经史)|(婚育史)|(生育史)|(月经及婚育史)|(月经史及婚育史)).*?(?=家族史)',
                                    chiefandhistory_text[0])
                if item:
                    text.append(item[0])
                else:
                    text.append('*')

                # 拉取家族史
                item = regex.findall(r'(?<=家族史).*?(?=情况属实)', chiefandhistory_text[0])
                if item:
                    text.append(item[0])
                else:
                    text.append('*')
                # 拉取中医望闻切诊
                item = regex.search(r'(?<=中医望、闻、切诊).*?(?=体格检查)', chiefandhistory_text[0])
                # print(chief)
                if item:
                    text.append(item[0])
                else:
                    text.append('*')
                # 拉取体格检查
                item = regex.search(r'(?<=体格检查).*?(?=辅助检查)', chiefandhistory_text[0])
                # print(chief)
                if item:
                    text.append(item[0])
                else:
                    text.append('*')
                # 拉取辅助检查
                item = regex.search(r'(?<=辅助检查).*?(?=初步诊断)', chiefandhistory_text[0])
                # print(chief)
                if item:
                    text.append(item[0])
                else:
                    text.append('*')

                #拉取初步诊断
                item = regex.search(r'(?<=初步诊断).*?(?=医师签名)', chiefandhistory_text[0])
                # print(chief)
                if item:
                    text.append(item[0])
                else:
                    text.append('*')
            else:
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
    except:
        print( '去除 xml error HIS id is '+ text[6])
    htmlfile.close()
    return text
