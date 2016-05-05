#!/usr/bin/env python

import sys
from bs4 import BeautifulSoup
import lxml
import requests

# Types that won't be considered
rejected_types = ['tab pro', 'video lesson', 'guitar pro', 'power tab']

# Class that will act as an individual tab result
class TabResult():
	def __init__(self, artist, title, tab_id, rating, tab_type, url):
		self.artist = artist
		self.title = title
		self.tab_id = tab_id
		self.rating = rating
		self.tab_type = tab_type
		self.url = url

	# Formats the tab output for printing to terminal or writing to file
	def format_tab_output(self):
		header = '{} - {}'.format(self.artist, self.title).encode('utf-8')
		spacer = ('-' * (len(header))).encode('utf-8')
		tab = get_tab_from_url(self.url).encode('utf-8')

		tab_output = '{}\n{}\n{}\n'.format(header, spacer, tab)
		return tab_output

	# Generates a file name for the tab as a text file
	def generate_filename(self):
		return '{} - {} -.txt'.format(self.artist, self.title, self.tab_id)
		# return self.artist + '-' + self.title + '-' + str(self.tab_id) + '.txt'


# Major function that performs the actual search and returns the results it found
def tabs_search(query):
	results = []

	ultimate_guitar = 'https://www.ultimate-guitar.com'
	endpoint = ultimate_guitar + '/search.php?search_type=title&order=&value=' + query

	page = requests.get(endpoint)

	if page.status_code == 200:
		tabs_soup = BeautifulSoup(page.text, 'lxml')
		results_table = tabs_soup.find('table', class_="tresults")

		rows = results_table.find_all('tr') # All the results rows in the table
		# Now comes the fun part.
		# Only consume and care about results that are chords, tab, bass, ukelele chords, drums.
		# Do NOT keep tabs pro, video lesson, or guitar pro types.
		total_count = 0
		curr_artist = None
		for row in rows:
			artist = row.find('a', class_="song search_art")
			if artist:
				curr_artist = artist.text

			tab_type = row.find('strong')
			if tab_type and tab_type.text not in rejected_types:
				tab_type = tab_type.text
				total_count += 1
			else:
				continue

			title = row.find('a', class_="song result-link").text.encode('utf-8')
			tab_id = total_count
			rating = len(row.find_all('span', class_="icon-rating-sm icon-rating-sm__active"))
			url = row.find('a', class_="song result-link")['href']

			results.append(TabResult(curr_artist, title, tab_id, rating, tab_type, url))


	elif 500 > page.status_code >= 400:
		print("[error] Something went wrong with the request that shouldn't have")
		sys.exit(1)


	elif page.status_code >= 500:
		print('[error] Looks like ultimate-guitar is having trouble fulfilling the request.')
		print('[error] Try again in a bit or check if the site is up right now.')
		sys.exit(1)

	return results

def get_tab_from_url(url):
	page = requests.get(url)
	tab_soup = BeautifulSoup(page.text, 'lxml')
	tab_content = tab_soup.find('div', class_="tb_ct").text
	return tab_content

def choose_from_results(results):
	for i in range(len(results)):
		curr_result = results[i]
		result_text = '[{}] {} - {} - {}/5 - {}'.format(i + 1, curr_result.artist, curr_result.title, curr_result.rating, curr_result.tab_type)
		print(result_text)

	choice = 0
	while choice < 1 or choice > len(results):
		try:
			choice = int(input('\nSelect a tab number: '))
		except ValueError:
			print('[error] Please enter a valid number!')

	return results[choice - 1]