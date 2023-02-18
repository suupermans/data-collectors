import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import sys
#导入爬虫的包
import b站
import weibo
import kuaishou
import 小红书

class myStdout():  # 重定向类
    def __init__(self):
        # 将其备份
        self.stdoutbak = sys.stdout
        self.stderrbak = sys.stderr
        # 重定向
        sys.stdout = self
        sys.stderr = self

    def write(self, info):
        # info信息即标准输出sys.stdout和sys.stderr接收到的输出信息
        t.insert('end', info)  # 在多行文本控件最后一行插入print信息
        t.update()  # 更新显示的文本，不加这句插入的信息无法显示
        t.see(tk.END)  # 始终显示最后一行，不加这句，当文本溢出控件最后一行时，不会自动显示最后一行

    def restoreStd(self):
        # 恢复标准输出
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak

# 创建一个爬虫调用函数
def crawl() :
# 用户输入的表达式，计算结果后转换为字符串
    oid = str(expression.get())
    if v.get() == 1:
        b站.crawlerB(oid)
    elif v.get() == 2:
        weibo.crawlerW(oid)
    elif v.get() == 3:
        kuaishou.crawlerK(oid)
    elif v.get() == 4:
        小红书.crawlerX(oid)

def select():
    dict = {1: 'BiliBili', 2: '微博', 3: '快手', 4: '小红书'}
    strings = '您爬取的网站是' + dict.get(v.get()) + '，祝您学习愉快'
    print(strings)
    label['text']=strings

def get_image(filename,width,height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

mystd = myStdout()  # 实例化重定向类

#创建主窗口
root_window = tk.Tk()
root_window.title("数据采集器")
root_window.geometry("800x600")
root_window['background'] = "#C9C9C9"

#设置背景图片
canvas_root = tk.Canvas(root_window,width=800,height=600)
im_root = get_image("bg.png",800,600)
canvas_root.create_image(400,300,image = im_root)
canvas_root.pack()

#设置程序的名称
text = tk.Label(root_window,text = "数据采集器",font=('仿宋',20,'bold italic')).place(x = 400,y=20,anchor=CENTER)

#配置单选按钮
# IntVar() 用于处理整数类型的变量# 根据单选按钮的 value 值来选择相应的选项
v = tk.IntVar()
v.set(0)
site = [('BiliBili',1),
        ('微博',2),
        ('快手',3),
        ('小红书',4)]
x = 100
for name,num in site:
    radio_button = tk.Radiobutton(root_window, text=name, fg='blue',font=('微软雅黑','16','bold'),variable=v, value=num,command=select).place(x = x,y=90,anchor=CENTER)
    x+=200

frame = Frame (root_window)
#创建一个Label控件
label = Label (frame,text = "准备好了吗,要开始了")
#创建一个Entry控件,读取用户输入的id号，将用户的输入表达式显示在Entry控件上
entry = Entry (frame,width=40)
expression = StringVar ()
entry ["textvariable"] = expression

#创建两个button按钮
button1 = Button (root_window, text="开 始",font = ('微软雅黑','19','bold'),command=crawl,width=10,height=3)
button2 = Button (root_window, text="结 束",font = ('微软雅黑','19','bold'),command=crawl,width=10,height=3)
#Button控件位于窗体的右方
button1.place(x = 600,y=120)
button2.place(x = 600,y = 240)

#设置Entry控件为焦点所在
entry.focus ()
frame.place(x = 400,y=140,anchor=CENTER)
#Entry控件位于窗体的上方
entry.pack()
#Label控件位于窗体的左方
label.pack (side="left")

#实例化多行文本
t = tk.Text(root_window)  # 创建多行文本控件
t.place(height= 170,x = 400,y = 520,anchor=CENTER)  # 布局在窗体上


root_window.resizable(False,False)
root_window.mainloop()
mystd.restoreStd()  # 恢复标准输出