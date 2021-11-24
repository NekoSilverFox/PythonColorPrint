# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 10:30
# @Author  : Meng Jianing
# @FileName: MainTest.py
# @Software: PyCharm
# @Versions: v0.1
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------
from Pycolor import *

Pycolor.color_print("输出字符串的 默认形式（未加任何参数）" + "后置字符串")
Pycolor.color_print("输出字符串的 颜色为青色", ForeColor.CYAN)
Pycolor.color_print("输出字符串的 背景色为红色", BackgroundColor.RED)
Pycolor.color_print("输出字符串的 颜色为黄色 背景色为青色", ForeColor.YELLOW, BackgroundColor.CYAN)
Pycolor.color_print("输出 加粗 字符串", ShowType.HIGHLIGHT)
Pycolor.color_print("输出字符串的 颜色为黄色 背景色为青色 且 为反显颜色", ForeColor.YELLOW, BackgroundColor.CYAN, ShowType.INVERT)

string = Pycolor.get_color_string("输出字符串的 颜色为黄色 背景色为青色 且 为加下划线", ForeColor.YELLOW, BackgroundColor.CYAN, ShowType.UNDERLINE)
print(string)
