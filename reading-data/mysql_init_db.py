'''
You must run this script to set up the environment before running the actual
dedulication script!
adapted from example from dedupe creators. Link to doc here:
http://open-city.github.io/dedupe/doc/mysql_init_db.html
'''
import os
import warnings
import MySQLdb

## you need to create a 'contributions' database before running this script if you don't already have one.
## you can do that by just adding this on line 20: c.execute("CREATE DATABASE contributions") AND
## make sure that you delete the db='contributions' from the conn=MySQLdb statement

warnings.filterwarnings('ignore', category=MySQLdb.Warning)

contributions_txt_file = 'contributions.csv'

conn = MySQLdb.connect(host='localhost', user='root', passwd='', read_default_file = 'my.cnf', 
                       local_infile = 1,
                       db='contributions')
c = conn.cursor()

print 'importing raw data from csv...'
c.execute("DROP TABLE IF EXISTS raw_table")
c.execute("DROP TABLE IF EXISTS donors")
c.execute("DROP TABLE IF EXISTS recipients")
c.execute("DROP TABLE IF EXISTS contributions")


c.execute("CREATE TABLE raw_table "
          "(CORP VARCHAR(70), LAST_NAME VARCHAR(70), FIRST_NAME VARCHAR(35), "
          " ADDR VARCHAR(35), CITY VARCHAR(20), "
          " STATE VARCHAR(15), ZIP VARCHAR(11), "
          " AMOUNT VARCHAR(23), DATE1 VARCHAR(23), "
          " FILER_ID VARCHAR(20), "
          " CHECK_NO VARCHAR(10),"
          " RECIPIENT VARCHAR(70), BOEE_ID VARCHAR(10)) "
          "CHARACTER SET utf8 COLLATE utf8_unicode_ci")
conn.commit()

c.execute("LOAD DATA LOCAL INFILE %s INTO TABLE raw_table "
          "FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\r\n' " 
          "IGNORE 1 LINES "
          "(CORP, LAST_NAME, FIRST_NAME, ADDR, CITY, STATE, ZIP, AMOUNT, FILER_ID, CHECK_NO, RECIPIENT, BOEE_ID)",
          (contributions_txt_file,))
conn.commit()

print 'creating indexes on raw table'
c.execute("CREATE INDEX raw_table_info ON raw_table "
          "(CORP, FIRST_NAME, LAST_NAME, ADDR, CITY, STATE, ZIP, AMOUNT, FILER_ID,"
          " CHECK_NO, RECIPIENT, BOEE_ID)")
conn.commit()

print 'nullifying empty strings in donors'
c.execute("UPDATE raw_table "
          "SET "
          "FIRST_NAME = CASE FIRST_NAME WHEN '' THEN NULL ELSE FIRST_NAME END, "
          "LAST_NAME = CASE LAST_NAME WHEN '' THEN NULL ELSE LAST_NAME END, "
          "ADDR = CASE ADDR WHEN '' THEN NULL ELSE ADDR END, "
          "CITY = CASE CITY WHEN '' THEN NULL ELSE CITY END, "
          "STATE = CASE STATE WHEN '' THEN NULL ELSE STATE END, "
          "ZIP = CASE ZIP WHEN '' THEN NULL ELSE ZIP END, "
          "AMOUNT = CASE AMOUNT WHEN '' THEN NULL ELSE AMOUNT END, " 
          "FILER_ID = CASE FILER_ID WHEN '' THEN NULL ELSE FILER_ID END, " 
          "CHECK_NO = CASE CHECK_NO WHEN '' THEN NULL ELSE CHECK_NO END, "
          "RECIPIENT = CASE RECIPIENT WHEN '' THEN NULL ELSE RECIPIENT END, "
          "BOEE_ID = CASE BOEE_ID WHEN '' THEN NULL ELSE BOEE_ID END")

conn.commit()

c.close()
conn.close()
print 'done'