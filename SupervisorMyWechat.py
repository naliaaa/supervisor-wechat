#!/usr/bin/env python
# coding: utf-8

# In[45]:

import sys
import aircv as ac


def supervisorMyWeChat(name):

    import time
    import numpy
    from PIL import ImageGrab
    import pytesseract
    import pyautogui
    #import os
    #鼠标在左上会报错
    pyautogui.FAILSAFE =False
    #每一个操作停顿1秒
    pyautogui.PAUSE = 1

    #进入监控阶段
    while True:
        #抓取监控的聊天框
        img = ImageGrab.grab(bbox=(0, 0, 1000, 1000))
        #转化为灰度图
        img = img.convert('L')
        #img = numpy.array(img.getdata(),numpy.uint8).reshape(img.size[1],img.size[0],3)
        #img.save(r'D:\1.png')
        #对图像进行文字识别
        im_str = pytesseract.image_to_string(img, lang='chi_sim') 
        #print(im_str)
        #对空白字符进行过滤
        im_str = im_str.replace(' ','').replace('\n','')
        #print(im_str)
        
        #找到关键词则在右边的聊天框输入并发送30次‘1’
        if im_str.find(name)>= 0:
            ''' 连续发30个1
            for i in range(30):
                #pyautogui.moveTo(1611,1116,duration=1)    
                pyautogui.click(1611,1116)
                #pyautogui.mouseDown()   # 鼠标按下
                #pyautogui.mouseUp()    # 鼠标释放
                pyautogui.typewrite('1')
                pyautogui.click(2040,1236)
            '''
            #打skype电话
            '''
            pyautogui.moveTo(2545,127,duration=1)
            pyautogui.mouseDown()
            pyautogui.mouseUp()
            break
            '''
            #全屏截图
            img = ImageGrab.grab()
            img.save('tmp.jpg')

            #被查找的图片          
            imsrc = ac.imread('tmp.jpg')
            #要查找的图像
            imsch = ac.imread('phone.jpg')
            #查找到的中心坐标和匹配度
            xy = ac.find_template(imsrc,imsch)

            if xy['result']:
                print(xy['result'])
                pyautogui.moveTo(xy['result'][0],xy['result'][1],duration=1)
                pyautogui.mouseDown()
                pyautogui.mouseUp()
                break
            


        #找不到就等待10秒后重复开始识别
        else:      
            time.sleep(30)

    #print(pyautogui.position())
    print('\n找到了',flush=True)
    return


# In[ ]:


if __name__ == '__main__':
    supervisorMyWeChat(sys.argv[1])
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




