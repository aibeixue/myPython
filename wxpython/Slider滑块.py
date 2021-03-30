import wx

class MainFrame(wx.Frame):
    def __init__(self,p,t):
        wx.Frame.__init__(self,id=-1,parent=p,size=(400,500),title=t)
        panel=wx.Panel(self,-1)
        self.count=0
        slider1=wx.Slider(
            panel,
            -1,
            50,
            -10,
            100,
            pos=(20,20),
            size=(250,-1),
            style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS
        )
        slider1.SetBackgroundColour('yellow')
        slider1.SetTickFreq(10)
        slider2 = wx.Slider(panel,
                            -1,
                            25,
                            1,
                            100,
                            pos=(125, 70),
                            size=(-1, 250),
                            # 垂直滑块，wx.SL_VERTICAL表示这是垂直滑块
                            style=wx.SL_VERTICAL | wx.SL_AUTOTICKS)
        slider2.SetTickFreq(50)

if __name__=='__main__':
    app=wx.App(False)
    frame=MainFrame(None,'CheckBox复选框')
    frame.Show()
    app.MainLoop()


