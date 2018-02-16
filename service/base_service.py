# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
import cv2
from settings import BASE_DIR
from matplotlib import pyplot as plt


def save_cv2_img(img, name, file="img"):
    path = BASE_DIR + '/%s/%s.jpg' % (file, name)
    cv2.imwrite(path, img)


def save_plt_img(img, file, filename):
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.imshow(img)
    print "保存", img.shape
    path = BASE_DIR + '/' +file
    plt.savefig(path+ '/' + '/%s.jpg' % filename)


def read_cv2_img(name, path="img"):
    p = BASE_DIR+ "/%s/%s.jpg" % (path, name)
    img = cv2.imread(p)
    return img


def show_3_img(img1, img2, img3, name1="b", name2="g", name3="r"):
    plt.subplot(131), plt.imshow(img1, cmap='gray')
    plt.title('b'), plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(img2, cmap='gray')
    plt.title('g'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(img3, cmap='gray')
    plt.title('r'), plt.xticks([]), plt.yticks([])
    plt.show()