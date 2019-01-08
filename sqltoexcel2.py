import psycopg2
from sqlalchemy import create_engine
import urllib
import pandas as pd 
import xlsxwriter
import math

engine = create_engine('postgresql+psycopg2://postgres:%s@localhost:5432/postgres' % urllib.parse.quote_plus('Postgres@root'))

with engine.connect() as conn, conn.begin():
    source_table_count = pd.read_sql('select count(1) from (select count(1) from prospects_all group by company_name, country) as aaa ' , conn)['count'][0]    
no_of_loop = math.ceil(source_table_count / 100000) 

print(no_of_loop)

for i in range(0,no_of_loop):    
    limit = 100000
    print(i)
    offset  = i*100000
    if i == 0:
        offset_str = ' '
    else:
        offset_str = ' offset '   + str(offset)    
    sql = "select company_name, country, count(1) from prospects_all group by company_name, country order by count(1) desc " + " LIMIT " + str(limit) + offset_str 
    print(sql)
    data=pd.read_sql_query(sql,con=engine)
    writer = pd.ExcelWriter( 'domain_append_' + offset_str + '.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
    data.to_excel(writer,'raw_data')
    writer.save()
    print(offset, ' done')
    
    