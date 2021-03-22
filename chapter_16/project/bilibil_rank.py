import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime


html_url = 'https://www.bilibili.com/v/popular/rank/all'

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}


def get_info(url):
    r = requests.get(url, headers=headers)
    html_text = r.text
    r.encoding = 'utf-8'
    return html_text


def get_list(text):
    soup = BeautifulSoup(text, 'lxml')
    rank_list = soup.find('ul', {'class': 'rank-list'}).find_all('li')
    for item in rank_list:
        title = item.find('div', class_='content').find('div', class_='info').a.string
        details = item.find('div', class_='content').find('div', class_='info').find_all('span', class_='data-box')
        up_name_no = item.find('div', class_='content').find('div', class_='info').find('div', class_='detail').a.span
        play = details[0].text.replace('\n', '').strip()
        view = details[1].text.replace('\n', '').strip()
        up_name = up_name_no.text.replace('\n', '').strip()
        info_dict = (
            title,
            play,
            view,
            up_name
        )
        ws.append(info_dict)
    return '写入完成'


if __name__ == "__main__":
    wb = Workbook()
    ws = wb.active
    ws_title = ['稿件名称', '播放量', '弹幕数', 'UP主']
    ws.append(ws_title)
    main_text = get_info(html_url)
    get_list(main_text)
    wb.save(f'bilibili排行榜实时数据{datetime.now()}.xlsx')
    print('写入完成')






















