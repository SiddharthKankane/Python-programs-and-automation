from utilities.configurations import *
from utilities.resources import *
import requests

def after_scenario(context, scenario):

    if "library" in scenario.tags:
        url=getconfig()['API']['endpoint']

        response_deleteBook = requests.post(url + ApiResources.deleteBook, json={"ID": context.bookID},
                                            headers={'Contest-Type': 'application/json'}, )

        assert response_deleteBook.status_code == requests.codes.ok
        res_json = response_deleteBook.json()

        print(res_json['msg'])
        assert res_json['msg'] == 'book is successfully deleted'