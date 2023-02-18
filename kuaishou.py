import requests
import csv #方便存储数据
import os
import time

def callback(next_str_value,photoId):
    global dits
    url = "https://www.kuaishou.com/graphql"
    head = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46",
        "Cookie" : "did=web_c746d31654a566f08fa1375a6908f797; didv=1670143728343; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; soft_did=1619580708547; _bl_uid=10lCyb40eCtqqd7kk2hXl1kn89I9; client_key=65890b29; kuaishou.web.cp.api_st=ChZrdWFpc2hvdS53ZWIuY3AuYXBpLnN0EqABgnwTfQkm_XXKzQQWpglFV-M6g9GmTnh5hWn7ZHASEnlv4KDPqV0YdRAS_sAS3fBrQQytPJOXv6GuguuaKO5s68aGnsMxTAv1ftDaq-971FI8K69EbtfRZYBUIuNFxGNoqv0Nz-aOvjqBbigpyDMD6hyzy9MfvFovNhyid3E-Ab0jE6_6TnYUz8LYUZ__AEHxkQHsGYavR3XuKhzAuZAdVxoSw3qBS3pld45Ots5myM_60sjTIiBpQJnPZxZAq8WFjSraVLxHVUJEpvOjeQnACaPjOhmHdigFMAE; kuaishou.web.cp.api_ph=e13f0ba0a9021465a14191a295ab3cf683a4; ksliveShowClipTip=true; userId=2057276035; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABElRJTtJTYwSvi7UFU57Sme0ePwqtQU7PRIgZSfAJ51Qtd42NMKh6xtcayMKc3rUqKM62kw95HPdNlRIPfe9VrPe8MDNsMJzOs3TBK8qtzKNl-c8UJkSZ7aQnhkSgtTYXPexLjwj5HKthbmtE7XypiNqn25zCnITYH7iWv9AHjEuoQOm4ijiaEjnYO2cdijL_CkKexv8dmNv3r2NHUO7L-BoS-1Rj5-IBBNoxoIePYcxZFs4oIiANWvyOwIUaStVVHdGa_T9z7SD8d7a4lMVz3_oOs0fnhygFMAE; kuaishou.server.web_ph=f53cb27f0b53c9383770feaa399d7c7bbe4a"
    }
    value = {
      "operationName": "commentListQuery",
      "variables": {
        "photoId": photoId,
        "pcursor": next_str_value
      },
      "query": "query commentListQuery($photoId: String, $pcursor: String) {\n  visionCommentList(photoId: $photoId, pcursor: $pcursor) {\n    commentCount\n    pcursor\n    rootComments {\n      commentId\n      authorId\n      authorName\n      content\n      headurl\n      timestamp\n      likedCount\n      realLikedCount\n      liked\n      status\n      subCommentCount\n      subCommentsPcursor\n      subComments {\n        commentId\n        authorId\n        authorName\n        content\n        headurl\n        timestamp\n        likedCount\n        realLikedCount\n        liked\n        status\n        replyToUserName\n        replyTo\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    return_json = requests.post(url=url,headers=head,json=value)
    return_json_to_json = return_json.json()
    try:
        data = list(return_json_to_json["data"]["visionCommentList"]["rootComments"])
        next_pcursor =str(return_json_to_json["data"]["visionCommentList"]["pcursor"])
    except:
        print("爬取成功")
        return
    for i in data:
        authorname = i["authorName"]
        content= i["content"]
        print(authorname," : ",content)
        time1 = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['timestamp'] // 1000)))
        dit = {
            '用户id': i['authorId'],
            '用户': i["authorName"],
            '评论日期': time1,
            '评论内容': i["content"]
        }
        print(dit)
        if i["content"][0] == '@':
            continue
        else:
            dits.append(dit)
    callback(next_pcursor,photoId)
    return 1

def existdir():
    isExists = os.path.exists('快手')
    if not isExists:
        os.mkdir('快手')
    else:
        pass
    os.chdir('快手')

dits = []
def crawlerK(pid):
    existdir()
    f = open(pid + ".csv", mode='w', newline='', encoding='utf-8-sig')
    csv_writer = csv.DictWriter(f, fieldnames=[
        '用户id',
        '用户',
        '评论日期',
        '评论内容'
    ])
    csv_writer.writeheader()  # 创建表头
    callback('', pid)
    # print(dits)
    for dit in dits:
        csv_writer.writerow(dit)
    os.chdir('../')
    print("爬取完成！！！")

if __name__ == '__main__':
    dits = []
    print("请输入id")
    pid = input()
    f = open(pid+".csv",mode ='w',newline='',encoding='utf-8-sig')
    csv_writer = csv.DictWriter(f,fieldnames=[
        '用户id',
        '用户',
        '评论日期',
        '评论内容'
    ])
    csv_writer.writeheader()   #创建表头
    callback('',pid)
    print(dits)
    for dit in dits:
        csv_writer.writerow(dit)