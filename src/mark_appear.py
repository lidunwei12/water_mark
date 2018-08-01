# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import cv2
import numpy as np
from PIL import Image
import os


def mark_show(image_file):
    """
            子函数
            :param image_file:处理前的图片
            :return: 突出水印的图片及其类别（水印是有颜色的或者是无颜色的）
        """
    img = Image.open(image_file)
    im = img.load()
    w, h = img.size
    for i in range(w):
        for j in range(h):
            data = im[i, j]
            if isinstance(data, int):
                fleck = 0
                ans = data
                if ans > 245:
                    im[i, j] = 0
                elif ans < 190:
                    im[i, j] = 0
                else:
                    im[i, j] = 255
            else:
                fleck = 1
                ans = int(sum(im[i, j]) / 3)
                if ans > 245:
                    im[i, j] = 0
                elif ans < 205:
                    im[i, j] = data
                else:
                    im[i, j] = 255
    # img.show()
    # print(fleck)
    img = np.asarray(img)
    return img, fleck


def mark_find(image, fleck):
    """
        子函数
        :param image:处理后的图片
        :return: 发票代码和号码的位置
    """
    if fleck == 1:
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # rgb图像转换为hsv
        color_lower = np.array([0, 20, 46])  # 设定红色的阈值
        color_upper = np.array([180, 255, 255])
        image_mask = cv2.inRange(image_hsv, color_lower, color_upper)  # 对原图像和掩模进行位运算 只保留红色区域
        image = cv2.bitwise_and(image, image, mask=image_mask)
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_enhance = cv2.createCLAHE(clipLimit=2, tileGridSize=(10, 10))
    color_gray = image_enhance.apply(image)
    color_gray = cv2.medianBlur(color_gray, 5)
    (rew, color_bi_ary) = cv2.threshold(color_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    image_dilate = cv2.erode(color_bi_ary, None, iterations=22)  # 剩余的像素扩张并重新增长
    image_area, contours, hierarchy = cv2.findContours(image_dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 找出最大面积
    if len(contours) >= 1:
        image_outline = sorted(contours, key=cv2.contourArea, reverse=True)[1]  # 找到最大轮廓
        x, y, w, h = cv2.boundingRect(image_outline)
        color_bi_ary = color_bi_ary[y:y + h, x:x + w]
    return color_bi_ary


def appear_main(image_file, home):
    image, fleck = mark_show(image_file)
    image = mark_find(image, fleck)
    image = Image.fromarray(image)
    image.save(os.path.join(home, image_file[0:image_file.find('.jpg')]+'.png'))
    os.remove(image_file)
