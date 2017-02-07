#!/usr/bin/python
#-*-coding: utf-8 -*-

import requests
import queue
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os

def main():
	url = "http://www.fishpond.co.nz/Beauty/NARS-Satin-Lip-Pencil-Rikugien/9999962910175"
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	img = soup.find("img",attrs={"class":"photo"}).get("src")
	print ("%s"%(img))


if __name__ == "__main__":
	main()