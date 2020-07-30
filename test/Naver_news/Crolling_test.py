import os
import sys
import urllib.request
import json
import math
from bs4 import BeautifulSoup
import sys
import datetime
import re


def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL,
                         "html.parser", from_encoding='utf-8')
    text1 = soup.select('#articleBody')
    text = soup.select('#articleBody')[0].get_text().replace('\n', " ")
    #print('전처리 전')
    #print(text)
    text = text.replace(
        "// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', text)
    text = re.sub('\▲', '', text)
    text = re.sub('\▶.*$', '', text)
    text = re.sub(' +', ' ', text)
    #print('전처리 후')
    #print(text)
    return text


def get_title(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL,
                         "html.parser", from_encoding='utf-8')
    text = ''
    for item in soup.find_all('h3', id='articleTitle'):
        text = text + str(item.find_all(text=True))
        text = re.sub(
            '[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', text)
    return text


url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=001&aid=0011778581'
my_text = get_text(url)
my_title = get_title(url)

#print(my_text)
print(my_title)

now_date = datetime.datetime.now().strftime('%Y%m%d')
# now_time = datetime.datetime.now().strftime('%H%M%S')
file_name = "news_"+'.json'
path = now_date

if not os.path.isdir(path):
    os.mkdir(path)

news = {}
news['title'] = my_title
news['text'] = my_text

with open(path+"/"+file_name, 'w', encoding='utf-8') as make_file:
    json.dump(news, make_file, indent="\t",
              ensure_ascii=False)
