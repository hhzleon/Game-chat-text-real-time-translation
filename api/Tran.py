import random
import requests
import hashlib

def baidu_translator_api(from_lang,to_lang,text):
    url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    salt = random.randint(1,100)
    data = {
        "q":text,
        "from":from_lang,
        "to":to_lang,
        "appid":"appid补充", # 需要补充
        "salt":salt,
        "sign":hashlib.md5(("appid补充"+text+str(salt)+"密钥补充").encode()).hexdigest()
    }
    web = requests.post(url=url,headers=header,data=data)
    data = web.json()
    if ("trans_result" in data):
        return data['trans_result'][0]["dst"]
    else:
        return "Error"