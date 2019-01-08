import psycopg2
from sqlalchemy import create_engine
import urllib
import pandas as pd 
import xlsxwriter
from datetime import date
from datetime import timedelta  
import random as rn
import math


start_number = 2500000
end_number = 4957082
start_day = -10
ran_start_number = 35000
ran_end_number = 45000
while end_number > start_number:
    date1 = date.today() + timedelta(days=start_day)  
    a = rn.randint(ran_start_number, ran_end_number)
    fk_start = start_number
    fk_end =start_number +  a
    start_day = start_day + 1
    #print (a,start_day,fk_start, fk_end, a)
    start_number = fk_end
    sql_update =  ("update prospects_all_fke set createddate ='" + str(date1) + "' where fk_id between  " +  str(fk_start) + " and " + str(fk_end )  + ";"  )
    print(sql_update)






"""
conn = psycopg2.connect(database="postgres",user="postgres",password='Postgres@root',host='173.212.222.223')
cursor = conn.cursor()
cursor.execute("UPDATE %s SET status=1 WHERE id = %d" % (url_table,id))
conn.commit()
cursor.close()
conn.close()
"""