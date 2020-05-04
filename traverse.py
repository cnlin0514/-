'''
@Author: zjk
@Date: 2020-04-26 10:19:05
@LastEditTime: 2020-04-26 13:34:01
@LastEditors: zjk
@Description: 批量读取xml、html文件
'''


# dir = "./Data1"
#使用listdir循环遍历
def getxml(dir):
    import os
    path = []
    if not os.path.isdir(dir):
        print(dir)
        path = dir
    dirlist = os.walk(dir)
    for root, dirs, files in dirlist:
        for file in files:
            if file.endswith(".xml"):
                path.append(os.path.join(root, file))
    with open("./XMLfilename.txt", 'w', encoding='utf-8') as f:
        for line in path:
            f.write(line)
            f.write('\n')
    return path

# dir = "./Data1"
#使用listdir循环遍历
def gethtml(dir):
    import os
    path = []
    if not os.path.isdir(dir):
        print(dir)
        path = dir
    dirlist = os.walk(dir)
    for root, dirs, files in dirlist:
        for file in files:
            if file.endswith(".html"):
                path.append(os.path.join(root, file))
    with open("./HTMLfilename.txt", 'w', encoding='utf-8') as f:
        for line in path:
            f.write(line)
            f.write('\n')
    return path