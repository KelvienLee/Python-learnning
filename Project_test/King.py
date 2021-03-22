import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}


def get_content(word):
    try:
        url = f'http://www.iciba.com/word?w={word}'
        r = requests.get(url, headers=header)
        r.encoding = "utf-8"
        content = r.text
        soup = BeautifulSoup(content, 'lxml')
        d = soup.find('ul', {'class': 'Mean_part__1RA2V'}).get_text().split(';')
        for i in d:
            print(i)
    except Exception:
        print('单词不存在或输入不正确')


if __name__ == '__main__':
    the_word = input('input the word that you want to check:')
    get_content(the_word)
