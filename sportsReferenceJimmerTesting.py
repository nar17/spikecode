#https://www.sports-reference.com/cbb/players/jimmer-fredette-1.html
#10-09-2023 ish

import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.sports-reference.com/cbb/players/jimmer-fredette-1.html"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

#print(soup.prettify())	#this will open up the whole script in a nice way



stats = []
statsTitle = []
table = soup.find('div', attrs = {'class':'p1'})	#find the div that has what you want



for row in table.findAll('div'):	#find what div you want within the above-specified div
	quote = {}
	quote[row.strong.text] = row.css.select('p:nth-of-type(2)')
	stats.append(quote)
	statsTitle.append(row.strong.text)


#for row in table.findAll('div', attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
#	quote = {}
#	quote['theme'] = row.h5.text
#	quote['url'] = row.a['href']
#	quote['img'] = row.img['src']
#	quote['lines'] = row.img['alt'].split(" #")[0]
#	quote['author'] = row.img['alt'].split(" #")[1]
#	stats.append(quote)

filename = 'jimmerStats.csv'	#create the csv file with the data
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,statsTitle)
#	w = csv.DictWriter(f,['Games','Points','Total Rebounds','Assists'])
	w.writeheader()
	for quote in stats:
		w.writerow(quote)

print(stats)