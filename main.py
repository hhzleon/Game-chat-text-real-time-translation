from api.Api import hexinAPI
from api.Tran import baidu_translator_api
import pyperclip as pc
import webview
class Api:
    def tranPlayers_message(self):
        # 这里实现你的方法
        messages_list = hexinAPI().language_translate(quyu=(110,700,640,1030)) # 传入截屏区域
        o = 0
        for i in messages_list:
            message = i.split(": ")[-1] # 获取到的单条玩家信息
            messages_list[o] = i+" --> " + baidu_translator_api("auto","zh",message)
            o+=1
        return messages_list
    
    def tranMessage(self,message):
        kor_message = baidu_translator_api("auto","kor",message)
        pc.copy(kor_message)
        return kor_message

def onshow(window):
    # 检测到窗口被切换了就直接翻译
    window.evaluate_js("submit()")




if __name__ == '__main__':
    api = Api()
    window = webview.create_window("OW2翻译器", "templates\index.html", width=600, height=277,js_api=api,frameless=True)
    webview.start(debug=False)
    window.events.shown += onshow(window=window)
    # api.tranPlayers_message()


