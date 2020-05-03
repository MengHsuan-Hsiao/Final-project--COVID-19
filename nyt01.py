import requests
import bs4

r = requests.get('https://github.com/nytimes/covid-19-data/blob/master/us-states.csv')
# print(r.text)

# with open('covid.csv', mode='w') as f:
# 	f.write(r.text)


# Input informatin from web into BeautifulSoup, as html format
soup = bs4.BeautifulSoup(r.text, "html.parser")
# print(soup)
# print(soup.title.string)

stat_table = soup.find_all('table', class_ = 'js-csv-data')
print(len(stat_table))
print(type(stat_table))
# Extract the data
# Change stat_table from ResultSet to Tag
stat_table = stat_table[0]
print(type(stat_table))

# tr represent rows
# td represent cells
with open('test.csv', mode='w') as f:
	for row in stat_table.find_all('tr'):
		for cell in row.find_all('td'):
			f.write(cell.text)

# for td in soup.find_all('td', class_='blob-num'):
# 	# ths = soup.find_all('th')
# 	# print(ths[0].text)
# 	# print(ths[1].text)
# 	# print(ths[2].text)
# 	# print(ths[3].text)
# 	# print(ths[4].text)
# 	tds = soup.find_all('td')
# 	print(tds[2].text)
# 	print(tds[3].text)
# 	print(tds[4].text)
# 	print(tds[5].text)
# 	print(tds[6].text)

# layer = soup.find_all('table', class_='js-csv-data')
# print(layer)

# test = soup.find_all('td', class_='blob-num')
# link_tag = soup.find_next_siblings('td')
# print(test)

# test2 = soup.find_all('td')
# print(str(test2))
# print(str(test2.string))
# for i in test2:
# 	print(i.string)


# test3 = soup.select('td [class_='blob-num']')
# print(test3)


# with open('test.csv', mode='w') as f:
# 	# print(str(test))
# 	print(str(link_tag))
# 	# f.write(str(test))
# 	f.write(str(link_tag))