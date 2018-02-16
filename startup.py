# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'

from service.align_image_code import align_images
from service.base_service import *
import cv2


def start():
    im1 = plt.imread(BASE_DIR + '/img/man.jpg')
    im2 = plt.imread(BASE_DIR + '/img/cat.jpg')
    # resize two images
    re2, re1 = align_images(im2, im1)
    new_man = cv2.cvtColor(re2, cv2.COLOR_RGB2BGR)
    cv2.imshow("man", new_man)
    cv2.waitKey()


if __name__ == '__main__':
    start()
