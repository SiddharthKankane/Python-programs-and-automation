from behave import *
from utilities.configurations import *
from utilities.resources import *
import requests
from payload import *

use_step_matcher("re")


@given("the Book details which needs to be added to library")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.url = getconfig()['API']['endpoint']
    context.query = 'select * from Books'


@when("we execute the Addbook API test")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    context.response_addbook = requests.post(context.url + ApiResources.addBook,
                                     json=buildPayloadFromDB(context.query),
                                     headers={"Contest-Type": "application/json"}, )



@then("book is successfully added")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    print(context.response_addbook.json())
    response_json = context.response_addbook.json()
    print(response_json['Msg'])

    context.bookID = response_json['ID']
    print(context.bookID)

    assert response_json['Msg'] == 'successfully added'

