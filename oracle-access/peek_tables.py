import socket, sys, cx_Oracle
import pandas as pd

hostname = socket.gethostname()

remote = False
if len(sys.argv) > 1 and sys.argv[1] == '--remote':
  remote = True

if hostname == 'compute.cusp.nyu.edu' and not remote:
  print "This script is accessing the local database on  %s" % hostname
  conn_str = u'[DB_NYOGDATA]/@oracle'
  conn = cx_Oracle.connect(conn_str)
elif hostname == 'oagcapstone' and not remote:
  print "This script is accessing the local database on  %s" % hostname
  conn_str = u'oag/oag123QWE@localhost/orcl'
  conn = cx_Oracle.connect(conn_str)
else:
  print "This script is accessing the database on oagcapstone remotely!"
  ip = '23.96.115.130'
  port = 1521
  SID = 'orcl'
  dsn_tns = cx_Oracle.makedsn(ip, port, SID)
  conn = cx_Oracle.connect('oag', 'oag123QWE', dsn_tns)

c = conn.cursor()
c.execute(u"SELECT * FROM SUN_BOE_EFSRECBS") 


i=0
print "These are some rows of Table SUN_BOE_EFSRECBS"
for row in c:
    i+= 1
    print row
    if i > 3:
       break


conn.close()
