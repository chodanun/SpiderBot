import csv
import editdistance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def readFile(path):
	return open(path)

def writeFile(path):
	return open(path,'w')

def editdistance(name1, name2):
	return editdistance.eval(name1, name2) # 0 -> good

def token_sort_ratio(name1, name2):
	return fuzz.token_sort_ratio(name1, name2)

def matching(csvfile_barcode,csvfile_items,thresold = 0):
	spamreader_barcode = csv.reader(csvfile_barcode, delimiter=',') # quotechar='|'
	spamreader_items = csv.reader(csvfile_items, delimiter=',')
	#barcode : 0:id,1:name,2:brand,3:barcode,4:description_eng,5:img,6:type
	#items : 0:item_id,1:name,2:brand,3:description_thai,4:img,5:type
	f = writeFile("../match_point.csv")
	for row_barcode in spamreader_barcode:
		barcode = row_barcode[3]
		barcode_id = row_barcode[0]
		type_barcode = row_barcode[6]
		brand_barcode = row_barcode[2]
		name_barcode = row_barcode[1]
		if barcode != "9999999999999": # check only if barcode != 9999999999999
			csvfile_items.seek(0)
			for row_items in spamreader_items:
				type_items = row_items[5]
				brand_items = row_items[2]
				name_items = row_items[1]
				id_items = row_items[0]
				if type_items == type_barcode and brand_items == brand_barcode:
					point = token_sort_ratio(name_items,name_barcode)
					if point >= thresold:
						print (",%s,%s,%s\n"%(id_items,point,barcode_id))
						f.write(",%s,%s,%s\n"%(id_items,point,barcode_id))
	f.close()

def main():
	# same type & same brand
	csvfile_barcode = readFile('../barcode.csv')
	csvfile_items = readFile('../items.csv')

	matching(csvfile_barcode,csvfile_items,70)

if __name__ == '__main__' :
	main()