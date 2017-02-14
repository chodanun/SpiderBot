#!/usr/bin/python
#-*-coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def main():
	# file_name = open("csv/lip/nyx.csv", "w")

	url = "http://nyx.konvy.com/search?brandDetailId=62&pid=114&cateId=1100"
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	links = soup.findAll(attrs={"class":"all_img"}) 
	for i in links :
		name = i.contents[1].get("title").strip()
		brand = "NYX"
		type_items = "lipstick"
		url = i.get("href")
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		description = soup.find(attrs={"class":"pro_name"}).get_text().strip()
		description = description[len(name):].strip()
		
		print("%s : %s : %s : %s"%(name,brand,description,type_items))
		break
	
	# file_name.close()


if __name__ == "__main__":
	main()
	