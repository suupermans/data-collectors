import requests
import csv #方便存储数据
import time  #防止被微博识别爬虫，让速度慢些
import json
import os

headers = {
    "cookie": "WEIBOCN_FROM=1110006030; __bid_n=185a50c042fd8547904207; FPTOKEN=F4rJG97CzHJQPbKVLkubuFegQWs4Mzu6wP7MW4et/lC9gr3OfWX29sXWbxaDpK/GYLxdqnZWV9nbyd/VhlAD/n4yeznYUhi0HodghRxfWJKYB+nsZE+jW4ddummj9fWkhpXHBVPH1y5JR/BMqH/AsHbQ5TTiYCUJ6+TrTBp3SLdv2re18NKpc8xgcpyHJsRSxtFBj/zjrMRZgRq+BbwEvxW99hNQOeAP8UXMKsyEWHyGgJZNcRY4Eyi/m8qd0K6vGpUrbyyUKJIPJ0JvCzAVxocYEpl6YK2sOhrUCHmWOzWtQJH3U8KBFJcmO60tg5K7WegsmzqOAFX4jEMUUMKlI9nzbk3a4kqv1+dywZ9TPzjgUHix94eo6itLcPG2X3mOHU2aibHypbe5XLLqJ6qWkw==|Fxd1VhK1uLZNBpf4Cg3ua3JAJzmqCwkQrOb2LM/fWm8=|10|be0ef873a2c0aa276dae05239ff82eec; SUB=_2A25Ou7HqDeRhGeFL71UU9CrNwzuIHXVqR9-irDV6PUJbkdAKLVfEkW1NQhKzMR9v0Rsv_vicrGc2P3JGELqzGjuq; MLOGIN=1; _T_WM=87010392536; M_WEIBOCN_PARAMS=oid%3D4839399348766717%26luicode%3D20000061%26lfid%3D4839399348766717; WEIBOCN_WM=3349; XSRF-TOKEN=fcae7f",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

def crawler(id):
    url = "https://m.weibo.cn/comments/hotflow?id="+str(id)+"&mid="+str(id)+"&max_id_type=0"
    f = open(id+".csv",mode ='w',newline='',encoding='utf-8-sig')
    csv_writer = csv.DictWriter(f,fieldnames=[
        '用户id',
        '用户',
        '评论日期',
        '评论内容'
    ])
    csv_writer.writeheader()   #创建表头
    mid = ''

    r = requests.get(url,headers=headers)
    json1 = json.loads(r.text, strict=False)
    # print(json1)
    try:
        datas = json1['data']
    except:
        return -1
    mid = datas['max_id']

    for data in datas['data']:
        dit = {
            '用户id':data['user']['id'],
            '用户':data['user']['screen_name'],
            '评论日期':data['created_at'],
            '评论内容':data['text'].split('<')[0]
        }
        print(dit)
        csv_writer.writerow(dit)
    for i in range(100):
        flag = 0
        try:
            url = "https://m.weibo.cn/comments/hotflow?id=" + str(id) + "&mid=" + str(id) + "&max_id=" + str(mid) + "&max_id_type=" + str(flag)
            r = requests.get(url, headers=headers)
            json1 = json.loads(r.text, strict=False)
            datas = json1['data']
        except:
            flag = 1
            url = "https://m.weibo.cn/comments/hotflow?id=" + str(id) + "&mid=" + str(id) + "&max_id=" + str(mid) + "&max_id_type=" + str(flag)
            r = requests.get(url, headers=headers)
            json1 = json.loads(r.text, strict=False)
            datas = json1['data']
        mid = datas['max_id']
        if mid == 0:  # 最后一页的max_id = 0用来结束循环
            break
        time.sleep(1)
        for data in datas['data']:
            dit = {
                '用户id': data['user']['id'],
                '用户': data['user']['screen_name'],
                '评论日期': data['created_at'],
                '评论内容': data['text'].split('<')[0]
            }
            print(dit)
            csv_writer.writerow(dit)
    return 1

def existdir():
    isExists = os.path.exists('微博')
    if not isExists:
        os.mkdir('微博')
    else:
        pass
    os.chdir('微博')

def crawlerW(oid):
    existdir()
    url = oid
    crawler(url)
    os.chdir('../')
    print("爬取完成！！！")

if __name__ == '__main__':
    print("请输入微博网址:")
    url1 = input()
    res = crawler(url1)


