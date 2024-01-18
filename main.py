from api.Api import hexinAPI
from api.Tran import baidu_translator_api
import webview
class Api:
    def tranPlayers_message(self):
        # 这里实现你的方法
        messages_list = hexinAPI().language_translate()
        # print(messages_list)
        o = 0
        for i in messages_list:
            message = i.split(": ")[-1] # 获取到的单条玩家信息
            messages_list[o] = i+" --> " + baidu_translator_api("auto","zh",message)
            o+=1
        return messages_list
    
    # def tranMessage(self,message):
    #     return baidu_translator_api("auto","")


if __name__ == '__main__':
    api = Api()
    webview.create_window("OW2翻译器", "templates\index.html", width=600, height=350,js_api=api)
    webview.start(debug=True)
    # api.tranPlayers_message()


