#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox
import time
import threading
import os
import urllib.request


def update_show_time(show_text):
    datetime = time.localtime()
    show_text.set("%s-%s-%s %s:%s:%s 星期%s" % (datetime[:6] + (weekday[datetime[6]], )))

    t = threading.Timer(1, update_show_time, (show_text, ))
    t.start()

def onBtnPowoerClick():
    # print("关机")
    os.system("shutdown -s -t 0")

def onBtnDownload():
    url = userName.get()
    data = urllib.request.urlopen(url).read()

    file_name = url.split("?")[0].split("/")[-1]
    with open(file_name, "wb") as f:
        f.write(data)

    tk.messagebox.showinfo("友情提示", "下载完毕！")

mainWnd = tk.Tk()  # 创建一个Tk类的实例（它代表程序的主窗口）

mainWnd.title("用户登录")
mainWnd.minsize(500, 500)

weekday = ("一", "二", "三", "四", "五", "六", "日")
show_text = tk.StringVar()
datetime = time.localtime()
show_text.set("%s-%s-%s %s:%s:%s 星期%s" % (datetime[:6] + (weekday[datetime[6]], )))
lblTime = tk.Label(mainWnd, textvariable=show_text)
lblTime.pack()

t = threading.Timer(1, update_show_time, (show_text, ))
t.start()

btnPower = tk.Button(mainWnd, text="关 机", command=onBtnPowoerClick)
btnPower.pack()

userName = tk.Entry(mainWnd)
userName.configure(width=60)
userName.pack(pady=10)

btnDownload = tk.Button(mainWnd, text="下 载", command=onBtnDownload)
btnDownload.pack()

mainWnd.mainloop()  # 事件循环
