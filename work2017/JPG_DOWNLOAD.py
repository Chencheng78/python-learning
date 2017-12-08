#-*- coding:utf-8 -*-
import re
import requests
from time import sleep


def dowmloadPic(html,keyword):

    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 0
    print '找到关键词:'+keyword+'的图片，现在开始下载图片...page:'+str(j)
    print pic_url
    for each in pic_url:
        print '正在下载第'+str(i+1)+'张图片，图片地址:'+str(each)
        try:
            pic = requests.get(each, timeout=10)
        except:
            print '【错误】当前图片无法下载'
            continue
        string = 'pictures\\'+keyword+'_'+str(i) + '_' + str(j) + '.jpg'
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        sleep(0.1)
        i += 1


if __name__ == '__main__':
    word = raw_input("Input key word: ")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    print url
    result = requests.get(url)

    for j in range(0, 200):
        dowmloadPic(result.text, word)
        next_page = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn=' + str(
            (j + 1) * 60) + '&gsm=0&ct=&ic=0&lm=-1&width=0&height=0'
        j += 1
        result = requests.post(next_page)

    #print result.content
