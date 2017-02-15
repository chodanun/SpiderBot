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
	comment_id = 1
	item_id = 1
	for i in links :
		name = i.contents[1].get("title").strip()
		brand = "NYX"
		type_items = "lipstick"
		url = i.get("href")
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		description = soup.find(attrs={"class":"pro_name"}).get_text().strip()
		description = description[len(name):].strip()

		while True : # comment table (more than 1 page)
			ages = soup.findAll(attrs={"class":"right_text_skin"})
			for age in ages:
				try:
					age = int(age.contents[3].get_text().split(" ")[1])
				except Exception as e:
					age = 0

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

			comments = soup.findAll(attrs={"class":"comm_right_con"})
			for k in comments :
				try:
					if k.contents[1].get('class')[0] == "right_text_tit" :
						comment_title = k.contents[1].get_text().strip()
					else :
						comment_title = ""	
				except Exception as e:
					comment_title = ""

				try:
					if k.contents[3].get('class')[0] == "right_text_con" : # comment
						comment_com = k.contents[3].get_text().strip()
					elif k.contents[1].get('class')[0] == "right_text_con" :
						comment_com = k.contents[1].get_text().strip()
				except Exception as e:
					comment_com = ""
				
				print ("%s : %s : %d . %s => %s"%(item_id,name,comment_id,comment_title,comment_com)) 
				comment_id += 1 # increase comment id

			next_page = soup.find(attrs={"class":"paginator"})	
			try:
				if next_page.contents[-2].contents[0].get_text().strip() == "Next" :
					url = "http://www.konvy.com/"+next_page.contents[-2].contents[0].get('href')
					page = requests.get(url)
					soup = BeautifulSoup(page.text, "html.parser")
				else :
					break
			except Exception as e:
				break
			
		item_id += 1
		# break
	
	# file_name.close()


if __name__ == "__main__":
	main()
	