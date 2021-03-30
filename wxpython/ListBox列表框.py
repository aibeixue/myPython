import wx

class MainFrame(wx.Frame):
    def __init__(self,p,t):
        wx.Frame.__init__(self,id=-1,parent=p,size=(260,300),title=t)
        panel=wx.Panel(self,-1)
        self.label1 = wx.StaticText(parent=panel,
                                    id=-1,
                                    size=(40, 58),
                                    label=u"地点:",
                                    pos=(10, 10))
        self.list1 = wx.ListBox(parent=panel,
                                id=-1,
                                size=(100, 68),
                                pos=(60, 10),
                                style=wx.LB_EXTENDED,
                                choices=[u"北京", u"上海", u"广州", u"深圳"])
if __name__=='__main__':
    app=wx.App(False)
    frame=MainFrame(None,'CheckBox复选框')
    frame.Show()
    app.MainLoop()


