# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:21:28 2017
@author: bob.Lee
"""
from PIL import Image
import os
import re

# DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), 'temp'))
# if not os.path.isdir(DATA_HOME):
#     os.mkdir(DATA_HOME)


def dhash(image, hash_size=8):
    image = image.convert('L').resize((hash_size + 1, hash_size), Image.ANTIALIAS, )
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2 ** (index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)


def hash_write(content):
    with open("hash.txt", "a", encoding='utf-8') as f:
        f.write(content)
        f.write('\n')
    return True


def hash_image_save(DATA_HOME):
    for file_jpg in os.listdir(DATA_HOME):
        try:
            orig = Image.open(DATA_HOME + '/' + file_jpg)
            content = file_jpg + '  ' + str(dhash(orig))
            hash_write(content)
        except Exception as e:
            print(e)
    return True


# hash_image_save()
def hammingDist(s1, s2):
    assert len(s1) == len(s2)
    ans = sum([ch1 != ch2 for ch1, ch2 in zip(s1, s2)])
    if ans > 5:
        return "no copy"
    else:
        return "copy"


def han_main(file):
    orig = Image.open(file)
    s1 = str(dhash(orig))
    content = 0
    for line in open('hash.txt'):
        line = line[line.find(' ') + 2:]
        ans = hammingDist(s1, line.strip())
        if ans == "copy":
            content = content + 1
    if content != 0:
        return "copy"
    else:
        return "no copy"


