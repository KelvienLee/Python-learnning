import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def f_user_agent():
    """
    伪造请求头
    :return: 请求头结果
    """
    # noinspection PyBroadException
    try:
        ua = UserAgent(verify_ssl=False)
        user_agent = ua.random
    except Exception:
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/89.0.4389.72 Safari/537.36'
    return user_agent


def get_post(url):
    """
    获取页面异步加载json数据
    :param url: 目标页面url
    :return: requests对象
    """
    # user_agent = f_user_agent()
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
        "edu-script-token": "f2aafd76b8ce44f1823178705a688aad",
        'origin': 'https://www.icourse163.org',
        'referer': 'https://www.icourse163.org/channel/2001.htm',
        'sec-ch-ua': 'Google Chrome";v="89","Chromium;v="89",";Not A Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        "content-type": "application/json;charset=UTF-8",
        "x-application-context": "mooc:online: 18382",
        'cookie': 'NTESSTUDYSI=f2aafd76b8ce44f1823178705a688aad; EDUWEBDEVICE=104f1348f83d4f289d670294ed879181; WM_NI=Ga2kaJZdWC8Kpvoo6f8uU1DqSQ2D%2F6mlrg9XWS4bgysTw0i6YGit30ZDPkrGzC4jg1YZR50nKo%2BkeGumCWWMZ%2F72KTmvP2bBVyfl8Qg53oIoTiuaD7c%2FHTWm%2B3NC%2BmqpeUk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb9cd7f98e7a490eb7e97bc8fb6d45a969e8eaeb63c879fa5d0cd6097ef00b9b62af0fea7c3b92a85bffe8ce4429abc99a4bb41b4aaa190b56efcab9bd2c77b918ffea5ae3eafb4be88bc54958dfc83e673b18cb9d1ec3e9b99a795b23c9a9ca08cf14dba9dfc8be63b9b869ed6b36689b1e58ce84db7b38db8d6479af1f9d3ca60afaaa0d3e14a96a7aa8dbb5ba5ebfd90cc6598b7bb82c73da1f188b5d667e9ed82a4aa67b3b0abb6ea37e2a3; WM_TID=OSPqB3hh%2FHtFURQUAUJv0VQg7NGUxgX%2B; __yadk_uid=ug32Jg9i4hbbMmCDGuvHBOzwH6k9NZTT'
    }
    data = {
        "csrfKey": "f2aafd76b8ce44f1823178705a688aad"
    }
    r = requests.post(url, headers=headers, data=data)
    json_post = r.json()
    return json_post


def parse_text(text):
    soup = BeautifulSoup(text, 'lxml')
    print(soup)


def main():
    html_url = 'https://www.icourse163.org/web/j/channelBean.getCustomCourseModuleVo.rpc'
    html_content = get_post(html_url)
    print(html_content)
    # parse_text(html_content)


if __name__ == '__main__':
    main()















