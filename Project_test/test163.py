import requests
from openpyxl import Workbook
from datetime import datetime


html_url = 'https://www.icourse163.org/web/j/mocSearchBean.searchCourseCardByChannelAndCategoryId.rpc' \
           '?csrfKey=f2aafd76b8ce44f1823178705a688aad'


def get_info(url, i):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
        'cookie': 'NTESSTUDYSI=f2aafd76b8ce44f1823178705a688aad; EDUWEBDEVICE=104f1348f83d4f289d670294ed879181; WM_NI=Ga2kaJZdWC8Kpvoo6f8uU1DqSQ2D%2F6mlrg9XWS4bgysTw0i6YGit30ZDPkrGzC4jg1YZR50nKo%2BkeGumCWWMZ%2F72KTmvP2bBVyfl8Qg53oIoTiuaD7c%2FHTWm%2B3NC%2BmqpeUk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb9cd7f98e7a490eb7e97bc8fb6d45a969e8eaeb63c879fa5d0cd6097ef00b9b62af0fea7c3b92a85bffe8ce4429abc99a4bb41b4aaa190b56efcab9bd2c77b918ffea5ae3eafb4be88bc54958dfc83e673b18cb9d1ec3e9b99a795b23c9a9ca08cf14dba9dfc8be63b9b869ed6b36689b1e58ce84db7b38db8d6479af1f9d3ca60afaaa0d3e14a96a7aa8dbb5ba5ebfd90cc6598b7bb82c73da1f188b5d667e9ed82a4aa67b3b0abb6ea37e2a3; WM_TID=OSPqB3hh%2FHtFURQUAUJv0VQg7NGUxgX%2B; __yadk_uid=ug32Jg9i4hbbMmCDGuvHBOzwH6k9NZTT',
        'path': '/web/j/channelBean.getCustomCourseModuleVo.rpc?csrfKey=f2aafd76b8ce44f1823178705a688aad',
        'edu-script-token': 'f2aafd76b8ce44f1823178705a688aad',
        'referer': 'https://www.icourse163.org/channel/2001.htm',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    data = {
        'mocCourseQueryVo': f'{{"categoryId":-1,"categoryChannelId":2001,"orderBy":0,"stats":30,"pageIndex":{i},"pageSize":20}}'
    }
    r = requests.post(url, headers=headers, data=data)
    j = r.json()
    json_list = j['result']['list']
    for item in json_list:
        course_list = item['mocCourseBaseCardVo']
        info_tuple = (course_list['name'], course_list['schoolName'], course_list['teacherName'], course_list['enrollCount'])
        ws.append(info_tuple)


def get_more_page(url):
    for index in range(1, 11):
        get_info(url, index)
        print(f'第{index}页写入完成')


if __name__ == '__main__':
    ws_title = ['课程名称', '教学机构', '教师名称', '参加人数']
    wb = Workbook()
    ws = wb.active
    ws.append(ws_title)
    get_more_page(html_url)
    wb.save(f'中国大学MOOC国家精品课程{datetime.now()}.xlsx')
    print('所有数据写入完成')

















