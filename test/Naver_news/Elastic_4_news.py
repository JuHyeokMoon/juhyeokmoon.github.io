from elasticsearch import Elasticsearch
import datetime
import json

es = Elasticsearch('http://localhost:9200')

now_date = datetime.datetime.now()
index = "navernews" + str(now_date)
doc_path = "C:/Users/MoonJu/Documents/Python/juhyeokmoon.github.io-1/20200730/news_.json"

# file.open = os.listdir('20200730')

# for file_f in file.open:
#     doc_path = "new.json"

with open(doc_path, encoding='utf-8') as json_file:
    json_data = json.load(json_file)

es.index(index=index, doc_type="_doc", body=json_data)

print(es.search(index=index))