import wx

class MainFrame(wx.Frame):
    def __init__(self,p,t):
        wx.Frame.__init__(self,id=wx.ID_ANY,parent=p,title=t,size=(300,100))
        panel=wx.Panel(self,-1)
        self.button=wx.Button(panel,-1,u'单击我',pos=(50,20))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        self.clicked_times=0
    def OnClick(self,event):
        self.clicked_times=self.clicked_times+1
        self.button.SetLabel(u'单击成功（%d）'%self.clicked_times)
if __name__=='__main__':
    app=wx.App()
    frame=MainFrame(None,'button演示')
    frame.Show(True)
    app.MainLoop()