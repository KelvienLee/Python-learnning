import requests
from beautifultable import BeautifulTable

url = 'https://lab.isaaclin.cn/nCoV/api/area?latest=1&province=北京市'


def get_ncov_info(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except RuntimeError:
        print('未获取到数据')


data = get_ncov_info(url)
if not data['results']:
    print('输入错误或不完整')
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





































