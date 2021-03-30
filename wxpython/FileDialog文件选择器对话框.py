import wx

class MainFrame(wx.Frame):
    def __init__(self,p,t):
        wx.Frame.__init__(self,id=-1,parent=p,size=(260,300),title=t)
        panel=wx.Panel(self,-1)
        fileDialog=wx.FileDialog()
if __name__=='__main__':
    app=wx.App(False)
    frame=MainFrame(None,'CheckBox复选框')
    frame.Show()
    app.MainLoop()


