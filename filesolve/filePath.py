import wx


class DirDialog(wx.Frame):

    def __init__(self, parent, title):
        super(DirDialog, self).__init__(parent, title=title, size=(520, 220))
        panel = wx.Panel(self)
        box1 = wx.BoxSizer(wx.VERTICAL)

        self.label1 = wx.StaticText(panel, label="请选择文件所在的文件夹：", style=wx.ALIGN_CENTER)
        box1.Add(self.label1, 0, wx.EXPAND, 20)

        self.btn1 = wx.Button(panel,-1,u"文件夹选择对话框")
        box1.Add(self.btn1, 0,wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON,self.OnButton,self.btn1)

        self.label2=wx.StaticText(panel, label="请选择文件所在的文件夹：", style=wx.ALIGN_CENTER)
        box1.Add(self.label2,0,wx.EXPAND,20)

        panel.SetSizer(box1)

    def OnButton(self,event):
        dlg=wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal()==wx.ID_OK:
            self.label2.LabelText=f"你选择的文件夹是：\n{dlg.GetPath()}"
            print()
        dlg.Destroy()


if __name__=="__main__":
    app = wx.App()
    frame=DirDialog(None, title='选择文件所在文件夹')
    frame.Center()
    frame.Show()
    app.MainLoop()
