import wx
import datetime

class FirstFrame(wx.Frame):
    def __init__(self,*args,**kwargs):
        super(FirstFrame, self).__init__(*args,**kwargs)
        panel=wx.Panel(parent=self)
        # text=wx.StaticText(parent=panel,label='coolpython.net',pos=(100,30))
        # text.SetForegroundColour((255,0,0))
        self.text=wx.StaticText(parent=panel,label=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),pos=(50,30))
        #设置字体
        font=wx.Font(15,wx.MODERN,wx.NORMAL,wx.NORMAL,False,'Consolas')
        self.text.SetFont(font)
        #设置字体颜色：绿色
        self.text.SetForegroundColour((0,255,0))
        #设置背景颜色：黑色
        self.text.SetBackgroundColour((0,0,0))
        self.timer=wx.Timer(owner=self)
        #绑定事件
        self.Bind(wx.EVT_TIMER,self.on_timer,self.timer)
        #每隔一秒触发一次事件
        self.timer.Start(1000)

def on_timer(self,evt):
    timer_now=datetime.datetime.now()
    time_str=timer_now.strftime('%Y-%m-%d %H:%M:%S')
    self.text.SetLabel(time_str)

def main():
    app=wx.App()
    ff=FirstFrame(None,title='我的第一个桌面软件',size=(300,320))
    ff.Show()
    ff.Center()
    app.MainLoop()

if __name__=='__main__':
    main()

