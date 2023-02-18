import sys
import tkinter


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
        t.see(tkinter.END)  # 始终显示最后一行，不加这句，当文本溢出控件最后一行时，不会自动显示最后一行

    def restoreStd(self):
        # 恢复标准输出
        sys.stdout = self.stdoutbak
        sys.stderr = self.stderrbak


def btn_func():
    """按键的触发事件"""
    #demo0929.func()

mystd = myStdout()  # 实例化重定向类
window = tkinter.Tk()  # 实例化tk对象
t = tkinter.Text(window)  # 创建多行文本控件
t.pack()  # 布局在窗体上

b = tkinter.Button(window, text='start', command=btn_func)  # 创建按钮控件，并绑定触发事件
b.pack()  # 布局在窗体上

window.mainloop()  # 显示窗体
mystd.restoreStd()  # 恢复标准输出

