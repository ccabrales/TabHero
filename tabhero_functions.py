#!/usr/bin/env python

from bs4 import BeautifulSoup

# Class that will act as an individual tab result
class TabResult():
	def __init__(self, artist, title, tab_id, rating, url):
		self.artist = artist
		self.title = title
		self.tab_id = tab_id
		self.rating = rating
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
	return results

def choose_from_resuls(results):
	print(results)