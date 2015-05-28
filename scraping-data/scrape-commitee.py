from cookielib import CookieJar
import os, tempfile, time, shutil, unicodewriter, urllib2
from bs4 import BeautifulSoup

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

def download_to(url, filename, post_data):
  cache_dir = "tmp/"
  # Use MD5 hash of the URL as the filename
  print "POST %s" % url
  filepath = os.path.join(cache_dir, filename)
  if os.path.exists(filepath):
    print "no, got it in cache"
    return filepath
  # Retrieve over HTTP and cache, using rename to avoid collisions
  for c in cj:
    print c
  try:
    opener.addheaders = [
        ('Referer', 'http://www.elections.ny.gov:8080/plsql_browser/recipients_county_loaddates'),
        ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:38.0) Gecko/20100101 Firefox/38.0'),
        ('Cookie', '_ga=GA1.2.1817646456.1424449509; __utma=205729607.1817646456.1424449509.1429209872.1429215101.5; __utmz=205729607.1428940616.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=205729607; __utmb=205729607.2.10.1429215101')
    ]
    data = opener.open(url, data=post_data).read()
    fd, temppath = tempfile.mkstemp()
    fp = os.fdopen(fd, 'w')
    fp.write(data)
    fp.close()
    shutil.move(temppath, filepath)
    return filepath
  except Exception as ex:
    print str(ex)
    return ""

url = "http://www.elections.ny.gov/recipientstext.html"
print "GET %s" % url
opener.open(url).read()

url = "http://www.elections.ny.gov:8080/plsql_browser/recipients_county_loaddates"
post_data = 'NAME_IN=&position_IN=ANYWHERE'
download_to(url, "list.html", post_data)

soup = BeautifulSoup(open("tmp/list.html"))

csvwriter = unicodewriter.UnicodeWriter(open('../data/committees-with-offices.csv', 'wb'))

csvwriter.writerow(["filer_name",  "office",  "district", "county", "subdivision",  "municipality", "filer_active"])

data = []
for row in soup.find_all('tr'):
  cols  = [ele.text.strip().replace("N/A", "") for ele in row.find_all('td')]
  inp = row.find('input')
  if inp is None:
    continue
  i = inp.get('value')
  if i is None:
    continue
  download_to("http://www.elections.ny.gov:8080/plsql_browser/getfiler2_loaddates", 'detail%s.html' % i, 'filerid_in=%s' % i)
  detailSoup = BeautifulSoup(open('tmp/detail%s.html' % i))
  t = detailSoup.find('td').text.strip()
  if "Status = INACTIVE" in t:
    cols.append("0")
  else:
    cols.append("1")
  # print t
  csvwriter.writerow( cols )

  
