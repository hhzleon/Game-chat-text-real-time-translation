from api.Api import hexinAPI
from api.Tran import baidu_translator_api
import pyperclip as pc
import webview

class Api:
    def __init__(self):
        self.hexin_api = hexinAPI()
        self.hexin_api.loadSetting()

    def tranPlayers_message(self):
        # 这里实现你的方法
        appid = self.hexin_api.appid
        key = self.hexin_api.key
        messages_list = self.hexin_api.language_translate() # 传入截屏区域
        o = 0
        for i in messages_list:
            message = i.split(": ")[-1] # 获取到的单条玩家信息
            messages_list[o] = i+" --> " + baidu_translator_api("auto","zh",message,appid,key)
            o+=1
        return messages_list
    
    def tranMessage(self,message):
        appid = self.hexin_api.appid
        key = self.hexin_api.key
        kor_message = baidu_translator_api("auto","kor",message,appid,key)
        pc.copy(kor_message)
        return kor_message
    
    def setting(self):
        setting = Setting() # 设置页面的API
        webview.create_window("设置页面","templates\setting.html",width=500,height=380,js_api=setting,resizable=False)
    
class Setting:
    def __init__(self):
        self.hexin_api = hexinAPI() 
        self.hexin_api.loadSetting() # 读取配置文件 
    def test(self,x,y,lastX,lastY):
        """
        测试截图的函数，输入4个值
        x - 开始x
        y - 开始y
        lastX - 结束x
        lastY - 结束y
        """
        self.hexin_api.jietuTest(quyu=(int(x),int(y),int(lastX),int(lastY)))
    def save(self,x,y,lastX,lastY,appid,key):
        """
        保存配置
        x - 开始x
        y - 开始y
        lastX - 结束x
        lastY - 结束y
        appid - 百度的接口ID
        key - 百度的接口Key
        """
        return self.hexin_api.saveSetting(x,y,lastX,lastY,appid,key)
        
    def getSetting(self):
        return {
            "x":self.hexin_api.x,
            "y":self.hexin_api.y,
            "lastX":self.hexin_api.lastX,
            "lastY":self.hexin_api.lastY,
            "appid":self.hexin_api.appid,
            "key":self.hexin_api.key
        }
        
a = False # 是否隐藏


if __name__ == '__main__':
    api = Api() # 主页的API
    window = webview.create_window("OW2翻译器", "templates\index.html", width=600, height=282,js_api=api,frameless=True,resizable=False)
    webview.start(debug=False)


