# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
from src.word_to_pdf import doc2pdf
from src.pdf_to_jpg import convert_pdf_to_jpg
from src.mark_appear import appear_main
from src.mark_compare import hash_image_save
import os

WORD_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'word/'))
if not os.path.isdir(WORD_HOME):
    os.mkdir(WORD_HOME)
PDF_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pdf/'))
if not os.path.isdir(PDF_HOME):
    os.mkdir(PDF_HOME)


def crate_mark_database():
    for file in os.listdir(WORD_HOME):
        input = WORD_HOME + '/' + file
        output = PDF_HOME + '/' + file[0:file.find('.')] + '.pdf'
        rc = doc2pdf(input, output)
        if rc:
            print('转换成功')
        else:
            print('转换失败')
    for file in os.listdir(PDF_HOME):
        if file.find('.pdf') != -1:
            convert_pdf_to_jpg(PDF_HOME + '/' + file)
    for file in os.listdir(PDF_HOME):
        if file.find('.pdf') != -1:
            os.remove(PDF_HOME + '/' + file)
    for file in os.listdir(PDF_HOME):
        appear_main(PDF_HOME + '/' + file, PDF_HOME)
    hash_image_save(PDF_HOME)


