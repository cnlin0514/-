# @time： 2020/5/11 16:06
# @description：拉取出院证明书



import regex
from pyquery import PyQuery

def extract_dischargeCertificate(file):

    with open(file, 'r', encoding='utf-8') as htmlfile:
        myhtml = htmlfile.read()

    # pandas数组暂存输出结果
    text = []
    # myhtml_b = bytes(bytearray(file, encoding='utf-8'))
    # myhtml = etree.HTML(myhtml)
    # result = myhtml.xpath('//*[@id="Mandala"]/table/tbody/tr[1]/td[1]/font/text()')
    # print(result)

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

    # 病案号
    his_record_number = r'<病案号.*?>.*?</病案号>'
    his_record_number_temp = regex.findall(his_record_number, myhtml)
    if his_record_number_temp:
        modified_number = r'\d{6}(?=</病案号>)'
        text.append(regex.findall(modified_number, his_record_number_temp[0])[0])
    else:
        text.append('null')

    # # 床号
    # his_record_number = r'<床号.*?>.*?</床号>'
    # his_record_number_temp = regex.findall(his_record_number, myhtml)
    # if his_record_number_temp:
    #     modified_number = r'(?<=">).*?(?=</床号>)'
    #     text.append(regex.findall(modified_number, his_record_number_temp[0])[0])
    # else:
    #     text.append('null')

    # # 住院号
    # his_record_number = r'<住院号.*?>.*?</住院号>'
    # his_record_number_temp = regex.findall(his_record_number, myhtml)
    # if his_record_number_temp:
    #     modified_number = r'(?<=>).*?(?=</住院号>)'
    #     text.append(regex.findall(modified_number, his_record_number_temp[0])[0])
    # else:
    #     text.append('null')

    # 病历号
    his_record_number = r'(?<=病历号:)\d{6}'
    his_record_number_temp = regex.findall(his_record_number, myhtml)
    if his_record_number_temp:
        text.append(his_record_number_temp[0])
    else:
        text.append('null')

    #拉取姓名
    age = r'(<姓名.*?>.*?</姓名>)'
    age_temp = regex.findall(age,myhtml)
    age = r'(?<=">).*?(?=(</姓名>))'
    age_temp = regex.search(age,age_temp[0])
    if age_temp[0]:
        text.append(age_temp[0])
    else:
        text.append('null')

    # #拉取年龄
    # age = r'(<年龄.*?>.*?</年龄>)'
    # age_temp = regex.findall(age,myhtml)
    # age = r'(?<=">).*?(?=(</年龄>))'
    # age_temp = regex.search(age,age_temp[0])
    # if age_temp[0]:
    #     text.append(age_temp[0])
    # else:
    #     text.append('null')


    # #拉取性别
    # age = r'(<性别.*?>.*?</性别>)'
    # age_temp = regex.findall(age,myhtml)
    # age = r'(?<=">).*?(?=(</性别>))'
    # age_temp = regex.search(age,age_temp[0])
    # if age_temp[0]:
    #     text.append(age_temp[0])
    # else:
    #     text.append('null')

    # try:
    #     # 出院病区
    #     admission_location = r'(<病区.*?>.*?</病区>)'
    #     admission_location_temp = regex.findall(admission_location, myhtml)
    #     admission_location = r'(?<=">).*?(?=(</病区>))'
    #     admission_location_temp = regex.search(admission_location,admission_location_temp[0])
    #     if admission_location_temp[0]:
    #         text.append(admission_location_temp[0])
    #     else:
    #         text.append('null')
    # except:
    #     text.append('null')
    #     print("出院病区为空" + text[6])

    try:
        # 出院科室
        admission_location = r'(<科别.*?>.*?</科别>)'
        admission_location_temp = regex.findall(admission_location, myhtml)
        if admission_location_temp[0]:
            hospital_admission_depatrment = r'((?<=">).*?(?=</科别>))'
            hospital_admission = regex.findall(hospital_admission_depatrment, admission_location_temp[0])
            #print(hospital_admission[0])
            text.append(hospital_admission[0])
        else:
            text.append('null')
    except:
        text.append('null')
        print("出院科室为空" + text[9])


    #不匹配xml
    htmlexecxml = r'</XML><XML id="2">.*?患者/委托人/受达人.*?</P>'
    wushi = regex.search(htmlexecxml, myhtml)

    try:
        if wushi:
            chiefandhistory = PyQuery(wushi[0])
            p1 = r'\n|:|：| |\t'
            chiefandhistory_clean = regex.sub(p1, '', str(chiefandhistory.text()))
            # 去除住院病人授权委托书
            # print(chiefandhistory_clean)
            weituo = r'(?<=出院证明书).*?(?=患者/委托人/受达人)'
            chiefandhistory_text = regex.search(weituo, chiefandhistory_clean)
            if chiefandhistory_text[0]:
                # 拉取入院日期
                chief = regex.search(r'(?<=入院日期).*?(?=出院日期)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')

                # 拉取出院日期
                chief = regex.search(r'(?<=出院日期).*?(?=住址/户口地址/单位)', chiefandhistory_text[0])
                # print(chief)
                if chief:
                    text.append(chief[0])
                else:
                    text.append('*')




                # 拉取出院诊断

                item = regex.findall(r'(?<=出院诊断).*?(?=住院诊疗经过)', chiefandhistory_text[0])
                if item:
                    text.append(item[0])
                else:
                    text.append('*')

                # 拉取住院诊疗经过
                item = regex.findall(r'(?<=住院诊疗经过).*?(?=出院带药)', chiefandhistory_text[0])
                if item:
                    text.append(item[0])
                else:
                    text.append('*')

                # 拉取出院带药
                item = regex.search(r'(?<=出院带药).*?(?=注意事项)', chiefandhistory_text[0])
                # print(chief)
                if item:
                    text.append(item[0])
                else:
                    text.append('*')
                # 拉取注意事项
                item = regex.search(r'(?<=注意事项).*?(?=医师签名)', chiefandhistory_text[0])
                # print(chief)
                if item:
                    text.append(item[0])
                else:
                    text.append('*')
                # # 拉取出院医嘱
                # item = regex.search(r'(?<=出院医嘱).*?(?=医师签名)', chiefandhistory_text[0])
                # # print(chief)
                # if item:
                #     text.append(item[0])
                # else:
                #     text.append('*')


            else:
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')
                text.append('null')

    except:
        print('去除 xml error HIS id is ' + text[0])
    htmlfile.close()
    return text
