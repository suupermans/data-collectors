import requests
import json
import time
import csv
import execjs
import os

js_code = open('x_s.js', encoding='utf-8').read()
ctx = execjs.compile(js_code)
def crawler(pid,cursor):
    global dits,ctx
    url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id={}&cursor={}".format(pid,cursor)
    # 第一个参数为ja代码中的函数名, 后面为函数对应的参数
    # time.sleep(2)
    x_t = int((time.time()+8)*1000)
    print(str(x_t)+'test/api/sns/web/v2/comment/page?note_id='+str(pid)+'&cursor=')
    x_s = ctx.call('get_x', str(x_t)+'test/api/sns/web/v2/comment/page?note_id='+str(pid)+'&cursor='+str(cursor))
    print(x_t,x_s)
    headers = {
        "referer": "https://www.xiaohongshu.com/",
        "user-agent": "Mozilla/5.0(Windows NT 10.0; Win64; x64)AppleWebKit/537.36(KHTML, like Gecko)Chrome/108.0.0.0 Safari/537.36",
        "cookie": "a1=1863fc82a22frc98nhoukuwwz5dheb75wsyioroyv50000330561; webId=a73e00435be81747e88424490c51610f; gid=yYKqiSYJfdE4yYKqiSYJ0MFlJJiFSjYIxl7Tvvh7EEu2f328xdDW2l888qq82Ky8Y82d4Y80; gid.sign=tFOpSazWEtJ2kdna1dZqoXzCO2E=; xhsTrackerId=7b4e4740-ce70-4d4b-83a8-aab0b5ff4c5a; xhsTrackerId.sig=zAACsXyWfrGO5ux0nlzxJBmGxEpkx_Yd3eH1Lka0lXc; xsecappid=xhs-pc-web; xhsTracker=url=explore&xhsshare=QQ; xhsTracker.sig=iSWaEcun305KzSS3ZhAMZ5J8ORQ4gAiwUyB-ByOnu6o; web_session=0400698f28a05c564cfd42dade314b54abc684; extra_exp_ids=h5_1208_exp3,h5_1130_origin,ios_wx_launch_open_app_exp,h5_video_ui_exp3,wx_launch_open_app_duration_origin,ques_exp2; extra_exp_ids.sig=ua6MfqPmWNei3g281auEK3fEXC8GM_g6TlXVgkXr1I4; websectiga=3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2; sec_poison_id=6ddf23ac-ddb4-4ea6-a139-92d6de2c3167",
        "accept": "application/json",
        "content-type": "application/json;charset=utf-8",
        # "x-b3-traceid":"0fa5414ce957aa16",
        "x-s": x_s,
        "x-t": str(x_t),
    }
    print(url)
    try:
        r = requests.get(headers=headers,url = url)
        json1 = json.loads(r.text, strict=False)
        print(json1)
        datas = json1['data']
        print(datas)
        cur = datas['cursor']
        print(cur)
        for data in datas['comments']:
            id = data['id']
            nikename = data['user_info']["nickname"]
            content = data['content']
            t = int(data['create_time']//1000)
            time1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t))
            dit = {
                '用户id': id,
                '用户': nikename,
                '评论日期': time1,
                '评论内容': content
            }
            if content[0] == '@':
                continue
            else:
                dits.append(dit)
            print(dit)
        crawler(pid,cur)
    except:
        return
    return

    # print(dit)
def existdir():
    isExists = os.path.exists('小红书')
    if not isExists:
        os.mkdir('小红书')
    else:
        pass
    os.chdir('小红书')

dits = []
def crawlerX(pid):
    existdir()
    f = open(pid + ".csv", mode='w', newline='', encoding='utf-8-sig')
    csv_writer = csv.DictWriter(f, fieldnames=[
        '用户id',
        '用户',
        '评论日期',
        '评论内容'
    ])
    csv_writer.writeheader()  # 创建表头
    crawler(pid,"")
    # print(dits)
    for dit in dits:
        csv_writer.writerow(dit)
    os.chdir('../')
    print("爬取完成！！！")

if __name__ == '__main__':
    dits = []
    print("请输入note_id号:")
    pid = input()
    f = open(pid + ".csv", mode='w', newline='', encoding='utf-8-sig')
    csv_writer = csv.DictWriter(f, fieldnames=[
        '用户id',
        '用户',
        '评论日期',
        '评论内容'
    ])
    csv_writer.writeheader()  # 创建表头
    crawler(pid,'')
    print(dits)
    for dit in dits:
        csv_writer.writerow(dit)




