# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
from src.word_to_pdf import doc2pdf
from src.pdf_to_jpg import convert_pdf_to_jpg
from src.mark_appear import appear_main
from src.mark_compare import han_main
import os

TEMP_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'temp'))
if not os.path.isdir(TEMP_HOME):
    os.mkdir(TEMP_HOME)


def main(file):
    name = file[0:file.find('.')]
    if file.find('.pdf') == -1:
        rc = doc2pdf(TEMP_HOME + '/' + file, TEMP_HOME + '/' + name + '.pdf')
        os.remove(TEMP_HOME + '/' + file)
    convert_pdf_to_jpg(TEMP_HOME + '/' + name + '.pdf')
    os.remove(TEMP_HOME + '/' + name + '.pdf')
    for file in os.listdir(TEMP_HOME):
        appear_main(TEMP_HOME + '/' + file, TEMP_HOME)
    result = 0
    for file in os.listdir(TEMP_HOME):
        ans = han_main(TEMP_HOME + '/' + file)
        if ans == "copy":
            result = result + 1
    if result != 0:
        return "copy"
    else:
        return "no copy"



