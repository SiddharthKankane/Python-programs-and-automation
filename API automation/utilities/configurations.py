import configparser
import mysql.connector


def getconfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config


connect_config = {
    'host': getconfig()['SQL']['host'],
    'database': getconfig()['SQL']['database'],
    'user': getconfig()['SQL']['user'],
    'password': getconfig()['SQL']['password'],
}


def getPassword():
    return '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'


def getConnection():
    try:
        con = mysql.connector.connect(**connect_config)
        assert con.is_connected() == True
        return con
    except Error as e:
        print(e)


def getQuery(query):
    con = getConnection()
    cursor = con.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    return row
