# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
import win32com.client


def doc2pdf(input, output):
    try:
        # 打开文件
        o = win32com.client.Dispatch("kwps.Application")
        o.Visible = False
        doc = o.Documents.Open(input)
        doc.ExportAsFixedFormat(output, 17)
        return True
    except:
        return False
    finally:
        o.Quit()



