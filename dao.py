import json
import HttpUtil
import base64

class BhDao:
    def __init__(self):
        pass

    def login(self):
        url = "http://plus.app.baihe.com/register/login"
        params = {
            'channel': 'ios||iPhone OS##9.3.2||appstore||appstore_6.3.0',
            'plusCode': 'appstore',
            'mobile': '13047800414',
            'appId': '1',
            'plusPlatform': '1203',
            'plusChannel': 'appstore',
            'latitude': '22.5496226671007',
            'longitude': '113.924221191406',
            'password': '13047800414',
            'plusClientVersion': '6.3.0',
            'appUpgradeVersionCode': '',
            'plusPhoneOSVersion': 'iPhone OS##9.3.2',
            'plusPhoneModel': 'iPhone 6s Plus (A1634\/A1687\/A1699)',
            'device': 'iPhone',
            'apver': '6.3.0'
        }
        systemID = 2
        traceID = 1
        param_dict = {"params": json.dumps(params), "systemID": systemID, "traceID": traceID}
        result = HttpUtil.postForm(url, param_dict)
        data = json.loads(result)
        return data

    def search(self,index):
        url = "http://plus.app.baihe.com/search/searchUser"
        params = {
            "currentPageNumber": index,
            "district": "864403",
            "plusPhoneModel": "iPhone 6s Plus (A1634\/A1687\/A1699)",
            "plusChannel": "appstore",
            "maxAge": "25",
            "apver": "6.3.0",
            "channel": "ios||iPhone OS##9.3.2||appstore||appstore_6.3.0",
            "sorterField": "dynValue",
            "plusPhoneOSVersion": "iPhone OS##9.3.2",
            "plusClientVersion": "6.3.0",
            "maxHeight": "180",
            "gender": "1",
            "appRulerName": "AppSearchChannel",
            "pageRows": "20",
            "appId": "1",
            "plusCode": "appstore",
            "minAge": "19",
            "appUpgradeVersionCode": "",
            "minHeight": "155",
            "device": "iPhone",
            "plusPlatform": "1203"
        }
        result = HttpUtil.get(url, {"params": json.dumps(params), "systemID": 1, "traceID": 2})
        print(result)
        data = json.loads(result)
        return data

    def send(self, userID, content):
        url = "http://plus.app.baihe.com/msg/sendMessage"
        params = {
            "tempID": "8F45D60E46774ABCAF11FDAD01701FFD",
            "toUserID": userID,
            "userID": "121746294",
            "channel": "ios||iPhone OS##9.3.2||appstore||appstore_6.3.0",
            "plusCode": "appstore",
            "appId": "1",
            "plusPlatform": "1203",
            "plusChannel": "appstore",
            "type": "1",
            "plusClientVersion": "6.3.0",
            "appUpgradeVersionCode": "",
            "plusPhoneOSVersion": "iPhone OS##9.3.2",
            "pathID": "01.00.30301",
            "plusPhoneModel": "iPhone 6s Plus (A1634\/A1687\/A1699)",
            "device": "iPhone",
            "apver": "6.3.0",
            "content": base64.b64encode(content.encode()).decode()
        }
        systemID = 2
        traceID = 1
        param_dict = {"params": json.dumps(params), "systemID": systemID, "traceID": traceID}
        result = HttpUtil.postForm(url, param_dict)
        data = json.loads(result)
        return data


if __name__ == '__main__':
    dao = BhDao()
    print(dao.login())
    index=100
    result=dao.search(index)
    for user in result["data"]["result"]:
        print(dao.send(user["userID"],"你好，诚心交友，认识一下吧!"))
