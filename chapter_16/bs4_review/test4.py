import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
user_agent = ua.random

headers = {
    "User-Agent": user_agent
}

# html_url = 'https://www.tupianzj.com/meinv/20181211/175827.html'
html_url = input('请输入网址：')
list_html = html_url[:-5]


def get_info(url):
    """
    使用requests获取页面内容
    :param url: 目标页面
    :return: 获取到的页面数据
    """
    response = requests.get(url, headers=headers)
    response.encoding = 'gb2312'
    return response


def bs4_get_pictures(content):
    """
    使用bs4从页面中解析出图片
    :param content: requests获取到的数据
    :return: 返回图片二进制数据
    """
    soup_content = BeautifulSoup(content, 'lxml')
    pic = soup_content.find('div', {'id': 'bigpic'}).find_all('a')[1].img
    pic_content = pic.get('src')
    return pic_content


def get_how_pages(pages_url):
    """
    提取该图组共有多少页
    :param pages_url: 图组首页
    :return: 返回该图组共有多少页
    """
    pages = get_info(html_url)
    pages.encoding = 'gb2312'
    pages_content = pages.text
    pages_soup = BeautifulSoup(pages_content, 'lxml')
    pages_div = pages_soup.find('div', {'class': 'pages'}).ul.li.a.string
    pages_info = str(pages_div[1:3])
    pages_count = int(pages_info) + 1
    return pages_count


def get_all_pic(url):
    """
    主函数，获取图片并存入本地
    :param url: 图组链接
    :return: 最终结果
    """
    r_first = get_info(html_url)
    content_first = r_first.text
    link_first = bs4_get_pictures(content_first)
    first_pic = get_info(link_first)
    first_result = first_pic.content
    with open('1.jpg', 'wb') as first_file:
        first_file.write(first_result)
    print('第1张采集完成')

    how_pages = get_how_pages(url)
    for i in range(how_pages):
        if i == 0 or i == 1:
            continue
        else:
            pages_url = f'{list_html}_{i}.html'
            pic = get_info(pages_url)
            content = pic.text
            pic_link = bs4_get_pictures(content)
            pic_content = get_info(pic_link)
            result = pic_content.content
            with open(f"{i}.jpg", 'wb') as file:
                file.write(result)
            print(f"第{i}张采集完成")
    print('所有数据采集完毕')


if __name__ == "__main__":
    get_all_pic(html_url)
