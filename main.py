"""
@author: 冫氵丶面包
@file: main.py
@time: 2024.01.17
"""
import time

from model.Android_tool import Tool, log
from model.app_xml import xml_6, xml_66, xml_666
from model.w_xls import xw_toExcel
import os

sh = "/bin"

tool = Tool(sh=sh)
tool.root()
dict_ = list()
tool.xml()
i = 0
while 1:
    i += 1
    tool.xml()
    try:
        c = xml_6()
    except Exception as e:
        log(e, 4)
    title = c[0]
    answer_ = c[1]
    answer = c[2]
    if len(c) == 4:
        xy = c[3]
        tool.scrp(i, xy[0], xy[1], xy[2], xy[3])
        path = f"img/{i}.png"
    else:
        path = None
    # 需要下滑半屏
    tool.swipe("550 850 550 300 100")
    try:
        tool.xml()
    except Exception as e:
        log(e, 4)
    info = xml_66()
    print(info)
    tool.swipe("850 1600 300 1600 100")
    # time.sleep(0.1)
    if not title or not info:
        break
    dict_.append({"title": title, "answer_": answer_, "answer": str(answer), "info": info, "path": path})
    print("---"*10)

xw_toExcel(dict_, 'out.xlsx')
