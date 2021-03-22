import requests
from fake_useragent import UserAgent
from openpyxl import Workbook
from datetime import datetime
from tqdm import tqdm


def agent():
    """
    伪造浏览器代理
    :return: 浏览器代理参数
    """
    # noinspection PyBroadException
    try:
        ua = UserAgent(verify_ssl=False)
        user_agent = ua.random
        return user_agent
    except Exception:
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' \
                     '(KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
    return user_agent


def get_content(url, i):
    """
    获取页面json内容并解析数据写入excel表格
    :param url: 目标页面URL
    :param i: 课程列表的页数
    :return: 写入结果
    """
    user_agent = agent()
    headers = {
        "user-agent": user_agent,
        "path": "/web/j/mocSearchBean.searchCourseCardByChannelAndCategoryId.rpc?"
                "csrfKey=f2aafd76b8ce44f1823178705a688aad",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        "edu-script-token": "f2aafd76b8ce44f1823178705a688aad",
        "cookie": "NTESSTUDYSI=f2aafd76b8ce44f1823178705a688aad; EDUWEBDEVICE=104f1348f83d4f289d670294ed879181;"
                  " WM_NI=Ga2kaJZdWC8Kpvoo6f8uU1DqSQ2D%2F6mlrg9XWS4bgysTw0i6YGit30ZDPkrGzC4jg1YZR50nKo%2BkeGumCWWMZ%"
                  "2F72KTmvP2bBVyfl8Qg53oIoTiuaD7c%2FHTWm%2B3NC%2BmqpeUk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb9cd7f98e7"
                  "a490eb7e97bc8fb6d45a969e8eaeb63c879fa5d0cd6097ef00b9b62af0fea7c3b92a85bffe8ce4429abc99a4bb41b4aaa190"
                  "b56efcab9bd2c77b918ffea5ae3eafb4be88bc54958dfc83e673b18cb9d1ec3e9b99a795b23c9a9ca08cf14dba9dfc8be63b"
                  "9b869ed6b36689b1e58ce84db7b38db8d6479af1f9d3ca60afaaa0d3e14a96a7aa8dbb5ba5ebfd90cc6598b7bb82c73da1f1"
                  "88b5d667e9ed82a4aa67b3b0abb6ea37e2a3; WM_TID=OSPqB3hh%2FHtFURQUAUJv0VQg7NGUxgX%2B;"
                  " __yadk_uid=ug32Jg9i4hbbMmCDGuvHBOzwH6k9NZTT"
    }
    data = {
        "mocCourseQueryVo": f'{{"categoryId":-1,"categoryChannelId":30001,"orderBy":0,"stats":30,"pageIndex":{i},'
                            f'"pageSize":20}}'
    }
    r = requests.post(url, headers=headers, data=data)
    content = r.json()
    course_list = content['result']['list']
    for item in course_list:
        try:
            if item['mocCourseBaseCardVo'] == None and item['mocCourseKyCardBulkPurchaseVo'] == None:
                course = item['mocCPkgKyCardBulkPurchInfoVo']
            elif item['mocCourseBaseCardVo'] == None:
                course = item['mocCourseKyCardBulkPurchaseVo']
            else:
                course = item['mocCourseBaseCardVo']

            if 'courseName' in course:
                course_tuple = (
                    course['courseName'],
                    course['teacherName'],
                    course['teacherName'],
                    course['enrollNum'],
                )
            else:
                course_tuple = (
                    course['name'],
                    course['schoolName'],
                    course['teacherName'],
                    course['enrollCount'],
                )
        except:
            course_tuple = ('广告投放课程', '已自动过滤', '', '')
        ws.append(course_tuple)


def main(url):
    """
    主函数，实现最终功能
    :param url: 目标页面URL
    :return: 最终结果
    """
    i = 0
    for index in tqdm(range(1, 11)):
        i += 1
        get_content(url, index)
        # print(f'第{i}页写入完成')


if __name__ == '__main__':
    ws_title = ['课程名称', '提供机构', '教师名称', '参加人数']
    html_url = 'https://www.icourse163.org/web/j/mocSearchBean.searchCourseCardByChannelAndCategoryId.rpc?' \
               'csrfKey=f2aafd76b8ce44f1823178705a688aad'
    wb = Workbook()
    ws = wb.active
    ws.append(ws_title)
    main(html_url)
    wb.save(f'中国大学mooc兴趣爱好分类课程数据{datetime.now()}.xlsx')
    print('all done')





















