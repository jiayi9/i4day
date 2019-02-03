#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import re
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


# 3.下载图片并保存成文件名
def downloadimage(image, filename):
    urllib.request.urlretrieve(image, filename)


# 4.批量下载图片，保存当前目录下文件
# 自定义函数，用来批量保存图片
def batchdownloadimage(images, names, path='C:/i4day/demo/pics/'):
    count = 1
    newImages = list(images)
    newImages.pop()
    newImages.pop()
    newImages.pop()
    for (url, name) in zip(newImages, names):
       if os.path.exists("C:/i4day/demo/pics/%s.jpg" % (name.strip('"')).replace("&#183;", "-")):
            continue
       else:
           # OSError: [Errno 22] Invalid argument: 'D:/pics/starPics/:费尔鲁扎-鲍克.jpg'
           downloadimage(url, ''.join([path, '{}.jpg'.format(((name.strip('"')).replace("&#183;", "-"))).strip(":")]))
           print('正在下载 --> {} 的图片'.format((name.strip('"')).replace("&#183;", "-")), end='\n')
           count += \
               1

# 调用自定义函数
for num in range(1, 464):
    url = 'http://www.yoka.com/dna/star/item-------------%s.html' % num
    page = urllib.request.urlopen(url).read()
    page = page.decode('utf-8')

    rel = re.compile('<img src="(http://www.yoka.com/dna/pics/Star/*.*?\.jpg)".*?>')
    rel_Name = re.compile(".*alt=(.*) width.*")

    jpgs = re.findall(rel, page)
    names = re.findall(rel_Name, page)
    batchdownloadimage(jpgs, names)
