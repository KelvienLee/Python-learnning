import requests

url = 'https://lab.isaaclin.cn/nCoV/api/news'


def get_nCov_news(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except:
        return None


data = get_nCov_news(url)

if not data['results']:
    print('未获取到数据')
else:
    for i in range(10):
        title = data['results'][i]['title']
        summary = data['results'][i]['summary']
        infoSource = data['results'][i]['infoSource']
        sourceUrl = data['results'][i]['sourceUrl']
        print(f'第{i + 1}条\n标题：\n{title}\n\n内容:\n{summary}\n\n来源：\n{infoSource}\n\n原文：\n{sourceUrl}\n\n')
