import requests
from openpyxl import Workbook
from datetime import datetime


def get_page(index):
    payload = {
        'activityId': 0,
        'keyword': "c语言",
        'orderType': 5,
        'pageIndex': index,
        'pageSize': 50,
        'priceType': -1,
        'qualityType': 0,
        'relativeOffset': 0,
        'searchTimeType': -1
    }

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }

    url = 'https://study.163.com/p/search/studycourse.json'
    try:
        r = requests.post(url, headers=headers, json=payload)
        data = r.json()
        if data and data["code"] == 0:
            return data
    except RuntimeError:
        print('出错了，获取数据失败')


def get_course(data):
    course_list = data["result"]["list"]
    return course_list


def main(index):
    data = get_page(index)
    course_list = get_course(data)
    for course in course_list:
        course_tuple = (course['productId'], course['courseId'], course['productName'], course['provider'],
                        course['lectorName'], course['score'], course['learnerCount'], course['lessonCount'],
                        course['originalPrice'], course['discountPrice'])
        ws.append(course_tuple)


if __name__ == "__main__":
    ws_title = ['商品id', '课程id', '课程名称', '机构名称', '讲师名称', '评分', '学习人数', '课程节数', '原价', '折扣价']
    wb = Workbook()
    ws = wb.active
    ws.append(ws_title)
    total_page_count = get_page(1)['result']['query']['totlePageCount']
    for index in range(1, total_page_count+1):
        main(index)
    wb.save(f'网易云C语言课程信息{datetime.now()}.xlsx')

































