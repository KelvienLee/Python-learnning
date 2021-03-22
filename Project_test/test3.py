import requests

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
    'path': '/c100010000-p100901/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'referer': "https://www.zhipin.com/web/common/security-check.html?seed=zhbwn0x0EZUDloMZPaAqHVsOYDBSQtHe66YsXRwXhS8%3D&name=3dc7c73c&ts=1615028868690&callbackUrl=%2Fc100010000-p100901%2F&srcReferer=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3Dzhbwn0x0EZUDloMZPaAqHVsOYDBSQtHe66YsXRwXhS8%253D%26name%3D3dc7c73c%26ts%3D1615028868197%26callbackUrl%3D%252Fc100010000-p100901%252F%26srcReferer%3Dhttps%253A%252F%252Fwww.zhipin.com%252Fweb%252Fcommon%252Fsecurity-check.html%253Fseed%253Dzhbwn0x0EZUDloMZPaAqHX4gm6KCkouSKdnIT2oM4Ts%25253D%2526name%253D3dc7c73c%2526ts%253D1615028867731%2526callbackUrl%253D%25252Fc100010000-p100901%25252F%2526srcReferer%253Dhttps%25253A%25252F%25252Fwww.zhipin.com%25252Fweb%25252Fcommon%25252Fsecurity-check.html%25253Fseed%25253Dzhbwn0x0EZUDloMZPaAqHX4gm6KCkouSKdnIT2oM4Ts%2525253D%252526name%25253D3dc7c73c%252526ts%25253D1615028867235%252526callbackUrl%25253D%2525252Fc100010000-p100901%2525252F%252526srcReferer%25253Dhttps%2525253A%2525252F%2525252Fwww.zhipin.com%2525252Fweb%2525252Fcommon%2525252Fsecurity-check.html%2525253Fseed%2525253Dzhbwn0x0EZUDloMZPaAqHfuQmo2sIw1vqZ1qgbvZ9%252525252Bg%252525253D%25252526name%2525253D3dc7c73c%25252526ts%2525253D1615028866716%25252526callbackUrl%2525253D%252525252Fc100010000-p100901%252525252F%25252526srcReferer%2525253Dhttps%252525253A%252525252F%252525252Fwww.zhipin.com%252525252F",
    'upgrade-insecure-requests': '1',
    'cookie': '__g=-; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.google.com%2F&g=&s=3&friend_source=0; lastCity=100010000; __c=1615028161; __a=94577129.1615028161..1615028161.4.1.4.4; __zp_stoken__=fcfabODoUSz8MOX9lOQ5URQEWSE5GG205GVI3KS8ocSo0GGpaPTlZKRw4WAI3c0Zlfldffyg2YXUGXzhfYnsqdTIwdmIWGB9PXVUCOC0PAVw7dEwYGxpoXxA9RAkHWyRZeAZVRm08HA52VXU8dA%3D%3D',
    'sec-fetch-des': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin'
}

url = 'https://www.zhipin.com/c100010000-p100901/'


r = requests.get(url=url, headers=headers)
r.encoding = 'utf-8'
c = r.text
print(c)




















