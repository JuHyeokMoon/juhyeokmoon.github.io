import requests

url = 'http://localhost:7777/list2'
name = '문주혁'
content = '안녕하세요, restful 테스트 입니다.'
data = {'name':name, 'content':content}

# requests.post(url=url, data=data)

response = requests.get(url=url, data=data)
print(response.text)

