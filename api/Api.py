import pyautogui
from PIL import Image,ImageGrab
import pytesseract
import os
class hexinAPI:
    def __init__(self):
        pass

    def language_translate(self,quyu):
        """
        quyu - 截图区域的坐标（x,y,结束x,结束y）

        """
        im1 = ImageGrab.grab(quyu)
        text = pytesseract.image_to_string(im1,lang="eng+kor+chi_sim")    # 今天把这个也给精简了
        os.system("cls")
        messages_list = []
        for i in text.split("\n"): # 循环消息列表来判定识别的文字是否为玩家的语言
            if (len(i)==0):
                continue
            if (i[0]=="["):
                # 不是的话删除
                messages_list.append(i)
        
        return messages_list   # 返回玩家消息列表

if __name__=="__main__":
    print (hexinAPI().language_translate(quyu=(46,700,640,1100)))