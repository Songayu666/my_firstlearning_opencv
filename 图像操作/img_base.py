import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('TkAgg')  # 设置后端为 Agg

img=cv2.imread('cat.jpg')  #彩色图
# img=cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)     #灰度图

#显示图片大小
# img_shape=img.shape
# print(img_shape)

def cv2_show(name, img):  # 显示图片的函数
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyWindow()

# cv2_show('image',img)   # 显示图片
#
# cv2.imwrite('mt_cat.png',img)   #保存

# #截取图像
# img=cv2.imread("cat.jpg")
# cat=img[:300,:300]
# cv2_show('cat',cat)

# #颜色通道提取
# b,g,r=cv2.split(img)  #有一个问题就是提取完之后只有一个维度，就会被认为是灰度图
# cv2_show('image',b)
# cv2_show('image1',g)
# cv2_show('image2',r)
# #颜色通道合成
# img=cv2.merge((b,g,r))
# cv2_show('image3',img)
# #显示多个图片要把以下两行单拧出来
# cv2.waitKey(0)
# cv2.destroyWindow()

# # 只保留R  bgr:r是第三层，把前两层变0就行
# cur_img = img.copy()
# cur_img[:,:,0] = 0
# cur_img[:,:,1] = 0
# print(cur_img.shape)
# cv2_show('R',cur_img)

# 边缘填充
top_size,bottom_size,left_size,right_size = (50,50,50,50)

replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_CONSTANT, value=666)
# BORDER_REPLICATE：复制法，也就是复制最边缘像素。
# BORDER_REFLECT：反射法，对感兴趣的图像中的像素在两边进行复制例如：fedcba|abcdefgh|hgfedcb
# BORDER_REFLECT_101：反射法，也就是以最边缘像素为轴，对称，gfedcb|abcdefgh|gfedcba
# BORDER_WRAP：外包装法cdefgh|abcdefgh|abcdefg
# BORDER_CONSTANT：常量法，常数值填充。
# plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
# plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
# plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
# plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
# plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
# plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
# plt.show()

# #数值计算
# img_cat=cv2.imread('cat.jpg')
# img_dog=cv2.imread('dog.jpg')
# img_cat2= img_cat -10
# # cv2_show('img_cat',img_cat2)
# img_cat2_add=img_cat+img_cat2 #相当于% 256
# # img_cat2_add=cv2.add(img_cat,img_cat2) #max（255，add）
# cv2_show('img_cat_add',img_cat2_add)

#图像融合
img_cat=cv2.imread('cat.jpg')
img_dog=cv2.imread('dog.jpg')
img_dog = cv2.resize(img_dog, (500, 414))
# img_mix=img_cat + img_dog
# cv2_show('img_mix',img_mix) #只是矩阵相加
res = cv2.addWeighted(img_cat, 0.4, img_dog, 0.6, 0)   #0是偏执像
cv2_show('img_mix',res)   #可以融合图像，而不只是简单的矩阵相加
res = cv2.resize(img, (0, 0), fx=4, fy=4)  #倍数关系
plt.imshow(res)