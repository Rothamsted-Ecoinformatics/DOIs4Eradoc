'''
Created on 2 Nov 2017

@author: ostlerr
'''

import pymysql
import configparser
from datacite import DataCiteMDSClient

def getConfig():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def getDbConnection():
    config = getConfig()
    # ERA database
    erahost = config['ERA_DATABASE']['host']
    erauser = config['ERA_DATABASE']['user']
    erapwd= config['ERA_DATABASE']['password']
    eradb = config['ERA_DATABASE']['db']
    eraCon = pymysql.connect(host=erahost,user=erauser,password=erapwd,db=eradb)
    
    return eraCon

def getDataCiteClient():
    config = getConfig()
    client = DataCiteMDSClient(
        username=config['DATACITE']['user'],
        password=config['DATACITE']['password'],
        prefix=config['DATACITE']['prefix'],
        test_mode=False
    )
    
    return client
    