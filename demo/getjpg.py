#!/bin/env python
#coding:utf8

__author__ = 'LEo'
import re
import urllib

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html



def getjpg(html):
    reg = r'src="(http://imgsrc.+?.jpg)" pic_ext='
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg,html)
    return imglist

html = gethtml("http://tieba.baidu.com/p/3038729868")
imglist = getjpg(html)
x = 0
for imgurl in imglist:
    urllib.urlretrieve(imgurl,'LEo%s.jpg'%x )
    x+=1





