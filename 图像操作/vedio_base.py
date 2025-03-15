import cv2 #opencv读取的格式是BGR
import matplotlib.pyplot as plt
import numpy as np

vc = cv2.VideoCapture('test.mp4')
# 检查是否打开正确
# if vc.isOpened():
#     open, frame = vc.read()
#     print(open,frame)
# else:
#     open = False

while open:
    ret,frame=vc.read()
    if frame is None:
        break
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(10)&0xFF==27:
            break
vc.release()  #程序不会再占用摄像头（释放摄像头资源），cv2.VideoCapture()之后用
cv2.destroyWindow()    #销毁一个由 cv2.imshow() 创建的窗口