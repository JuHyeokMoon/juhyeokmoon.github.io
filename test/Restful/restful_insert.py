import requests
import json

def web_request(method_name, url, dict_data, is_urlencoded=True) :  #web_request 함수를 만드는 과정
    method_name = method_name.upper()
    if method_name not in ('GET','POST'):
        print('다시 함수 호출 해주세요. Method가 다릅니다.')
        return 0
        
    if method_name == 'GET' :
        response = requests.get(url=url, params=dict_data)
    if method_name == 'POST' :
        if is_urlencoded is True : 
            response = requests.get(url=url, data=dict_data, headers={'Contnt=Type':'application/x-www-form-urlencoded'})
        else :
            response = requests.get(url=url, data=json.dups(dict_data), headers={'Contnt=Type':'application/json'})
    dict_meta = {'status_code':response.status_code, 'ok':response.ok, 'encoding':response.encoding, 'Content-Type':response.headers['Content-Type']}

    if 'json' in str(response.headers['Content-Type']): #json 형태인 경우
        return {**dict_meta, **response.json()}
    else : #문자열 형태인 경우
        return {**dict_meta, **{'text':response.text}}        