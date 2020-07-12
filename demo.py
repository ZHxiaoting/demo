# _*_ coding:utf-8 _*_
"""
author: Zhuxiaoting
date: 2020/7/12
"""

# r 表示原生的
print(2+2)
print('c:\\some\\name')
print(r'c:\some\name')

# 字符串中 format 用法
x='abc'
print(f'c:\\some\\name\\{x}')
print('c:\\some\\name\\{}'.format(x))
print('c:\\some\\name\\{}\\{}'.format(x, 123))
print('c:\\some\\name\\{x}\\{y}'.format(x=x, y=123))