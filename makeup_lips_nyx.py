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
	max_page = 16
	# file_name = open("mouse_name_barcode.txt", "w")

	while number_of_page <= max_page:
		url = "http://www.fishpond.co.nz/c/Beauty/Makeup/Lips/p/NYX?page="+str(number_of_page)
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		links = soup.findAll(attrs={"class":"blue_link fn url"}) 
		for i in links :
			name = i.get_text().replace("'", " ")
			url_product = i.get('href')
			page_product = requests.get(url_product)
			soup = BeautifulSoup(page_product.text, "html.parser")
			brand = soup.find(id="product_author").contents[1].get_text()
			
			print ("%s : %s"%(name,brand))
			# file_name.write("%s\n"%i.get_text())
		print ("%d is downloaded"%(number_of_page))
		number_of_page+=1
		break


if __name__ == "__main__":
	main()
	