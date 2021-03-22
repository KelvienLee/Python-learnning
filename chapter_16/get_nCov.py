import requests
from beautifultable import BeautifulTable

# response = requests.get(url)
# data = response.json()
# print(data['results'][0]['currentConfirmedCount'])

def get_nCov_info(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except:
        return None

city_name = input('查询省市:')
url = f'https://lab.isaaclin.cn/nCoV/api/area?latest=1&province={city_name}'
data = get_nCov_info(url)
if not data['results']:
    print('没有获取到数据')
else:
    currentConfirmedCount = data['results'][0]['currentConfirmedCount']
    confirmedCount = data['results'][0]['confirmedCount']
    suspectedCount = data['results'][0]['suspectedCount']
    curedCount = data['results'][0]['curedCount']
    deadCount = data['results'][0]['deadCount']
    table = BeautifulTable()
    table.column_headers = ['现存确诊人数', '累计确诊人数', '疑似感染人数', '治愈人数', '死亡人数']
    table.append_row([currentConfirmedCount, confirmedCount, suspectedCount, curedCount, deadCount])
    print(table)


