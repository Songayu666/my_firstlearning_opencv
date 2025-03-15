import cv2
import matplotlib.pyplot as plt
import numpy as np

# img=cv2.imread('cat.jpg')  彩色图
img=cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)     #灰度图

img_shape=img.shape
print(img_shape)

def cv2_show(name, img):  # 显示图片的函数
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyWindow()

# cv2_show('image',img)   # 显示图片
#
# cv2.imwrite('mt_cat.png',img)   #保存

#截取图像
img=cv2.imread("cat.jpg")
cat=img[:300,:300]
cv2_show('cat',cat)