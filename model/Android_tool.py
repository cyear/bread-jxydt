"""
@author: 冫氵丶面包
@file: main.py
@time: 2024.01.17
"""

import os
import time


def log(string, v):  # 控制台输出
    os.system('')
    hms = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print([f"[Log]\033[1;38m{string}\033[0m",  # 白色
           f"\033[1;32m[{hms}]{string}\033[0m",  # 绿色
           f"\033[1;33m[{hms}]{string}\033[0m",  # 黄色
           f"\033[1;35m[{hms}]{string}\033[0m",  # 紫色
           f"\033[1;31m[Error-{hms}] {string}\033[0m"][v])  # 红色


class Tool:
    def __init__(self, sh):
        self.sh = sh
        log(f"sh -> {sh}", 2)
        self.path = os.path.abspath(__file__).split('\\')[:-2]

    def root(self):
        c = self.path.copy()
        c.append("platform-tools\\adb.exe")
        c = "\\".join(c)
        self.root_path = c
        log("Use adb！", 0)

    def swipe(self, xy):
        """
        550 1700 550 300 500
        :param xy:
        :return:
        """
        os.system(self.root_path + f" shell input swipe " + xy)
        # log("swipe ok!", 1)

    def scrp(self, file, x, y, x_, y_):
        os.system(self.root_path + f" shell {self.sh}/screencap -p /storage/emulated/0/1.png >nul 2>nul")
        c = self.path.copy()
        c = "\\".join(c)
        os.system(self.root_path + f" pull /storage/emulated/0/1.png " + c + " >nul 2>nul")
        os.system(f"magick 1.png -crop {x}x{y}+{x_}+{y_} -quality 100 img/{file}.png")
        # log(f"Screenshot save location: img/{file}.png", 1)

    def xml(self):
        """
        获取 控件
        :return: xml（str）
        """
        os.system(self.root_path + f" shell {self.sh}/uiautomator dump /storage/emulated/0/1.xml >nul 2>nul")
        # log(f"XML save /storage/emulated/0/1.xml", 1)
        c = self.path.copy()
        c = "\\".join(c)
        os.system(self.root_path + f" pull /storage/emulated/0/1.xml " + c + " >nul 2>nul")