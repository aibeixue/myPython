import wx
from mainFrame import MainFrame
import sys


## @detail ShellApp主应用程序的核
class ShellApp(wx.App):

    def OnInit(self):
        mainFrame = MainFrame()
        mainFrame.Show(True)
        return True


# @detail main程序的主入口程序
if __name__ == '__main__':
    app = ShellApp()
    # 重新定向wxpython的输出输入和错误输出到系统标准输入输出
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    app.MainLoop()
