from bs4 import BeautifulSoup
import requests


def get_page(url):
    """
    获取页面内容
    :param url: url链接
    :return: BeautifulSoup对象
    """
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    return soup


def get_news_list(url):
    """
    获取列表页内容
    :param url: 列表URL
    :return: links列表
    """
    soup = get_page(url)
    news = soup.select('.banner-news ul li a')
    links = []
    for item in news:
        link = item.get('href')
        links.append(link)
    return links


def get_new_detail(url):
    """
    获取详细页信息
    :param url: URL连接
    :return: 详情页内容
    """
    soup = get_page(url)
    news_detail = {'title': soup.find('h1', {'class': 'am-article-title'}).string,
                   'publish_date': soup.select('.am-article-meta span')[0].string,
                   'view_count': soup.select('.am-article-meta span')[1].string,
                   'content': soup.find('div', {'class': 'am-article'}).text}
    return news_detail


def main():
    url = 'http://8.135.6.248/'
    links = get_news_list(url)
    news_list = []
    for link in links[1:]:
        news_detail = get_new_detail(link)
        news_list.append(news_detail)
    print(news_list)


if __name__ == '__main__':
    main()
