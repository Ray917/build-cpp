import wx
import os
import sys
from wx import stc

def load(event):
    if(filename.GetValue()=='设置'):
        file = open('.\\setting.txt')
        contents.SetValue(file.read())
        file.close()
    else:
        file = open(filename.GetValue())
        contents.SetValue(file.read())
        file.close()

def look(event):
    wildcard = 'C++ Source File (*.cpp)|*.cpp'
    dialog = wx.FileDialog(None,'选择文件',os.getcwd(),'',wildcard,wx.FD_OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        filename.SetValue(dialog.GetPath())
        dialog.Destroy
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    if(filename.GetValue()=='设置'):
        file = open('.\\setting.txt', 'w')
        file.write(contents.GetValue())
        file.close()
    else:
        file = open(filename.GetValue(), 'w')
        file.write(contents.GetValue())
        file.close()

def run(event):
    if(filename.GetValue()=='设置'):
        wx.MessageBox('嘛~ 发生了一个错误……\n\n“设置” 是不能Run的啊啊啊啊啊！！！！！')
    else:
        file = open(filename.GetValue(), 'w')
        file.write(contents.GetValue())
        file.close()
        os.system('start .\\run.exe '+chr(34)+filename.GetValue()+chr(34))

def she(event):
    filename.SetValue('设置')
    file = open('.\\setting.txt')
    contents.SetValue(file.read())
    file.close()

def end(event):
    sys.exit()

def about(event):
    wx.MessageBox('关于\n\n睿集团 Build-C++ 编程工具\n版本：1.0.0.00B81800202.2 64位\n\n官网：http://project.raygroup.rthe.net/build-cpp\nGitHub：https://github.com/Ray917/build-cpp\n反馈邮箱：ray_group@126.com\n\nCopyright 2020 RayGroup. All Rights Reserved.')

app = wx.App()
win = wx.Frame(None, title="睿集团 Build-C++ 编程工具", size=(1200, 750))
bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label='打开')
loadButton.Bind(wx.EVT_BUTTON, load)

lookButton = wx.Button(bkg,label='浏览')
lookButton.Bind(wx.EVT_BUTTON, look)

saveButton = wx.Button(bkg, label='保存')
saveButton.Bind(wx.EVT_BUTTON, save)

runButton = wx.Button(bkg, label='Run')
runButton.Bind(wx.EVT_BUTTON, run)

sheButton = wx.Button(bkg, label='设置')
sheButton.Bind(wx.EVT_BUTTON, she)

endButton = wx.Button(bkg, label='退出')
endButton.Bind(wx.EVT_BUTTON, end)

aboutButton = wx.Button(bkg, label='关于')
aboutButton.Bind(wx.EVT_BUTTON, about)

filename = wx.TextCtrl(bkg)
filename.SetValue('test.cpp')

contents = wx.stc.StyledTextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL | wx.TE_PROCESS_TAB | wx.TE_PROCESS_ENTER | wx.TE_LEFT | wx.TE_AUTO_URL | wx.TE_WORDWRAP)
contents.SetMarginType(1, stc.STC_MARGIN_NUMBER)        
contents.SetMarginWidth(1, 20)

file = open(filename.GetValue())
contents.SetValue(file.read())
file.close()

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(lookButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(runButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(sheButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(endButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(aboutButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1,
    flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
bkg.SetSizer(vbox)
win.Show()

if __name__ == "__main__":
    app.MainLoop()