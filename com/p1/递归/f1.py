import os
'''
递归遍历目录
'''
def getAllFires(path,sp):
    fileList = os.listdir(path)
    sp+="   "
    for fileName in fileList:
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录: " + fileName)
            getAllFires(fileAbsPath,sp)
        else:
            print(sp + "普通文件："  + fileName)
# getAllFires("/Users/ywh/CODESRC"," ")
'''
深度遍历
'''
def getAllPathDeep(path):
    stack = []
    stack.append(path)
    while len(stack) !=0:
        dirPath=stack.pop()
        filesList = os.listdir(dirPath)
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                stack.append(fileAbsPath)
                print("目录：" + fileName)
            else:
                print( "普通文件："  + fileName)

getAllPathDeep("/Users/ywh/CODESRC")