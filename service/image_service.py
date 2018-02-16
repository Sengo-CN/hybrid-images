# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
import cv2


def low_pass_filter(img, sigma):
    """
    In this approach, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used.
    It is done with the function, cv2.GaussianBlur(). We should specify the width and height of the kernel which
    should be positive and odd. We also should specify the standard deviation in the X and Y directions,
    sigmaX and sigmaY respectively. If only sigmaX is specified, sigmaY is taken as equal to sigmaX.
    If both are given as zeros, they are calculated from the kernel size. Gaussian filtering is highly effective
    in removing Gaussian noise from the image.
    """
    return cv2.GaussianBlur(img, (sigma, sigma), 0)


def high_pass_filter(img, sigma):
    _img = img.copy()
    low_pass = low_pass_filter(img, sigma)
    return _img - low_pass


def hybrid_img(hig, low):
    return hig + low


def save_photo(img, name):
    path = BASE_DIR + '/%s.jpg' % name
    cv2.imwrite(path, img)


if __name__ == '__main__':
    from settings import BASE_DIR
    from align_image_code import align_images
    import matplotlib.pyplot as plt
    from base_service import *
    #
    im1 = plt.imread(BASE_DIR + '/img/man.jpg')
    print im1.shape
    #
    im2 = plt.imread(BASE_DIR + '/img/cat.jpg')

    re2, re1 = align_images(im2, im1)
    print re1.shape
    save_plt_img(re1, "img", "align1")
    save_plt_img(re2, "img", "align2")
    plt.close()

    a1 = read_cv2_img("align1")
    a2 = read_cv2_img("align2")
    print a1.shape
    hig = high_pass_filter(a2, 15)
    low = low_pass_filter(a1, 15)
    re = hybrid_img(hig, low)
    save_photo(re, "result")
    cv2.imshow("result", re)
    # save_plt_img(re, "img", "result")
    cv2.waitKey(0)