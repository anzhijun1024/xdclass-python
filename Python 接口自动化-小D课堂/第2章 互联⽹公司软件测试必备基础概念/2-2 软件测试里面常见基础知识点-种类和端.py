import json
import requests

def Dingding(data1):
    business_number_941 = data1["data"][0]["shopId"]
    msg ="伍仔醉余额预警报告\n 商户号：{} \n 今日限额：{}\n 今日实时支出:{}".format(business_number_941,data1["data"][0]["limitMoney"],data1["data"][0]["today"])

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
    print(data)
    # 5、发送请求
    request = requests.post(url=url, data=sendData, headers=header)

    # 6、打印返回的结果
    print(request.text)


def requests_content():
    url = 'https://plineapi.hnwzz.cn/api/money/record/getWxList'
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJbXCJvbmVjb2RlXCIsXCIxXCIsXCI1MVwiLFwiMTA0XCJdIiwiZXhwIjoxNTk4NjY1MDIxfQ.QyCcOM4axLkpRJCNEs4cJdA8J0CAM-VsaPZ4aABgUT-vMdFEZwmPu1hKTOQ9SbhpmCxUK9jWXlR_FcY2fMLXCw'}
    # response = requests.get(url,headers=headers)
    # data = json.loads(response.text)
    data={"code":"0000","msg":"成功","data":[{"id":1,"name":"枸杞槟榔 槟榔贵族","shopId":"1581245941","mchKey":"GO7zSeARU0CHuWBjenlepg48w5Jr****","limitMoney":1950000.00,"remindMoney":1900000.00,"status":0,"thisMonth":5.37886258E7,"topMonth":4.586656189E7,"thisWeek":1.07704008E7,"topWeek":1.370208142E7,"today":973607.3,"yesterday":1950016.96},{"id":2,"name":"湘潭铺子槟榔","shopId":"1565067801","mchKey":"1234567890qwertyuiopasdfghjk****","limitMoney":1950000.00,"remindMoney":1900000.00,"status":0,"thisMonth":8574880.78,"topMonth":1546039.68,"thisWeek":2475408.08,"topWeek":3054747.88,"today":9.88,"yesterday":604365.32}],"timespan":0}
    return data


def data_aeeert(data):
    data1 = data

    # 限额
    limitMoney= data1["data"][0]["limitMoney"]
    today_money = data1["data"][0]["today"]

    print(limitMoney)
    print(today_money)
    a=[]
    a.append(today_money)
    print(a)
    print(type(today_money))

    if limitMoney-today_money<1000:

        print("需要上处理")
        msg = Dingding(data1)
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

