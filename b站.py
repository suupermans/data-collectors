# -*- coding = utf-8 -*-
# @Time:2022/8/21 9:11
# Author:李小宝
# @File:b站.py
# @Software:PyCharm

import os
import re
import requests
import pandas as pd
import json
import time
# from .main import crawler

def crawler(page,oid):
    def json_load(_json):
        try:
            return json.loads(re.match(".*?({.*}).*",r.text,re.S).group(1))
        except:
            raise ValueError("invalid Input")

    url = "https://api.bilibili.com/x/v2/reply/main?callback=jQuery17203267765874610167_1661044064860&jsonp=jsonp&next={}&type=1&oid={}&mode=3&plat=1&_=1661044481599".format(page,oid)
    headers = {
            "referer": "https://www.bilibili.com/bangumi/play/ss24049?spm_id_from=333.337.0.0",
            "user-agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/104.0.0.0Safari/537.36",
            "cookie": "buvid3=0DC3AE86-B5F5-1EBB-4D34-54E7FABB8E4150566infoc;i-wanna-go-back=-1;_uuid=F487DE13-131C-3E104-71D6-5238107DBC97F51111infoc;buvid4=B9986AC5-791B-9433-A77F-0287BB180D3E56168- 022021813-6FTBgjXvldgy1K9EYdC7Tw % 3D % 3D;rpdid = | (k | k)u) | mlm0J'uYRluYk)l); buvid_fp_plain=undefined; CURRENT_BLACKGAP=0; blackside_state=1; AMCV_98CF678254E93B1B0A4C98A5%40AdobeOrg=1176715910%7CMCMID%7C07446268011832996772434268923758195031%7CMCAAMLH-1656938177%7C11%7CMCAAMB-1656938177%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1656340577s%7CNONE%7CvVersion%7C5.4.0; nostalgia_conf=-1; LIVE_BUVID=AUTO5216587103243819; is-2022-channel=1; hit-dyn-v2=1; CURRENT_QUALITY=0; fingerprint=aa91a8a810eafbff367c3d5bbd8f282f; SESSDATA=8cf916ed%2C1676291744%2Cb2927%2A81; bili_jct=720e789e981e23b3da959400f6fb245b; DedeUserID=669273416; DedeUserID__ckMd5=1a1c9f1ff88a08bf; buvid_fp=9e855698858a6222ac092a6ae37534f7; b_ut=5; bsource=search_bing; sid=57ex0ucl; PVID=2; innersign=1; CURRENT_FNVAL=4048; b_lsid=103E426E5_182BDC413F6; bp_video_offset_669273416=696645941711601700; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_0DC3AE86%22%3A%22182BB1E35B3%22%2C%22333.788.fp.risk_0DC3AE86%22%3A%22182BB96916D%22%2C%22333.337.fp.risk_0DC3AE86%22%3A%22182BDC74F32%22%2C%22333.999.fp.risk_0DC3AE86%22%3A%22182AEC41D3C%22%2C%22333.937.fp.risk_0DC3AE86%22%3A%22182BDC700A1%22%2C%22333.1193.fp.risk_0DC3AE86%22%3A%22182BDC7500B%22%2C%22666.25.fp.risk_0DC3AE86%22%3A%22182BDCBEC84%22%2C%22333.905.fp.risk_0DC3AE86%22%3A%22182BDE258CD%22%7D%7D"
        }
    r = requests.get(url =url ,headers=headers)
    ta = json_load(r.text)
    # print(ta)
    dic = ta['data']['replies']
    content = []
    utime = []
    cname = []
    if dic is not None:
        for i in dic:
            message = i['content']['message']
            print(message)
            content.append(message)
            ctime = i['ctime']
            timeArray = time.localtime(ctime)
            true_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            print(true_time)
            utime.append(true_time)
            name = i['member']['uname']
            print(name)
            cname.append(name)
    datas = {
        "uname":cname,
        "content":content,
        "ctime":utime
             }
    csv =pd.DataFrame(datas)
    if page==1:
        csv.to_csv(oid+".csv",sep=',',index=False,header=True,encoding='utf-8-sig',mode='a')
    else:
        csv.to_csv(oid+".csv", sep=',', index=False, header=False, encoding='utf-8-sig', mode='a')
    return page,oid

def existdir():
    isExists = os.path.exists('B站')
    time.sleep(3)
    if not isExists:
        os.mkdir('B站')
    else:
        pass
    os.chdir('B站')

def crawlerB(oid):
    existdir()
    for page in range(0,100):
        crawler(page, oid)
    os.chdir('../')
    print("爬取完成！！！")

if __name__ =="__main__":
     oid = str(input("请输入视频的oid号:"))
     for page in range(0,100):
         crawler(page,oid)
     print("爬取完成！！！")

