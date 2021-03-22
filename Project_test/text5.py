import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime


def header():
    """
    伪造请求头
    :return: 请求头数据
    """
    ua = UserAgent(verify_ssl=False)
    agent = ua.random
    headers = {
        "User-Agent": agent
    }
    return headers


def get_html(url):
    """
    获取页面文本数据
    :param url: 目标页面url
    :return: requests对象
    """
    r = requests.get(url, headers=header())
    r.encoding = 'utf-8'
    html_text = r.text
    return html_text


def get_url_list(main_text):
    """
    获取首页下的推荐影片连接
    :param main_text: 页面文本数据
    :return: 影片列表
    """
    soup = BeautifulSoup(main_text, 'lxml')
    url_list_no = soup.find('ul', {'id': 'post_container'}).find_all('li')
    url_list = []
    for links in url_list_no:
        a = links.find('h2', {'style': 'font-size:15px'}).find('a').get('href')
        url_list.append(a)
    return url_list


def get_info(text):
    """
    读取子页面信息并写入excel
    :param text: 页面文本数据
    :return: 结果
    """
    soup = BeautifulSoup(text, 'lxml')
    c = str(soup.find('div', {'id': 'post_content'}).find_all('p')[1])
    d = c.replace('\u3000', '').replace('\u2002/\u2002', '').replace('\u2002', '').replace('\n', '').replace('<p>', '')\
        .replace('</p>', '').replace('◎', '').replace('\xa0', '')
    str_list = d.split('<br/>')
    try:
        info_tuple = (
            str(str_list[0]),
            str(str_list[1]),
            str(str_list[2]),
            str(str_list[3]),
            str(str_list[4]),
            str(str_list[5]),
            str(str_list[6]),
            str(str_list[7]),
            str(str_list[9]),
            str(str_list[11]),
            str(str_list[12]),
            str(str_list[13]),
        )
    except:
        info_tuple = ()
    ws.append(info_tuple)
    return None


def main(url):
    """
    主函数
    :param url: 首页url
    :return: 结果
    """
    main_a = get_html(url)
    main_list = get_url_list(main_a)
    i = 0
    for links in main_list:
        contents = get_html(links)
        get_info(contents)
        i += 1
        print(i)


if __name__ == '__main__':
    ws_title = ('译名', '片名', '年代', '产地', '类别', '语言', '上映时间', 'IMDB评分', '豆瓣评分', '片长', '导演', '主演/编剧')
    wb = Workbook()
    ws = wb.active
    ws.append(ws_title)
    main_url = 'https://www.yinfans.me/'
    main(main_url)
    wb.save(f'yinfans{datetime.now()}.xlsx')
