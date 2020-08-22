# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from urllib import request
from urllib import error

def reqRest(timeStrs,cont):
    try:
        create_url='http://localhost:8080/springmvcpc/rest/test'#the create request url
        create_headers={'Content-Type':'text/plain; charset=utf-8'} #the request headers
        body_data_str={"timeStr":timeStrs,'content':cont}
        body_data = bytes(str(body_data_str), 'utf8')
        req = request.Request(create_url, headers=create_headers, data=body_data, method='POST')
        resp = request.urlopen(req)
        result = resp.read().decode()
        print(result)
        # result_json = json.loads(result)
    except error.HTTPError as err:
         error_body = err.file.read().decode()

def getDataFromNet():
    target = 'http://jn.bendibao.com/live/yiliaojiankang/'
    try:
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        texts = bf.find_all('li', class_='J-has-share listNews-item-s1 clearfix')
        # print(texts[0])
        num = 1
        for text in texts:
            bf0 = BeautifulSoup(str(text), 'html.parser')
            title_text = text.get_text()
            param1 = title_text.find('九价')
            param2 = title_text.find('HPV')
            param3 = title_text.find('宫颈癌')
            if param1 > 0 or param2 > 0 or param3 > 0:
                time_tag = bf0.find('p',class_='from')
                time_txt = time_tag.get_text()
                # print(type(bf0.li.div.h3.string))
                # print(type(bf0.li.div.h3.a.string))
                # print(bf0.li.div.h3.a.get_text())
                # print(bf0.li.div.get_text())
                next_href = bf0.li.div.h3.a.get('href')
                # print(next_href)
                req1 = requests.get(url=next_href)
                html1 = req1.text
                bf1 = BeautifulSoup(html1, 'html.parser')
                next_html_text = bf1.find('div', class_='content')
                next_text = next_html_text.get_text()
                reqRest(time_txt,next_text)
                num += 1
                if num == 4:
                    break
    except BaseException as e:
        print(e)
    finally:
        print("本次执行结束")

# getDataFromNet()

sched = BlockingScheduler()
# 表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
sched.add_job(getDataFromNet, 'cron', minute='*/5')
sched.start()