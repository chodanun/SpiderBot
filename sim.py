import csv
import editdistance

def readFile(path):
	return open(path,'r')

def editdistanceScore(name1, name2):
	return editdistance.eval(name1, name2)

def sim(csvfile_barcode,csvfile_konvey):
	spamreader_barcode = csv.reader(csvfile_barcode, delimiter=',') # quotechar='|'
	spamreader_konvey = csv.reader(csvfile_konvey, delimiter=',') # quotechar='|'
	#barcode : 0,1:name,2:brand,3:barcode,4:description_eng,5:img,6:type
	for row_konvey in spamreader_konvey:
		name_konvey = row_konvey[1]
		for row_barcode in spamreader_barcode:
			name_barcode = row_barcode[1]
			point = editdistanceScore(name_konvey,name_barcode)
			print (point)
		break

def main():
	# same type & same brand
	csvfile_barcode = readFile('barcode/csv/barcode_database/lips-nyx.csv')
	csvfile_konvey = readFile('konvey/csv/lip/nyx.csv')

	# sim(csvfile_barcode,csvfile_konvey)
	print (editdistance.eval('banana', 'banana'))
	print (editdistance.eval('banana', 'asd'))

if __name__ == '__main__' :
	main()