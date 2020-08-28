import json
import requests

import  requests
# import demjson






def Dingding():


    msg = "python向钉钉消息发送成功报告 文杰兄加油了，主体流程已经调通"
    # 1、构建url
    url ="https://oapi.dingtalk.com/robot/send?access_token=b6d85a8c41ec8612e02be01c5462979fe04ac581aed6040248bca223243c0fee"  # url为机器人的webhook

    # 2、构建一下请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    # 3、构建请求数据
    data = {
        "msgtype": "text",
        "text": {
            "content":msg
        },
        "at": {
            "isAtAll": True  # @全体成员（在此可设置@特定某人）
        }
    }

    # 4、对请求的数据进行json封装
    sendData = json.dumps(data)  # 将字典类型数据转化为json格式
    sendData = sendData.encode("utf-8")  # python3的Request要求data为byte类型

    # 5、发送请求
    request = requests.post(url=url, data=sendData, headers=header)

    # 6、将请求发回的数据构建成为文件格式
    print(request.text)

    # opener = request.open(request)
    # # # 7、打印返回的结果
    # print(opener.read())
    return msg


def requests_content():

    # url = 'https://plineapi.hnwzz.cn/api/money/record/getWxList'

    # headers = {
        # 'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJbXCJvbmVjb2RlXCIsXCIxXCIsXCI1MVwiLFwiMTA0XCJdIiwiZXhwIjoxNTk4NjIxMTI5fQ.9sh1KZ2gnEwjJvMjEBfrBRyuNRnBCYLAWMgs3T9kwJJbO0Hq8mXN5sMCr2QCEo0TnCtVnPVGcAGlsNRmPnLkMw'}
    # response = requests.get(url,headers=headers)

    data = {"code": "0000", "msg": "成功", "data": [
        {"id": 1, "name": "枸杞槟榔 槟榔贵族", "shopId": "1581245941", "mchKey": "GO7zSeARU0CHuWBjenlepg48w5Jr****",
         "limitMoney": 1950000.00, "remindMoney": 1900000.00, "status": 0, "thisMonth": 5.281499186E7,
         "topMonth": 4.586656189E7, "thisWeek": 9796667.7, "topWeek": 1.370208142E7, "today": 1950016.96,
         "yesterday": 1996576.18},
        {"id": 2, "name": "湘潭铺子槟榔", "shopId": "1565067801", "mchKey": "1234567890qwertyuiopasdfghjk****",
         "limitMoney": 1950000.00, "remindMoney": 1900000.00, "status": 0, "thisMonth": 8294070.76,
         "topMonth": 1546039.68, "thisWeek": 2194706.3, "topWeek": 3054747.88, "today": 323511.54,
         "yesterday": 487421.72}], "timespan": 0}

    return data









def data_aeeert(data):
    data = data

    # 限额
    limitMoney= data["data"][0]["limitMoney"]
    today_money = data["data"][0]["today"]

    print(limitMoney)
    print(today_money)

    if today_money > limitMoney:

        print("需要上处理")
        msg = Dingding()
        print(msg)
    else:
        print('正常')











def main():


    # 拿到接口数据
    data = requests_content()


    # 对接口的数据断言 并发送钉钉消息
    data_aeeert(data)






if __name__ == '__main__':
    main()

