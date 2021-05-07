import wx
import os


wildcard = u"Python 文件 (*.py)|*.py|"     \
           u"编译的 Python 文件 (*.pyc)|*.pyc|" \
           u" 垃圾邮件文件 (*.spam)|*.spam|"    \
           "Egg file (*.egg)|*.egg|"        \
           "All files (*.*)|*.*"

class FileDialog(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1)
        b1=wx.Button(self,-1,u'选择文件夹',(50,50))
        self.Bind(wx.EVT_BUTTON,self.OnButton1,b1)
        b2 = wx.Button(self, -1, u"保存文件",(50,90))
        self.Bind(wx.EVT_BUTTON, self.OnButton2,b2)

    def OnButton1(self, event):
        """"""
        dlg = wx.FileDialog(self, message=u"选择文件",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard=wildcard,
                            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)

        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()  # 返回一个list，如[u'E:\\test_python\\Demo\\ColourDialog.py', u'E:\\test_python\\Demo\\DirDialog.py']
            print
            paths
            for path in paths:
                print
                path  # E:\test_python\Demo\ColourDialog.py E:\test_python\Demo\DirDialog.py

        dlg.Destroy()

    def OnButton2(self, event):
        """"""
        dlg = wx.FileDialog(self, message=u"保存文件",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard=wildcard,
                            style=wx.SAVE)
        dlg.SetFilterIndex(0)  # 设置默认保存文件格式，这里的0是py，1是pyc
        dlg.ShowModal()
        dlg.Destroy()

if __name__ == '__main__':
    frame = wx.PySimpleApp()
    app = FileDialog()
    app.Show()
    frame.MainLoop()