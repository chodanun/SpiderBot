#!/usr/bin/python
#-*-coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def main():
	file_items = open("csv/powder/loreal.csv", "w")
	file_comment = open("csv/powder/loreal-comment.csv", "w")
	item_id = 290
	comment_id = 2209
	brand = "L'Oreal"
	type_items = "powder"
	url = "http://loreal.konvy.com/search?brandDetailId=78&pid=114&cateId=2504"

	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	links = soup.findAll(attrs={"class":"all_img"}) 
	
	for i in links :
		name = i.contents[1].get("title").strip().replace("'"," ").replace('"',' ').replace(","," ")
		url = i.get("href")
		page = requests.get(url)
		soup = BeautifulSoup(page.text, "html.parser")
		description = soup.find(attrs={"class":"pro_name"}).get_text().strip()
		description = description[len(i.contents[1].get("title").strip()):].strip().replace("'"," ").replace('"',' ').replace(","," ").replace("\n"," ")
		img = i.contents[1].get('src')
		file_items.write("%d,%s,%s,%s,%s,%s\n"%(item_id,name,brand,description,img,type_items))
		# print ("%s,%s,%s,%s,%s\n"%(item_id,name,brand,description,type_items))
		while True : # comment table (more than 1 page)
			comments = soup.findAll(attrs={"class":"comm_right_con"})
			for k in comments :
				try: # rate
					if k.previous_sibling.previous_sibling.contents[9].contents[-2].get("class")[0].strip() != "" : # 5
						rate = 5
					elif k.previous_sibling.previous_sibling.contents[9].contents[-4].get("class")[0].strip() != "" : # 4
						rate = 4
					elif k.previous_sibling.previous_sibling.contents[9].contents[-6].get("class")[0].strip() != "" : # 3
						rate = 3
					elif k.previous_sibling.previous_sibling.contents[9].contents[-8].get("class")[0].strip() != "" : # 2
						rate = 2
					elif k.previous_sibling.previous_sibling.contents[9].contents[-10].get("class")[0].strip() != "" : # 1
						rate = 1
					else :
						rate = 0
				except Exception as e:
					rate = -1
				try: # age 
					age = int(k.previous_sibling.previous_sibling.contents[7].contents[-2].get_text().split(" ")[1])
				except Exception as e:
					age = -1
				
				try: # comment title 
					if k.contents[1].get('class')[0] == "right_text_tit" :
						comment_title = k.contents[1].get_text().strip().replace("'"," ").replace('"',' ').replace(","," ").replace("\n"," ")
					else :
						comment_title = ""	
				except Exception as e:
					comment_title = ""

				try: # comment com
					if k.contents[3].get('class')[0] == "right_text_con" : # comment
						comment_com = k.contents[3].get_text().strip().replace("'"," ").replace("\""," ").replace(","," ").replace("\n"," ").replace('\r', '')
					elif k.contents[1].get('class')[0] == "right_text_con" :
						comment_com = k.contents[1].get_text().strip().replace("'"," ").replace("\""," ").replace(","," ").replace("\n"," ").replace('\r', '')
					else :
						comment_com = ""
				except Exception as e:
					comment_com = ""
				
				file_comment.write("%d,%d,%s,%s,%s,%s\n"%(comment_id,item_id,comment_title,comment_com,age,rate))
				print ("%d : %d : %s => %s (%d-%d)"%(item_id,comment_id,comment_title,comment_com,age,rate))

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
	
	file_items.close()
	file_comment.close()


if __name__ == "__main__":
	main()
	