# coding :utf-8 

from QUANTAXIS.QAFetch import QATushare
import tushare as ts
from QUANTAXIS.QAUtil import QA_util_date_stamp,QA_util_time_stamp
from QUANTAXIS.QAUtil import QA_Setting
import datetime,json
import re
import time
import pymongo

def QA_save_stock_day_all():
    df= ts.get_stock_basics()
    for i in df.index:  
        print(i)    
        try:
            data=ts.get_k_data(i)
            data_json=json.loads(data.to_json(orient='records'))
            coll=pymongo.MongoClient().quantaxis.stock_day
            coll.insert_many(data_json)
        except:
            print('none data')

def QA_SU_save_stock_list():
    data=QATushare.QA_fetch_get_stock_list()
    date=str(datetime.date.today())
    date_stamp=QA_util_date_stamp(date)
    coll=pymongo.MongoClient().quantaxis.stock_list
    coll.insert({'date':date,'date_stamp':date_stamp,'stock':{'code':data}})
