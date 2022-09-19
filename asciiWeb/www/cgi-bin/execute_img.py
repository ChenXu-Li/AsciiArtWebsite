#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

def exe_img(img_path="D:\\justplay\\asciiweb\www\\tmp\\test.jpg",show_heigth = 1,show_width = 1):
    


    #ascii_char = list("@#0QCt/i!;:,'.  ")
    ascii_char = list(" .;!1X0%#@")
    char_len = len(ascii_char)
    pic = plt.imread(img_path)
    #使用plt.imread方法来读取图像，对于彩图，返回size = heigth*width*3的图像
    #matplotlib 中色彩排列是R G B
    #opencv的cv2中色彩排列是B G R

    pic_heigth,pic_width,_ = pic.shape#只能处理三通道
    #pic_heigth,pic_width = pic.shape
    #print("pic.shape",pic.shape)
    #print("img argument",pic_heigth,pic_width)
    #pic_width,pic_heigth,_ = pic.shape
    #获取图像的高、宽

    if(1==show_heigth ==show_width):#就行一个自适应的分辨率调整
        show_heigth = 100
        show_width = int(show_heigth*pic_width/pic_heigth)
    #print("adjust argument",show_heigth ,show_width)


    gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]
    #RGB转灰度图的公式 gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

    #思路就是根据灰度值，映射到相应的ascii_char
    text_img=""
    for i in range(show_heigth):
        #根据比例映射到对应的像素
        y = int(i * pic_heigth / show_heigth)
        text = ""
        for j in range(show_width):
            x = int(j * pic_width / show_width)
            text += ascii_char[int(gray[y][x] / 256 * char_len)]

        # print(text)
        text+="\n"
        text_img+=text
    return text_img

if __name__ == '__main__':
    #print(exe_img("D:\\justplay\\asciiweb\www\\tmp\\test4.jpg",50,50))
    print(exe_img("D:\\justplay\\asciiweb\www\\tmp\\test3.jpg",1,1))
