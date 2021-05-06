import wx
import demo
class CalcFrame(demo.MyFrame1):
   def __init__(self,parent):
      demo.MyFrame1.__init__(self,parent)

   def FindSquare(self,event):
      num = int(self.text1.GetValue())
      self.text2.SetValue (str(num*num))

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
#start the applications
app.MainLoop()