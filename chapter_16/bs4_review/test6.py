#!/home/kelvin/venv/bin/python
import requests
from bs4 import BeautifulSoup
from my_fake_useragent import UserAgent
import os
from datetime import datetime

ua = UserAgent(family='chrome')
# <#!/home/kelvin/Applications/Virtualenv/test_venv/bin/python3>
user_agent = ua.random()
headers = {
    'User-Agent': user_agent
}

html_url = input('url:')
# html_url = input('url:')


def get_text(url):
    """
    使用requests获取页面文本内容
    :param url: 目标页面url
    :return: 输出页面文本内容
    """
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    r_text = r.text
    return r_text


def get_content(url):
    """
    获取二进制文件
    :param url: 输入目标url
    :return: 输出文件二进制数据
    """
    rb = requests.get(url, headers=headers)
    rb_content = rb.content
    return rb_content


def get_pic_link_title(text):
    """
    获取页面的图片链接列表和图片名称
    :param text: 传入页面内容
    :return: 输出图片链接和名称列表
    """
    bs_c = BeautifulSoup(text, 'lxml')
    pic_list = bs_c.find('div', {'class': 'content'}).find_all('img')
    links = []
    for item in pic_list:
        pic_link = item.get('src')
        links.append(pic_link)
    title = []
    for title_item in pic_list:
        pic_title = title_item.get('alt')
        title.append(pic_title)
    pic_l_t = [links, title]
    return pic_l_t


def get_how_pages(url):
    """
    获取图组共有多少页并提取链接
    :param url: 首页url
    :return: 输出图组url列表
    """
    html_text = get_text(url)
    bs4_c = BeautifulSoup(html_text, 'lxml')
    pages = bs4_c.find('div', {'id': 'pages'}).find_all('a')
    page_list_no = []
    for item in pages:
        link = item.get('href')
        page_list_no.append(link)
    page_list = page_list_no[1:-1]
    return page_list


def down_pic(url, title):
    """
    获取数据保存到本地
    :param url: 目标文件地址
    :param title: 命名规则
    :return: 将数据保存到本地并作出反馈
    """
    root_path = os.getcwd()
    path = os.path.join(root_path, f'{t}{os.sep}')
    # print(path)
    # exit()
    pic_content = get_content(url)
    with open(f'{path}' f'{title}.jpg', 'wb') as pic:
        pic.write(pic_content)
    print(f"{title}_ok")


def get_all_pic(url):
    """
    主函数，获取文件内容并保存到本地
    :param url: 目标页面url
    :return: 结果
    """
    os.mkdir(t)
    html_text = get_text(url)
    first_pic_links_list = get_pic_link_title(html_text)
    i = 0
    for pic_url in first_pic_links_list[0]:
        down_pic(pic_url, title=first_pic_links_list[1][i])
        i += 1
    print('第1页写入完成')
    page_list = get_how_pages(url)
    pointer = 1
    for page_url in page_list:
        pages_content = get_text(page_url)
        pic_u_t = get_pic_link_title(pages_content)
        j = 0
        for page_pic_content in pic_u_t[0]:
            down_pic(page_pic_content, title=pic_u_t[1][j])
            j += 1
        pointer += 1
        print(f"第{pointer}页写入完成")
    return '所有数据写入完成'


if __name__ == "__main__":
    t = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    result = get_all_pic(html_url)
    print(result)
