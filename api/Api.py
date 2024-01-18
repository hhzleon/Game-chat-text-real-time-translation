import pyautogui
from PIL import Image
import pytesseract
import os
class hexinAPI:
    def __init__(self):
        pass

    def language_translate(self):
        # 可以把这个代码给优化一下
        # 两个截图给合并成一个截图 使用PIL

        im1 = pyautogui.screenshot(region=(46,700,600,400),imageFilename="img.png") #!TODO 截图区域，这里未来需要变成可设置的
        img = Image.open("./img.png")
        pixel_color = img.getpixel((15,350))
        # if (pixel_color == (0,195,255) or pixel_color == (255,252,67)): #!TODO 根据颜色判定是否弹出消息输入框
        text = pytesseract.image_to_string(img.crop((60,25,570,330)),lang="eng+chi_sim+kor")
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
    print (hexinAPI().language_translate())