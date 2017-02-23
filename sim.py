import csv

with open('barcode/csv/barcode_database/lips-nyx.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print (', ')