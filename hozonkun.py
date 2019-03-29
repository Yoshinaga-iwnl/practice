import requests
from bs4 import BeautifulSoup
import os

url = "https://www.pixiogaming.jp/"

soup = BeautifulSoup(requests.get(url).content,'lxml')

png_urls = []
jpg_urls = []

os.mkdir("testimg")
os.mkdir("testimg/jpg")
os.mkdir("testimg/png")

for link in soup.findAll("img", attrs = {"src" : True}):

	if ".png" in link["src"]:
		png_urls.append(link["src"])

	elif ".jpg" in link["src"]:
		jpg_urls.append(link["src"])

for link in soup.findAll("img", attrs = {"srcset" : True}):
    if ".png" in link["srcset"]:
    	for png_url in link["srcset"].split(","):
    		png_urls.append(png_url)

    elif ".jpg" in link["srcset"]:
    	for jpg_url in link["srcset"].split(","):
    		jpg_urls.append(jpg_url)

count = 0
for get_png in png_urls:
	png_data = requests.get(get_png)
	with open("./testimg/png/"+str(count) + ".png", mode='w') as f:
		f.write(png_data.content)
	count = count + 1

count = 0
for get_jpg in jpg_urls:
	jpg_data = requests.get(get_jpg)
	with open("./testimg/jpg/"+str(count) + ".jpg", mode='w') as f:
		f.write(jpg_data.content)
	print get_jpg
	count = count + 1