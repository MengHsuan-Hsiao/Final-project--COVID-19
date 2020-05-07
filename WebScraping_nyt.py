import requests
import bs4

# Get the url
# Sometimes might need to add a header or deal w/ cookies, in this case it's not necessary
r = requests.get('https://github.com/nytimes/covid-19-data/blob/master/us-states.csv')

# Input informatin from web into BeautifulSoup, as html format
soup = bs4.BeautifulSoup(r.text, "html.parser")

# .find_all find all the line w/ 'table' tag
stat_table = soup.find_all('table', class_ = 'js-csv-data')

# Extract the data
# Change stat_table from ResultSet to Tag
stat_table = stat_table[0]

# tr represent rows
# td represent cells
with open('us-states.csv', mode='w') as f:
	# Find every row w/ 'tr' tag
	for row in stat_table.find_all('tr'):
		count1 = 0
		count2 = 0

		# Find every cell w/ 'th' tag
		for cell in row.find_all('th'):
			# Use count to keep track of cells and help determine whtether comma is needed or not
			count1 += 1
			line = cell.text
			if count1 != 5:
				line += ','
			f.write(line)
		f.write('\n')

		# Find every cell w/ 'td' tag
		for cell in row.find_all('td'):
			# Use count to keep track of cells and help determine whtether comma is needed or not
			count2 += 1
			line = cell.text
			if count2 != 1 and count2 != 6:
				line += ','
			f.write(line)
		f.write('\n')