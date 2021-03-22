# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# import re
# from openpyxl import Workbook
#
# ua = UserAgent(verify_ssl=False)
# user_agent = ua.random
#
# headers = {
#     "User-Agent": user_agent
# }
#
# html_url = 'https://movie.douban.com/top250'
#
#
#
# def get_info(url):
#     r = requests.get(url, headers=headers)
#     r_text = r.text
#     return r_text
#
#
# def soup_info(content):
#     soup = BeautifulSoup(content, 'lxml')
#     main_ul = soup.find('ol', class_='grid_view').find_all('li')
#     info_list = []
#     for item1 in main_ul:
#         main_title = item1.find('div', class_='hd').find_all('span', class_='title')
#         title_list = []
#         for item2 in main_title:
#             title = item2.string.replace('\xa0/\xa0', '')
#             title_list.append(title)
#         other_title = item1.find('div', class_='hd').find('span', class_='other').string.replace('\xa0/\xa0', '').replace(' ', '')
#         dir_ac_sor_no = item1.find('div', class_='bd').p.text.replace(' ', '').replace('\xa0/\xa0', '').replace('\n', '')
#         star = item1.find('div', class_='bd').find('span', class_='rating_num').string
#         quote = item1.find('div', class_='bd').find('span', class_='inq').string
#         rand_num_no = item1.find('div', class_='bd').find('div', class_='star').find_all('span')[3]
#         for item3 in rand_num_no:
#             rand_num = item3.string
#         dir_ac_sor = dir_ac_sor_no.split('\xa0\xa0\xa0')
#         director = dir_ac_sor[0]
#         if len(dir_ac_sor) == 2:
#             act_and_sort = dir_ac_sor[1].split('...')
#         else:
#             act_and_sort = dir_ac_sor[0]
#         act = act_and_sort[0]
#         if len(act_and_sort) == 2:
#             sort = act_and_sort[1]
#         else:
#             sort = act_and_sort[0]
#         year = re.findall(r'\d{4}', sort)
#         year_end = year[0]
#         if len(title_list) == 2:
#             title_end = f"{title_list[0]} {title_list[1]}"
#         else:
#             title_end = f"{title_list[0]}"
#         # print(title_end)
#         # exit()
#         info_list.append([title_end, other_title, director, act, year_end, sort, star, rand_num, quote])
#         # print(f"名称：{title_list}")
#         # print(f"别称：{other_title}")
#         # print(f"导演:{director}")
#         # print(f"演员:{act}")
#         # print(f"年份：{year}")
#         # print(f"分类：{sort}")
#         # print(f"评分:{star}")
#         # print(f"评价人数：{rand_num}")
#         # print(f"描述：{quote}")
#         # print('\n\n')
#     return info_list
#
#
# def main():
#     pass
#
#
# if __name__ == "__main__":
#     url_1 = 'https://movie.douban.com/top250?start=0&filter='
#     wb = Workbook()
#     ws = wb.active
#     ws_title = ['名称', '别名', '导演', '主演', '年份', '地域及分类', '评分', '评价人数', '描述']
#     ws.append(ws_title)
#     k = 0
#     for i in range(0, 250, 25):
#         k += 1
#         end_url = f"https://movie.douban.com/top250?start={i}&filter="
#         html_content = get_info(end_url)
#         list_1 = soup_info(html_content)
#         print(list_1)
#         print(k)
#     wb.save('hello.xlsx')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
