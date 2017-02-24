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

def matching(csvfile_barcode,csvfile_items):
	point_max = 0
	spamreader_barcode = csv.reader(csvfile_barcode, delimiter=',') # quotechar='|'
	spamreader_items = csv.reader(csvfile_items, delimiter=',')
	#barcode : 0,1:name,2:brand,3:barcode,4:description_eng,5:img,6:type
	for row_items in spamreader_items:
		name_items = row_items[1]
		for row_barcode in spamreader_barcode:
			name_barcode = row_barcode[1]
			point = token_sort_ratio(name_items,name_barcode)
			if point > point_max :
				barcode = row_barcode[3]
				print ("name_items : %s \nname_barcode : %s \npoint : %d --> barcode : %s\n\n"%(name_items,name_barcode,point,barcode))
				point_max = max(point,point_max)
		break

def main():
	# same type & same brand
	csvfile_barcode = readFile('../barcode.csv')
	csvfile_items = readFile('../items.csv')

	matching(csvfile_barcode,csvfile_items)

if __name__ == '__main__' :
	main()