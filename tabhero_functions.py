#!/usr/bin/env python

from bs4 import BeautifulSoup
from lxml import html
import requests

# Class that will act as an individual tab result
class TabResult():
	def __init__(self, artist, title, tab_id, rating, tab_type, url):
		self.artist = artist
		self.title = title
		self.tab_id = tab_id
		self.rating = rating
		self.type = tab_type
		self.url = url

	# Formats the tab output for printing to terminal or writing to file
	def format_tab_output(self):
		header = '{} - {}'.format(self.artist, self.title)
		spacer = '-' * (len(header))
		tab = get_tab_from_url(self.url)

		tab_output = '{}\n{}\n{}\n'.format(header, spacer, tab)
		return tab_output

	# Generates a file name for the tab as a text file
	def generate_filename(self):
		return self.artist + '-' + self.title + '-' + self.tab_id + '.txt'


def tabs_search(query):
	results = []

	ultimate_guitar = 'https://www.ultimate-guitar.com'
	endpoint = ultimate_guitar + '/search.php?search_type=title&order=&value=' + query

	page = requests.get(endpoint)
	tree = html.fromstring(page.content)

	return results

def get_tab_from_url(url):
	return None

def choose_from_results(results):
	for i in range(len(results)):
		curr_result = results[i]
		result_text = '[{}] {} - {} - {}/5 - {}'.format(i + 1, curr_result.artist, curr_result.title, curr_result.rating, curr_result.type)
		print(result_text)

	choice = 0
	while choice < 1 or choice > len(results)
		try:
			choice = int(input('\nSelect a tab number: '))
		except ValueError:
			print('Please enter a valid number!')

	return results[choice - 1]