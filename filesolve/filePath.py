import wx
import os


class DirDialog(wx.Frame):

    def __init__(self, parent, title):
        super(DirDialog, self).__init__(parent, title=title, size=(520, 400))
        panel = wx.Panel(self)
        box1 = wx.BoxSizer(wx.VERTICAL)

        self.label1 = wx.StaticText(panel, label="请选择文件所在的文件夹：", style=wx.ALIGN_CENTER)
        box1.Add(self.label1, 0, wx.EXPAND, 20)

        self.btn1 = wx.Button(panel,-1,u"文件夹选择对话框")
        box1.Add(self.btn1, 0,wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON,self.OnBtn1,self.btn1)

        self.label2=wx.StaticText(panel, label="", style=wx.ALIGN_CENTER,size=(220,60))
        box1.Add(self.label2,0,wx.EXPAND,20)
        self.label3 = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER, size=(220, 80))
        box1.Add(self.label3, 0, wx.EXPAND, 20)

        self.btn2=wx.Button(panel,-1,u"点击处理文件",style=wx.ALIGN_CENTER)
        box1.Add(self.btn2, 0, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON,self.OnBtn2,self.btn2)

        self.label4 = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER, size=(220, 100))
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
        print(self.label3.LabelText)

        #获取dir路径下的目标文件
        files = os.listdir(dir)
        fileList = []
        for file in files:
            portion = os.path.splitext(file)
            if portion[1] == '.nc' and portion[0][0] == 'r' and len(portion[0]) == 8:
                fileList.append(portion[0])
        print(fileList)






if __name__=="__main__":
    app = wx.App()
    frame=DirDialog(None, title='选择文件所在文件夹')
    frame.Center()
    frame.Show()
    app.MainLoop()
