from datetime import datetime
from time import sleep
import requests


print('hell world')

url = 'http://weiguang19.xyz'

r = requests.get(url)
r.encoding = 'utf-8'
print(r.text)
