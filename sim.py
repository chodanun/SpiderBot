import csv
import editdistance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def readFile(path):
	return open(path,'r')

def editdistance(name1, name2):
	return editdistance.eval(name1, name2) # 0 -> good

def token_sort_ratio(name1, name2):
	return fuzz.token_sort_ratio(name1, name2)

def sim(csvfile_barcode,csvfile_konvey):
	point_max = 0
	spamreader_barcode = csv.reader(csvfile_barcode, delimiter=',') # quotechar='|'
	spamreader_konvey = csv.reader(csvfile_konvey, delimiter=',')
	#barcode : 0,1:name,2:brand,3:barcode,4:description_eng,5:img,6:type
	for row_konvey in spamreader_konvey:
		name_konvey = row_konvey[1]
		for row_barcode in spamreader_barcode:
			name_barcode = row_barcode[1]
			point = token_sort_ratio(name_konvey,name_barcode)
			if point > point_max :
				
				print ("name_konvey : %s \nname_barcode : %s \npoint : %d\n\n"%(name_konvey,name_barcode,point))
				point_max = max(point,point_max)
		break

def main():
	# same type & same brand
	csvfile_barcode = readFile('barcode/csv/barcode_database/lips-nyx.csv')
	csvfile_konvey = readFile('konvey/csv/lip/nyx.csv')

	sim(csvfile_barcode,csvfile_konvey)

if __name__ == '__main__' :
	main()