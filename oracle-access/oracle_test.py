from ourdb import ourconnect
import pandas as pd

conn = ourconnect()
c = conn.cursor()
c.execute(u"SELECT TABLE_NAME FROM USER_TABLES WHERE NOT(table_name LIKE '%DR%')") 

tables = []

d = conn.cursor()
for row in c:
  table = row[0]
  print "==========================================="
  print "Table %s" % table
  print "-------------------------------------------"
  e = conn.cursor()
  e.execute(u"SELECT column_name,data_type FROM all_tab_cols WHERE table_name = '%s'" % table )
  i=0
  print "%2d) %30s  %10s  %s" % (0, "Column Name", "Type", "Example Data")
  for row in e:
    i += 1
    col = row[0]
    f = conn.cursor()
    f.execute(u"SELECT %s FROM %s WHERE rownum < 2" % ( col, table ))
    data = f.next()[0]
    f.close()    
    print "%2d) %30s  %10s  %s" % (i, row[0], row[1], data)
  e.close()    
  print "-------------------------------------------"
  sql = "SELECT COUNT(*) FROM %s" % table
  d.execute(sql)
  for row in d:
    print "%d rows" % row[0]


conn.close()
