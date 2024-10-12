from utilities.configurations import *


def addBookPayload():
    payload_json = {
        "name": "Learn Appium Automation with Java",
        "isbn": "bcd",
        "aisle": "227",
        "author": "John foe"
    }
    return payload_json


def buildPayloadFromDB(query):
    addpayload = dict()

    tp = getQuery(query)
    addpayload['name'] = tp[0]
    addpayload['isbn'] = tp[1]
    addpayload['aisle'] = tp[2]
    addpayload['author'] = tp[3]

    return addpayload
