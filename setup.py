# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 12:30
# @Author  : Meng Jianing
# @FileName: setup.py
# @Software: PyCharm
# @Versions: v0.1
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------

from setuptools import setup
from setuptools import find_packages


VERSION = '0.1'

setup(
    name='Pycolor',
    version=VERSION,
    description='得到或输出带有色彩的字符串',
    packages=find_packages(),
    zip_safe=False
)
