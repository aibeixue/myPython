import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'RadioBox单选框',size=(350,200))
        panel=wx.Panel(self,-1)
        sampleList1=['0','1','2','3','4','5','6','7','8']
        wx.RadioBox(panel,-1,'选择商品个数',(10,10),wx.DefaultSize,sampleList1,3,wx.RA_SPECIFY_COLS)
        sampleList2=[u'苹果',u'橘子',u'香蕉']
        wx.RadioBox(panel,-1,'选择商品种类',(150,10),wx.DefaultSize,sampleList2,3,wx.RA_SPECIFY_COLS|wx.NO_BORDER)
if __name__=='__main__':
    app=wx.App()
    frame=MainFrame()
    frame.Show(True)
    app.MainLoop()