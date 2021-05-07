import wx
import os


class DirDialog(wx.Frame):

    def __init__(self, parent, title):
        super(DirDialog, self).__init__(parent, title=title, size=(520, 400))

        panel = wx.Panel(self)
        box1 = wx.BoxSizer(wx.VERTICAL)

        self.label1 = wx.StaticText(panel, label="请选择文件所在的文件夹：", style=wx.ALIGN_CENTER)
        box1.Add(self.label1, 0, wx.EXPAND, 20)

        #按钮1
        self.btn1 = wx.Button(panel,-1,u"文件夹选择对话框")
        box1.Add(self.btn1, 0,wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON,self.OnBtn1,self.btn1)

        self.label2=wx.StaticText(panel, label="", style=wx.ALIGN_CENTER, size=(520,20))
        box1.Add(self.label2,0,wx.EXPAND,20)

        #文件路径label3
        self.label3 = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER, size=(520, 20))
        box1.Add(self.label3, 0, wx.EXPAND, 20)

        #按钮2
        self.btn2=wx.Button(panel,-1,u"点击处理文件")
        box1.Add(self.btn2, 0, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON,self.OnBtn2,self.btn2)

        #结果label4
        self.label4 = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER, size=(520, 100))
        box1.Add(self.label4, 0, wx.EXPAND, 20)


        panel.SetSizer(box1)

    def OnBtn1(self,event):
        dlg=wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal()==wx.ID_OK:
            self.label2.LabelText=f"你选择的文件夹是:"
            self.label3.LabelText=dlg.GetPath()
        dlg.Destroy()

    def OnBtn2(self,event):
        dir=self.label3.LabelText
        files=self.getFiles(dir)
        print(files)
        text=''
        for flie in files:
            fileDir = f'{dir}\\{flie}.nc'
            text+=fileDir+'  文件已经处理完毕！\n'
            self.modifyAndSave(fileDir)
        print(text)
        self.label4.LabelText = f'{text}'

    # 获取当前目录下的所有待处理的文件
    def getFiles(self,dir):
        files = os.listdir(dir)
        fileList = []
        for file in files:
            portion = os.path.splitext(file)
            if portion[1] == '.nc' and portion[0][0] == 'r' and len(portion[0]) == 8:
                fileList.append(portion[0])
        return fileList

    # 获取并处理所有文件中的数据，存到数组中
    def modifyAndSave(self,dir):
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
        # 把处理好的数据，写入文件
        with open(dir, 'w') as f2:
            text2 = ''.join([str(i) for i in mlist])
            f2.write(text2)
            # self.label4.LabelText=f'{dir} 文件已经处理完毕！'
            print(f'{dir} 文件已经处理完毕！')







if __name__=="__main__":
    app = wx.App()
    frame=DirDialog(None, title='选择文件所在文件夹')
    frame.Center()
    frame.Show()
    app.MainLoop()
