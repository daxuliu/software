#重写了result 增加了对做个错误的处理方式
#增加了 使用更加严格的语法模式

import  requests
import  json
from bs4 import BeautifulSoup
from  . youdao import  trans
class Result:
    def __init__(self):
        self.sen=""
        self.help=[]
        self.start=[]
        self.end=[]
        self.orgstr=[]
        self.rightwrite=[]
        self.isright=""
        self.zhhelp=[]

t=trans()
def Judge(text,tra):
    try:
        t = text
        url = 'http://speller.cs.pusan.ac.kr/results'
        data = {"text1": t,"btnModeChange":"on"}
        result = requests.post(url, data).text

        soup = BeautifulSoup(result, "html5lib")
        js = soup.find_all("script")
        # print(js[2].string)
        # 예 받습니다
        s = js[2].string

        s = s.split("\n")
        #print(s[2].replace("\t", "")[7:-1])
        s1 = s[2].replace("\t", "")[7:-1]
        jsre = json.loads(s1)
        print(jsre[0])
        result = Result()
        result.sen = jsre[0]["str"]
        #result.help = jsre[0]["errInfo"][0]["help"]
        for i in jsre[0]["errInfo"]:
            result.help.append(i["help"])
            print(i)
            result.start.append(i["start"])
            result.end.append(i["end"])
            result.orgstr.append(i["orgStr"])
            result.rightwrite.append(i["candWord"])
            tra.tran(i["help"])
            result.zhhelp.append(tra.re)
        #result.start = jsre[0]["errInfo"][0]["start"]

        #result.end = jsre[0]["errInfo"][0]["end"]
        #result.orgstr = jsre[0]["errInfo"][0]["orgStr"]
        #result.rightwrite = jsre[0]["errInfo"][0]["candWord"]
        result.isright="notright"
        #tra.tran(result.help)
        #result.zhhelp=tra.re

        return  result
    except:
        result = Result()
        result.isright="right"
        return result
def Passage(text,t):
    sen=text.split(".")

    results=[]
    for i in sen:
        results.append(Judge(i,t))
    return results

if __name__ == '__main__':
    text=""
    result = Result()

    re=Judge(text,t)

    print()
    print(re.rightwrite)
