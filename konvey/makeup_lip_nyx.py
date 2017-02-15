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

		# for comment table
		ages = soup.findAll(attrs={"class":"right_text_skin"})
		for age in ages:
			try:
				age = int(age.contents[3].get_text().split(" ")[1])
			except Exception as e:
				age = 0
			# print("%s : %s"%(name,age))

		rates = soup.findAll(attrs={"class":"f-right new_comm_stars"})
		for j in rates :
			try:
				if j.contents[-2].get("class")[0].strip() != "" : # 5
					rate = 5 
				elif j.contents[-4].get("class")[0].strip() != "" : #4
					rate = 4
				elif j.contents[-6].get("class")[0].strip() != "" : #3
					rate = 3
				elif j.contents[-8].get("class")[0].strip() != "" : #3
					rate = 2
				elif j.contents[-10].get("class")[0].strip() != "" : #3
					rate = 1
				else :
					rate = 0
			except Exception as e:
				rate = "-1"
			
			print("%s : %s"%(name,rate))
		
		# print("%s : %s : %s : %s"%(name,brand,description,type_items))
		# comments = soup.find(attrs={"id":"commentlist"}).contents
		# for j in comments :
		
		# break
	
	# file_name.close()


if __name__ == "__main__":
	main()
	