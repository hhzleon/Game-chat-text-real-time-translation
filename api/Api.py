from PIL import ImageGrab
import pytesseract
import json
class hexinAPI:
    x = None
    y = None
    lastX = None
    lastY = None
    appid = None
    key = None
    def __init__(self):
        pass

    def language_translate(self):
        """
        quyu - 截图区域的坐标（x,y,结束x,结束y）

        """
        im1 = ImageGrab.grab((self.x,self.y,self.lastX,self.lastY))
        # im1.show()
        text = pytesseract.image_to_string(im1,lang="eng+kor+chi_sim")    # 今天把这个也给精简了
        print(text)
        messages_list = []
        for i in text.split("\n"): # 循环消息列表来判定识别的文字是否为玩家的语言
            if (len(i)==0):
                continue
            if (i[0]=="["):
                # 不是的话删除
                messages_list.append(i)
        
        return messages_list   # 返回玩家消息列表

    def jietuTest(self,quyu): # quyu必须要传入一个元组
        """
        截图测试功能
        """
        img = ImageGrab.grab(quyu)
        img.show()
    
    def saveSetting(self,x,y,lastX,lastY,appid,key):
        """
        保存配置
        x - 开始x
        y - 开始y
        lastX - 结束x
        lastY - 结束y
        appid - 百度的接口ID
        key - 百度的接口Key
        """
        with open("config.yml","w") as f:
            f.write(json.dumps({"x":int(x),"y":int(y),"lastX":int(lastX),"lastY":int(lastY),"appid":appid,"key":key}))
            f.close()
        return True

    def loadSetting(self):
        ff = open("config.yml","r")
        data = json.loads(ff.read())
        ff.close()
        self.x = data['x']
        self.y = data['y']
        self.lastX = data['lastX']
        self.lastY = data['lastY']
        self.appid = data['appid']
        self.key = data['key']
        # return data

if __name__=="__main__":
    # print (hexinAPI().jietuTest(quyu=(46,700,640,1100)))
    hexinAPI().loadSetting()