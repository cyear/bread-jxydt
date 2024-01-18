"""
@author: 冫氵丶面包
@file: main.py
@time: 2024.01.17
"""

import os
import xml.etree.ElementTree as ET

list_ = "ABCDEFG"


def xml_6():
    path = os.path.abspath(__file__).split('\\')[:-2]
    path.append("1.xml")
    path = '\\'.join(path)
    tree = ET.parse(path)
    root = tree.getroot()
    answer = []
    title = None
    answer_ = None
    x, y = None, None
    for i in root.iter("node"):
        # print(i.attrib)
        if i.get('resource-id') == "com.jxedt:id/tv_question_body":
            title = i.get("text").strip()
            answer_ = i.get("content-desc")
        if i.get("resource-id") == "com.jxedt:id/ll_question_img":
            img = i.get("bounds").split("][")
            xy, xy_ = img[0][1:].split(","), img[1][:-1].split(",")
            x, y = [(int(j), int(k)) for (j, k) in zip(xy, xy_)]
            # print(img)
        if i.get("resource-id") == "com.jxedt:id/tv_answer_title":
            answer.append(i.get("text").strip())
    # print(title)
    # print(answer_)
    answer = [f"{a}.{n}" for a, n in zip(list_, answer)]
    # print(answer)
    print(title, answer_, answer, x, y)
    if x and y:
        return [title, answer_, answer, (x[1] - x[0], y[1] - y[0], x[0], y[0])]
    return [title, answer_, answer]


def xml_66():
    path = os.path.abspath(__file__).split('\\')[:-2]
    path.append("1.xml")
    path = '\\'.join(path)
    tree = ET.parse(path)
    root = tree.getroot()
    answer = []
    for i in root.iter("node"):
        if i.get('resource-id') == "com.jxedt:id/tv_best_analysis":
            return i.get("text").strip()


def xml_666():
    path = os.path.abspath(__file__).split('\\')[:-2]
    path.append("1.xml")
    path = '\\'.join(path)
    tree = ET.parse(path)
    root = tree.getroot()
    answer = []
    for i in root.iter("node"):
        # print(i.attrib)
        if i.get("text") == "太棒啦，已答完最后一题\n快去考试，试试吧~":
            return 1
    return 0


if __name__ == '__main__':
    # xml_6()
    xml_6()
