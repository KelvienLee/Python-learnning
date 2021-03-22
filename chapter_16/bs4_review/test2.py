import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
user_agent = ua.random
headers = {
    "User-Agent": user_agent
}


def get_info(url):
    try:
        response = requests.get(url, headers=headers)
        return response
    except RuntimeError:
        print('获取数据异常')


html_url = 'http://www.wenzizhan.com/'
req_response = get_info(html_url)
req_text = req_response.text

soup = BeautifulSoup(req_text, 'lxml')
li = soup.select('.ulhot li a')
links = []
for item in li:
    link = item.get('href')
    links.append(link)

content_list = []

for link_url in links:
    content_dict = {}
    req_branch = get_info(link_url)
    req_branch_text = req_branch.text
    soup_b = BeautifulSoup(req_branch_text, 'lxml')
    content_dict['title'] = soup_b.find('div', {'class': 'mainTitle'}).find('h1').string
    main_content = str(soup_b.find('div', {'class': 'mainContent'}))
    content_dict['main_content_str'] = main_content.replace('<div class="mainContent">', '').replace('<br/>', '').replace('</div>', '')
    content_list.append(content_dict)

exit()

i = 0
for li_con in content_list:
    i += 1
    con_title = li_con['title']
    con_main = li_con['main_content_str']
    con_result = con_title + con_main
    with open(f'{con_title}.txt', 'w') as file:
        file.write(con_result)





























