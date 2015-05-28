#
# create some csv files about top contributers etc.
#
#


import socket, sys, cx_Oracle, csv, re, os
from ourdb import ourconnect, where
import pandas as pd

conn = ourconnect()
c = conn.cursor()


def query_to_csv(sql, sql_cols, filename):
  csvfile = open("../data/static/" + filename + '.csv', 'wb') 
  csvwriter = csv.writer(csvfile)

  df = pd.read_sql(sql_cols,  con=conn)
  cols = df.columns.values
  csvwriter.writerow(cols)

  c.execute(sql)

  for row in c:
      csvwriter.writerow(row)
      
  csvfile.close()
  

print "top contributors."
sql = """
SELECT * FROM (
  SELECT * FROM (SELECT
    "CORP_30", "FIRST_NAME_40", "MID_INIT_42", "LAST_NAME_44", 
    "ADDR_1_50", "CITY_52", "STATE_54", "ZIP_56", 
    SUM("AMOUNT_70") as "SUM_AMOUNT",
    COUNT(*) as "NUMBER_OF_CONTRIBUTIONS",
    MIN("DATE1_10") AS "FIRST_DATE",
    MAX("DATE1_10") AS "LAST_DATE"
  FROM "SUN_BOE_EFSRECBS"
  WHERE "AMOUNT_70" > 0 
  AND	Transaction_Code IN ('A','B','C','D','G','P')
  GROUP BY  
    "CORP_30", "FIRST_NAME_40", "MID_INIT_42", "LAST_NAME_44", 
    "ADDR_1_50", "CITY_52", "STATE_54", "ZIP_56") X
  ORDER BY "SUM_AMOUNT" DESC) Y
"""
query_to_csv(sql + "WHERE rownum < 101", sql + "WHERE rownum < 1" , "top_contributors")

sql = """
SELECT * FROM (
  SELECT * FROM (SELECT
    "ADDR_1_50", "CITY_52", "STATE_54", "ZIP_56", 
    SUM("AMOUNT_70") as "SUM_AMOUNT",
    COUNT(*) as "NUMBER_OF_CONTRIBUTIONS",
    MIN("DATE1_10") AS "FIRST_DATE",
    MAX("DATE1_10") AS "LAST_DATE"
  FROM "SUN_BOE_EFSRECBS"
  WHERE "AMOUNT_70" > 0 
  AND	Transaction_Code IN ('A','B','C','D','G','P')
  GROUP BY  
    "ADDR_1_50", "CITY_52", "STATE_54", "ZIP_56") X
  ORDER BY "SUM_AMOUNT" DESC) Y
"""
query_to_csv(sql + "WHERE rownum < 101", sql + "WHERE rownum < 1" , "top_contributing_addresses")
conn.close()

print "zipping."
os.system('cd ../data/; zip -r static.zip static/*.csv')
print "done."
