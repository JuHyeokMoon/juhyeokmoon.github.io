import os
import sys
import urllib.request
import json
import math
import re
from bs4 import BeautifulSoup

def call(keyword, start, news_sort):
    url = "https://openapi.naver.com/v1/search/news?query=" + \
        keyword + "&display=10" + \
        "&sort=" + news_sort + "&start=" + str(start)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)

    print(response)  # Response [200]
    return json.load(response)


def get_news_results(keyword, news_display, news_sort):
    list = []

    rangeNum = int(math.ceil(news_display/10))
    print(rangeNum)
    if rangeNum <= 0:
        rangeNum = 1

    for num in range(0, rangeNum):
        list = list + call(keyword, num * 10 + 1, news_sort)['items']
        # list.append(call(keyword, num * 10 + 1, news_sort)['items'])
    return list

client_id = "rEDDi0DeZa6Xc_xl9CzI"
client_secret = "i4EJ1uWD_R"
keyword = urllib.parse.quote("전기차")

news_display = 30  # 10 단위
news_sort = "sim"  # or date

news_list = get_news_results(keyword, news_display, news_sort)
print(news_list)

# with open('test.json', 'w', encoding='utf-8') as make_file:
#     json.dump(news_list, make_file, indent="\t",
#               ensure_ascii=False)
