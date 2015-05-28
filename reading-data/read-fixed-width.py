import pandas as pd
import re
from numpy import dtype


DATA_DIR = "../data/"

def read_fixed_width( filename ):
  # read header line from file
  f = open(filename)
  headers = f.next()
  f.close()

  # iterate through header line to create colspec for pandas
  beginning = 1
  i = 0
  coltypes = {}
  ww = []
  for w in re.split(r'(\w\w*\s*)', headers):
    if w == '':
      continue
    ending = beginning + len(w) 
    colname = w.rstrip()
    print "%4d-%4d (len %3d) %s" % (beginning, ending, len(w), colname)
    ww.append(len(w))

    coltypes[colname] = str
    # coltypes[colname] = dtype('O')
    i += 1
    beginning = ending 

  print 
  return pd.read_fwf(filename, widths = ww, header=0, converters=coltypes, encoding='iso-8859-1')



def print_data_dictionary(df):
  for c in df.columns:
    #print "Column %s has max length %d" % (c, df[c].map(len).max())
    print "Column %s:" % c
    for v in df[[c]].iloc[:+3].values:
      print "|%s|" % v[0]
    for v in df[[c]].iloc[-3:].values:
      print "|%s|" % v[0]
    print


for filename in ['Charities.txt', 'COMMITTEES.txt']:
  print 
  print "============= Reading File %s ==============" % filename
  print 

  df = read_fixed_width( DATA_DIR + filename )
  # print_data_dictionary( df )
  df.to_csv( DATA_DIR + filename + ".csv" )

