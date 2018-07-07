import requests
from urllib.request import urlretrieve
import os
headers = {
        'Accept - Charset': 'UTF - 8',
        'Accept - Encoding': 'gzip, deflate',
        'Content - type': 'application / x - www - form - urlencoded',
        'User - Agent': 'Dalvik / 2.1.0(Linux; U;Android 6.0.1;MI 5sMIUI / V8.0.18.0.MAGCNDI)',
        'Host': 'gamehelper.gm825.com',
        'Connection': 'Keep - Alive'
    }
urls = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=1F361282067F133CFB6A393486AA73FF&ovr=6.0.1&device=Xiaomi_MI+5s&net_type=1&client_id=LYY3F1NCtr5ODdbunHnv0w%3D%3D&info_ms=bRMqYzuG%2Fvk7C8x3EM4zug%3D%3D&info_ma=9mVZQyCbJHtzVXp1S4rKszNmECl34sYPedH8C84v7Ro%3D&mno=0&info_la=iu%2FWk1ewIsurU2meVXgo1w%3D%3D&info_ci=iu%2FWk1ewIsurU2meVXgo1w%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=ZI2yhJSaNYxd2RUWVBMlaR%2F6eLPYX6vDzcBkkAqswWY%3D&os_level=23&os_id=617934a8f5ba3e0c&resolution=1080_1920&dpi=480&client_ip=192.168.1.4&pdunid=ecb847cf"
detail_url = "http://gamehelper.gm825.com/wzry/hero/detail?hero_id=121&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=13.0.1.0&version_code=13010&cuid=1F361282067F133CFB6A393486AA73FF&ovr=6.0.1&device=Xiaomi_MI+5s&net_type=1&client_id=LYY3F1NCtr5ODdbunHnv0w%3D%3D&info_ms=bRMqYzuG%2Fvk7C8x3EM4zug%3D%3D&info_ma=9mVZQyCbJHtzVXp1S4rKszNmECl34sYPedH8C84v7Ro%3D&mno=0&info_la=iu%2FWk1ewIsurU2meVXgo1w%3D%3D&info_ci=iu%2FWk1ewIsurU2meVXgo1w%3D%3D&mcc=0&clientversion=13.0.1.0&bssid=ZI2yhJSaNYxd2RUWVBMlaR%2F6eLPYX6vDzcBkkAqswWY%3D&os_level=23&os_id=617934a8f5ba3e0c&resolution=1080_1920&dpi=480&client_ip=192.168.1.4&pdunid=ecb847cf "

def image(url,header):
    response = requests.get(url,headers).json()
    path = "imag"
    for each in response['list']:
        hero_url = each['cover']
        hero_name = each['name'] + '.jpg'
        filename = path +'/'+hero_name
        if path not in os.listdir():
            os.makedirs(path)
        urlretrieve(url=hero_url, filename=filename)




if __name__ == '__main__':

     image(urls,headers)
     # response = requests.get(detail_url, headers).json()
     # print(response['info'])


