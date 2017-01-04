# -*- coding: utf-8 -*-
# __author__ = 'eacaen'

import wx
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title='hello')
        frame.Show()
        return True



class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent = superior,title = 'Example',\
                          pos = (100,200),size = (200,100))
        panel = wx.Panel(self)
        text1 = wx.TextCtrl(panel , value = 'hello',\
                            size = (200,150))

if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()
