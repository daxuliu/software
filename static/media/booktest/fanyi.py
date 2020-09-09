import requests
import random
import urllib.parse
import hashlib
import json
class trans:
    def __init__(self):
        self.re=''
        self.salt = random.randint(0, 100)
        self.s=str(self.salt)
    def tran(self,q):
        m2 = hashlib.md5()

        values = {}
        url = "http://api.fanyi.baidu.com/api/trans/vip/translate?"

        appid = '20181109000232134'  # 你的appid
        secretKey = 'O0_5hwu0Yj2bgZWflvgG'  # 你的密钥
        q = q
        to = 'zh'
        froms = 'kor'


        str = appid + q + self.s + secretKey
        m2.update(str.encode('utf-8'))
        sign = m2.hexdigest()
        values['appid'] = appid
        values['q'] = q
        print(q)
        values['to'] = to
        values['from'] = 'auto'
        values['salt'] = self.salt
        values['sign'] = sign
        data = urllib.parse.urlencode(values)

        url = url + data
        #print(url)
        text = requests.get(url)
        # json=json.dumps(text.json())
        #print(text)
        js = text.json()
        #print(js)
        try:
            result = js['trans_result'][0]['dst']
            self.re=result
        except:
            pass


if  __name__ == '__main__':
   
    salt = random.randint(0, 100)
    s=str(salt)
    m2 = hashlib.md5()

    values = {}
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate?"

    appid = '20181109000232134'  # 你的appid
    secretKey = 'O0_5hwu0Yj2bgZWflvgG'  # 你的密钥
    q = input()
    to = 'zh'
    froms = 'kor'


    str1 = appid + q + s + secretKey
    m2.update(str1.encode('utf-8'))
    sign = m2.hexdigest()
    values['appid'] = appid
    values['q'] = q
    print(q)
    values['to'] = to
    values['from'] = 'auto'
    values['salt'] = salt
    values['sign'] = sign
    data = urllib.parse.urlencode(values)
    print(data)
    url = url + data
    #print(url)
    text = requests.get(url)
    # json=json.dumps(text.json())
    #print(text)
    js = text.json()
    print(js)
    try:
        result = js['trans_result'][0]['dst']
        print(result)
            #self.re=result
    except:
            pass
    #trans=trans()
    #trans.tran('hello')
    #print(trans.re)
