import wx
class ComboBoxFrameDemo1(wx.Frame):
    def __init__(self,p,t):
        wx.Frame.__init__(self,id=wx.NewId(),parent=p,size=(300,128),title=t)
        panel=wx.Panel(self,-1)
        self.label1=wx.StaticText(parent=panel,id=-1,size=(100,20),label=u'请选择第一候选人：',pos=(10,10))
        candidates = [u"张三", u"李四", u"王五", u"唐七", u"其他..."]
        self.combol=wx.ComboBox(parent=panel,id=-1,size=wx.DefaultSize,pos=(120,20),value='',choices=candidates,name=u'候选人名单')

if __name__=='__main__':
    app=wx.App(False)
    frame=ComboBoxFrameDemo1(None,'ComboBox下拉列表')
    frame.Show(True)
    app.MainLoop()