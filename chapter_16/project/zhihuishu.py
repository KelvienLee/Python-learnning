import requests
from openpyxl import Workbook
from fake_useragent import UserAgent
from datetime import datetime

ua = UserAgent(verify_ssl=False)
user_agent = ua.random
headers = {
    "User-Agent": user_agent,
    "Connection": "keep-alive"
}

html_url = 'https://bd-search.zhihuishu.com/bg_search/indexPageSearch/interestCourse?interestLabelId=11&courseType=-1&orderRuler=1&pageNo=0&pageSize=60&uuid=&dateFormate=1614676673000'

worksheet_title = ['课程ID', '课程名称', '讲师名称', '所属机构', '已学人数']


def get_info(url):
    r = requests.get(url, headers=headers)
    content = r.json()
    result = content["rt"]
    # info_list = []
    for item in result:
        info_tuple = (
            item['courseId'],
            item['courseName'],
            item['speakerName'],
            item['schoolName'],
            item['countUser'])
        # result = info_list.append(info_tuple)
        ws.append(info_tuple)
    # return result


def main(url):
    pass



if __name__ == "__main__":
    wb = Workbook()
    ws = wb.active
    ws.append(worksheet_title)
    get_info(html_url)
    wb.save(f'智慧树数据提取{datetime.now()}.xlsx')






























