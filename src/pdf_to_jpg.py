# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
from wand.image import Image


def convert_pdf_to_jpg(filename):
    with Image(filename=filename) as img:
        print('pages = ', len(img.sequence))
        with img.convert('jpg') as converted:
            converted.save(filename=filename[0:filename.find('.pdf')] + 'page.jpg')

