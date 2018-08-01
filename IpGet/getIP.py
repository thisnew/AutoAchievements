# coding=utf-8
#import urllib.request
import urllib3
import json
if __name__ == '__main__':
    # json = urllib.request.urlopen("http://api.ipstack.com/check?access_key=aefc901050f6aa3add1c0255ef0f1b11&format=1&output=json")
    # print(json.read())
    url = 'http://api.ipstack.com/check?access_key=aefc901050f6aa3add1c0255ef0f1b11&format=1&output=json'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }
    request = urllib3.PoolManager().request('GET',url,headers=header)
    data = request.data.decode()
    print(data)

    data = json.loads(data)
    print(data['ip'])
    print(data['latitude'])
    print(data['longitude'])

# "ip"
# "type"
# "continent_code"
# "continent_name"
# "country_code"
# "country_name"
# "region_code"
# "region_name"
# "city"
# "zip"
# "latitude"
# "longitude"
# "location"
#     "geoname_id"
#     "capital"
#     "languages" [{"code": "zh","name": "Chinese","native": "\u4e2d\u6587"}]
#     "country_flag"
#     "country_flag_emoji"
#     "country_flag_emoji_unicode"
#     "calling_code"
#     "is_eu"