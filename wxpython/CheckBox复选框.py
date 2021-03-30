import wx

class MainFrame(wx.Frame):
    def __init__(self,p,t):
        wx.Frame.__init__(self,id=-1,parent=p,size=(260,300),title=t)
        panel=wx.Panel(self,-1)
        self.checkbox1=wx.CheckBox(parent=panel,id=-1,label=u'苹果',pos=(60,10),size=(120,18))
        self.checkbox2=wx.CheckBox(parent=panel,id=-1,label=u'香蕉',pos=(60,30),size=(120,18))
        self.checkbox3=wx.CheckBox(parent=panel,id=-1,label=u'梨子',pos=(60,50),size=(120,18))
if __name__=='__main__':
    app=wx.App(False)
    frame=MainFrame(None,'CheckBox复选框')
    frame.Show()
    app.MainLoop()


