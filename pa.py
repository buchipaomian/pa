import requests
import requests,random
from bs4 import BeautifulSoup
import os
import time

proxies = {'http':'http://118.174.220.231:40924','https':'https://118.174.220.231:40924'}
user_agents = ['Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50','Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11']
def getHtmlurl(url):         #获取网址
    headers = {'User-Agent':random.choice(user_agents)}
    resp = requests.get(url,headers = headers,proxies = proxies)
    resp.raise_for_status()
    resp.encoding=resp.apparent_encoding
    return resp.text
def getaddress(html,i):#get the html of details page
    soup =BeautifulSoup(html,'html.parser')
    div=soup.select('div#uxthumbs')
    for item in div:
        a = item.find_all('a')
        for im in a:
            # print(im)
            hrf = im['href']
            # print(hrf)
            tempurl = "http://www.animecharactersdatabase.com/"+hrf
            getpic(getHtmlurl(tempurl))
            i = i+1
            print('ok')
            print(i)
    return i

def getpic(html,i): #获取图片地址并下载
    print("get set")
    soup =BeautifulSoup(html,'html.parser')
    div=soup.select('div#uxthumbs')
    for item in div:
        a = item.find_all('a')
        for im in a:
            i = i+1
            print(i)
            img = im.find('img')
            try:
                urla = img['src']
                if(urla != None):
                    downloadimg(urla)
            except:
                print('ad') 
    return i
    #     all_img.pop(k.find_all('jpg'))
    # print("ok2")
    # for img in all_img:
    #     downloadimg(img)
# def save_img(self, url, name):  # 保存图片
#     img = self.request(url)
#     f = open(name, 'ab')
#     f.write(img.content)
#     print(name, '文件保存成功！')
#     f.close()
# def get_html(url):
#     headers = {'User-Agent':random.choice(user_agents)}
#     proxies = {'http':'http://36.67.96.7:37554','https':'https://182.111.64.8:21776'}
#     resp = requests.get(url,headers = headers,proxies = proxies)
#     return resp.text
def downloadimg(img):
    # time.sleep(random.random()*0.01) 
    img_url=img
    img_url = img_url.replace("/thumbs/200",'')
    root='C:/pic/'
    path = root + img_url.split('/')[-1]
    try:                              #创建或判断路径图片是否存在并下载
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            headers = {'User-Agent':random.choice(user_agents)}
            r = requests.get(img_url,headers = headers,proxies = proxies)
            status = r.status_code
            if(status == 404):
                print('ok')
                img_url = img_url.replace("jpg","png")
                r = requests.get(img_url,headers = headers,proxies = proxies)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")
def main():
    i =6900
    while(i<30000) :
        url='http://www.animecharactersdatabase.com/ux_search.php?x='+str(i)+'&mimikko=0&tag=&sc=&sp=&date=0&refs=0&role=0&lightdark=0&esbr=-1&clothing=0&otherchar=-1&mt=0&gender=1&hair_color=0&hair_color2=0&hair_color3=0&hair_length=0&hair_length2=0&hair_length3=0&eye_color=0&eye_color2=0&eye_color3=0&age2=0&age3=0&age=0'
        html=(getHtmlurl(url))
        print('*******************new page***************************')
        print(i)
        i = getpic(html,i)
main()