import os
import wx

#获取当前目录下的所有待处理的文件
def getFile(dir):
    files=os.listdir(dir)
    fileList=[]
    for file in files:
        portion=os.path.splitext(file)
        if portion[1] == '.nc' and portion[0][0]=='r' and len(portion[0])==8:
            fileList.append(portion[0])
    return fileList



#获取并处理所有文件中的数据，存到数组中
def modifyAndSave(dir):
    with open(dir, 'r') as f:
        text = f.read()
        # 清除文件内的空行
        text = ''.join([s for s in text.splitlines(True) if s.strip()])
        # 截取文件内容6块
        mlist = text.split('*')
        if len(mlist) == 6:
            # 把2、3段位置互换
            mlist[2], mlist[3] = mlist[3], mlist[2]
            # 文件内容顺序调整正确后，获取偶数段，删除段的第一行内容
            for i, item in enumerate(mlist):
                if i == 2 or i == 4:
                    lines = item.splitlines()
                    del lines[1]
                    lineStr = '\n'.join([str(s) for s in lines])
                    mlist[i] = lineStr
    #把处理好的数据，写入文件
    with open(dir, 'w') as f2:
        text2 = ''.join([str(i) for i in mlist])
        f2.write(text2)
        print(f'{dir} 文件已经处理完毕！')
        print('*************************************************')


if __name__ == '__main__':
    dir='D:\code\myPython'
    files=getFile(dir)
    for flie in files:
        fileDir=f'{dir}\\\{flie}.nc'
        modifyAndSave(fileDir)





