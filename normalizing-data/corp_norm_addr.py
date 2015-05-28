import csv
import os
import address_normalization as an


filename = 'corporations.csv'

if not os.path.isfile('not_nyc_corp.csv'):
	not_nyc_file = open('not_nyc_corp.csv', 'wb')
	not_nyc_file.close()
	
not_nyc_file = open('not_nyc_corp.csv', 'a')
not_nyc_writer = csv.DictWriter(not_nyc_file, fieldnames=['corporation_name', 'address_string'])
not_nyc_writer.writeheader()

if not os.path.isfile('nyc_corp.csv'):
	nyc_file = open('nyc_corp.csv', 'wb')
	nyc_file.close()
	
nyc_file = open('nyc_corp.csv', 'a')
nyc_writer = csv.DictWriter(nyc_file, fieldnames=['corporation_name', 'orig_addr', 'norm_addr'])
nyc_writer.writeheader()


with open(filename, 'rU') as f:
	reader = csv.reader(f)
	reader.next()
		
	for row in reader:
		orig_addr = row[4] + ' ' + row[5] + ' ' + row[6] + ' ' + row[7] + ' ' + row[8]
		
		address = row[4].split(' ')
		num = address[0]
		address.pop(0)
		st = ' '.join(address)
		zip = row[8]

		res = an.address_normalization(num,st,zip)
		
		if res:
			nyc_writer.writerow({'corporation_name': row[9], 'orig_addr':orig_addr, 
				'norm_addr': res})
		else:
			not_nyc_writer.writerow({'corporation_name': row[9], 'address_string': orig_addr})	
		
			
f.close()		
nyc_file.close()	
not_nyc_file.close()
