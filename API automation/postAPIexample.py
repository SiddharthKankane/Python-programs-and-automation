import requests
from payload import *
import json
import configparser
from utilities.configurations import *
from utilities.resources import *

url = getconfig()['API']['endpoint']

query = 'select * from Books'
response_addbook = requests.post(url + ApiResources.addBook,
                                 json=buildPayloadFromDB(query),
                                 headers={"Contest-Type": "application/json"}, )

print(response_addbook.json())
response_json = response_addbook.json()

bookID = response_json['ID']
print(bookID)

response_deleteBook = requests.post(url + ApiResources.deleteBook, json={"ID": bookID},
                                    headers={'Contest-Type': 'application/json'}, )

assert response_deleteBook.status_code == requests.codes.ok
res_json = response_deleteBook.json()

print(res_json['msg'])
assert res_json['msg'] == 'book is successfully deleted'

if __name__ == '__main__':
    pass
