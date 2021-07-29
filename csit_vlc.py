import numpy as np
import cv2
import time

# 讀取視訊檔案
name = input()
cap = cv2.VideoCapture(name)
# 或者電影每秒的幀數
fps = cap.get(cv2.CAP_PROP_FPS)
# 判斷視訊是否一直開啟
print(fps)
flag = 0
number = 0
count1 = 0
count0 = 0
countnum = 0
counttwoframe = 0
while (cap.isOpened()):
    success,frame = cap.read()
    # 視訊顯示
    #cv2.imshow('law', frame)
    # 設定視窗
    #cv2.resizeWindow('law', 512,288)
    height, width, channels = frame.shape
    #print (frame[256,144,0]) #B Channel Value
    #print (frame[256,144,1]) #G Channel Value
    #print (frame[256,144,2]) #R Channel Value
    #print ('-----')
    if flag == 0:
        if frame[256,144,0] >= 128:
            count1 += 1
            if count1 == 3:
                flag = 1
                continue
        if frame[256,144,0] < 128:
            count1 = 0
    if flag == 1:
        if frame[256,144,0] < 128:
            count0 += 1
            if count0 == 3:
                flag = 2
                continue

    if flag == 2:
        if counttwoframe == 0 : 
            counttwoframe = 1
        elif counttwoframe == 1 :
            if frame[256,144,0] >= 128:
                number = number*2 + 1
                countnum += 1
            if frame[256,144,0] < 128:
                number = number*2 + 0
                countnum += 1
            counttwoframe = 0
    if countnum == 12:
        print(number)
        break
    
    # 判斷退出條件
    if cv2.waitKey(int(1000//fps)) ==ord('q'):
        break
# 清除快取退出
cv2.destroyAllWindows()