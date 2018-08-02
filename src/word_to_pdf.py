# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
import win32com.client


def doc2pdf(input, output):
    with open('../config.txt') as f:
        if f.read() != 'wps'and f.read() != 'word':
            return "没有安装word解析api"
        else:
            if f.read() == 'wps':
                api_content = "kwps.Application"
            else:
                api_content = "word.Application"
            try:
                # 打开文件
                o = win32com.client.Dispatch(api_content)
                o.Visible = False
                doc = o.Documents.Open(input)
                doc.ExportAsFixedFormat(output, 17)
                return True
            except:
                return False
            finally:
                o.Quit()
