import wx

class MainFrame(wx.Frame):
    def __init__(self,p,t):
        wx.Frame.__init__(self,id=-1,parent=p,title=t,size=(700,700))
        panel=wx.Panel(self,-1)
        bmp=wx.Image('../images/flower.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button=wx.BitmapButton(panel,-1,bmp,pos=(10,10))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        self.button.SetDefault()
    def OnClick(self,event):
        self.Destroy()
if __name__=='__main__':
    app=wx.App()
    frame=MainFrame(None,'BitmapButton图片按钮演示')
    frame.Show()
    app.MainLoop()
