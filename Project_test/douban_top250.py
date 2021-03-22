import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime


def get_cur_page_info(url):
    """
    获取当前页面信息
    :param url: 当前页面url
    :return: 当前页面文本内容
    """
    ua = UserAgent(verify_ssl=False)
    user_agent = ua.random
    headers = {
        "User-Agent": user_agent,
        "Connection": "keep - alive"
    }
    r = requests.get(url, headers=headers)
    html_text = r.text
    return html_text


def parse_text(text):
    soup = BeautifulSoup(text, 'lxml')
    all_li = soup.find('ol', class_='grid_view').find_all('li')
    info_list = []
    for film_info in all_li:
        rank = film_info.find('em', class_='').string
        title = film_info.find('span', class_='title').string
        dir_act = film_info.find('p', class_='').text.replace(' ', '').replace('\n', '').replace('\xa0\xa0\xa0', ' ')\
            .replace('\xa0/\xa0', '').replace('...', ' ')
        dir_act_sort = dir_act.split(' ')
        if len(dir_act_sort) == 3:
            director = dir_act_sort[0]
            act = dir_act_sort[1]
            sort = dir_act_sort[2]
        else:
            director = dir_act_sort[0]
            act = dir_act_sort[1]
            sort = dir_act_sort[1]
        rating = film_info.find('span', class_='rating_num').string
        # noinspection PyBroadException
        try:
            quote = film_info.find('span', class_='inq').string
        except Exception:
            quote = ''

        info_list.append([rank, title, director, act, sort, rating, quote])
    return info_list


def get_all_pages():
    page_pointer = 1
    for i in range(0, 250, 25):
        print(f"第{page_pointer}页")
        page_pointer += 1
        url_list = f'https://movie.douban.com/top250?start={i}&filter='
        page_text = get_cur_page_info(url_list)
        test_result = parse_text(page_text)
        for test in test_result:
            ws.append(test)


if __name__ == '__main__':
    wb = Workbook()
    ws = wb.active
    ws_title = ['排名', '名称', '导演', '主演', '分类', '评分', '描述']
    ws.append(ws_title)
    get_all_pages()
    wb.save(f'豆瓣top250数据{datetime.now()}.xlsx')
