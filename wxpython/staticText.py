import wx
class StaticTextDemo1(wx.Frame):            # 定义自己的Frame类
    def __init__(self):                        # 初始化函数
        wx.Frame.__init__(self,
                          None,
                          wx.ID_ANY,
                          "StaticText演示1",
                          size =(400, 400))
        panel = wx.Panel(self, -1)
        #基本静态的文本
        text1 = wx.StaticText(panel,
                              wx.ID_ANY,
                              "这是个基本的静态文本。",
                              (0, 0))
        #为文本指定前景色和背景色
        text2 = wx.StaticText(panel,
                              wx.ID_ANY,
                              "指定文本前景和背景色",
                              (50, 20))
        text2.SetForegroundColour("White")        # 设定前景色为白色
        text2.SetBackgroundColour("Black")        # 设置背景色为黑色
        #指定居中对齐
        text = wx.StaticText(panel, wx.ID_ANY, "居中对齐", (100,40),
             (100, 30),\
                                wx.ALIGN_CENTER)
        text.SetForegroundColour("White")
        text.SetBackgroundColour("Black")
        #指定右对齐
        text3 =wx.StaticText(panel,
                             wx.ID_ANY,
                             "居右对齐",
                             (100,70),
                             (160, -1),
                             wx.ALIGN_RIGHT)
        text3.SetBackgroundColour('yellow')
        #指定字体的静态文本的font
        text4 = wx.StaticText(panel,
                              wx.ID_ANY,
                              "设置文本font",
                              (20,150))
       # 设定字体
        font=wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text4.SetFont(font)
        #设置显示多行文本
        multiStr ="现在你看到\n的是多行\n文本"
        text5 = wx.StaticText(panel,
                              wx.ID_ANY,
                              multiStr,
                              (20, 200))
if __name__ == '__main__':
    app = wx.App()
    frame = StaticTextDemo1()
    frame.Show(True)
    app.MainLoop()