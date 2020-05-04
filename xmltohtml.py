'''
@Author: zjk
@Date: 2020-04-26 10:54:18
@LastEditTime: 2020-04-26 19:10:27
@LastEditors: zjk
@Description: 转义并提取html
'''
from lxml import etree
import os
import sys
import regex

def xmltohtml(inputpath, outputpath):
# convert xmlfile to html
# htmlfile = open(path, 'r', encoding='utf-8')
    
    line1 = os.path.split(inputpath)[1]
    line2 = os.path.splitext(line1)[0]
    # print(line2)
    with open(inputpath, 'r', encoding='utf-8') as xmlread:
        xmltext = xmlread.read()
        # print(xmlfile)

    # 反转义
    xmlfile1 = regex.sub('&amp;','&', xmltext)
    xmlfile2 = regex.sub('&lt;','<', xmlfile1)
    xmlfile3 = regex.sub('&nbsp;','',xmlfile2)
    xmltext = regex.sub('&gt;','>', xmlfile3)

    p1 = r'<HTML>.*?</HTML>'

    result = regex.search(p1, xmltext)
    if result:
        newtext = result[0]
    else:
        newtext = "Null"
    # newtext = etree.HTML(newtext, parser=etree.HTMLParser(encoding='utf-8'))
    # newtext = etree.tostring(newtext)
    # save as html
    html_path = os.path.join(outputpath,line2)
    with open(html_path+".html",'w',encoding='UTF-8-sig') as f:
        f.write(newtext)