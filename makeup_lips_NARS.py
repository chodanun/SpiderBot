#!/usr/bin/python
#-*-coding: utf-8 -*-

import requests
import queue
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os

def main():
	number_of_page = 1
	max_page = 5
	file_name = open("csv/lips/makeup_lips_NARS.csv", "w")

	while number_of_page <= max_page:
		url = "http://www.fishpond.co.nz/Beauty/Makeup/Lips/?brand=NARS&cName=Beauty%2FMakeup%2FLips&page="+str(number_of_page)
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		links = soup.findAll(attrs={"class":"blue_link fn url"}) 
		for i in links :
			name = i.get_text().replace("'", " ").replace("\""," ").replace("," ," ")
			url_product = i.get('href')
			page_product = requests.get(url_product)
			soup = BeautifulSoup(page_product.text, "html.parser")
			img = soup.find("img",attrs={"class":"photo"}).get("src")
			brand = "NARS"
			# brand = soup.find(id="product_author").contents[1].get_text().replace("'"," ").replace("\""," ").replace("," ," ")
			barcode_available = soup.find(attrs={"class":"product_info_text","width":"100%"}).contents[0].contents[2]
			barcode = barcode_available.get("itemprop") == "gtin13" 
			if barcode : 
				barcode = barcode_available.get_text().strip()
			else :
				barcode = "9999999999999"
			try:
				description = soup.find(attrs={"class":"description"}).contents[1].get_text().strip()
				description = description.replace("'"," ").replace("\""," ").replace("," ," ")
			except Exception as e:
				description = "no"
			
			print ("%s,%s,%s,%s,%s"%(name,brand,barcode,description,img))
			file_name.write("%s,%s,%s,%s,%s\n"%(name,brand,barcode,description,img))
		print ("%d is downloaded"%(number_of_page))
		number_of_page+=1
	file_name.close()


if __name__ == "__main__":
	main()