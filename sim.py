import csv
import editdistance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def readFile(path):
	return open(path)

def editdistance(name1, name2):
	return editdistance.eval(name1, name2) # 0 -> good

def token_sort_ratio(name1, name2):
	return fuzz.token_sort_ratio(name1, name2)

def matching(csvfile_barcode,csvfile_items,thresold = 0):
	
	spamreader_barcode = csv.reader(csvfile_barcode, delimiter=',') # quotechar='|'
	spamreader_items = csv.reader(csvfile_items, delimiter=',')
	#barcode : 0:id,1:name,2:brand,3:barcode,4:description_eng,5:img,6:type
	#items : 0:item_id,1:name,2:brand,3:description_thai,4:img,5:type
	i = 0 
	overall = 0
	for row_barcode in spamreader_barcode:
		barcode = row_barcode[3]
		type_barcode = row_barcode[6]
		brand_barcode = row_barcode[2]
		name_barcode = row_barcode[1]
		if barcode != "9999999999999": # check only if barcode != 9999999999999
			point_max = 0
			csvfile_items.seek(0)
			overall+=1
			for row_items in spamreader_items:
				type_items = row_items[5]
				brand_items = row_items[2]
				name_items = row_items[1]
				if type_items == type_barcode and brand_items == brand_barcode:
					point = token_sort_ratio(name_items,name_barcode)
					if point >= point_max:
						name_items_max = name_items
						point_max = max(point,point_max)
			if point_max >= thresold :
				i+=1
				print ("name_barcode : %s \nname_items : %s \npoint : %d --> barcode : %s\n\n"%(name_barcode,name_items_max,point_max,barcode))
		# break
	print ("Thresold : %s %% : %d\nOverall : %d"%(thresold,i,overall))

def main():
	# same type & same brand
	csvfile_barcode = readFile('../barcode.csv')
	csvfile_items = readFile('../items.csv')

	matching(csvfile_barcode,csvfile_items,70)

if __name__ == '__main__' :
	main()