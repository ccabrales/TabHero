#!/usr/bin/env python

import sys
import argparse
from tabhero_functions import *

parser = argparse.ArgumentParser(description="View and download guitar tabs from ultimate-guitar.com to the current directory")
parser.add_argument('query', metavar='query', nargs='+',
					help='Query song or artist to search on ultimate-guitar.com')
#maybe remove this in future
parser.add_argument('-p', '--print_tab',
					action='store_true', default=False,
					help='Print the resulting tab to console instead of downloading directly.')
parser.add_argument('-s', '--select',
					action='store_true', default=False,
					help='Show top results found without automatic selection and choose among them.')

if len(sys.argv) < 2:
	parser.print_help()
	sys.exit(1)

args = parser.parse_args()


if __name__ == '__main__':
	query = ' '.join(args.query)
	search_results = tabs_search(query)

	# Allow the user to choose from the results, or pick the first result by default
	if args.select is True:
		tab_choice = choose_from_results(search_results)
	else:
		tab_choice = search_results[0]

	formatted_tab = tab_choice.format_tab_output()

	# Print the tab to command line or download by default
	if args.print_tab is True:
		print ('\n' + formatted_tab,)
	else:
		filename = tab_choice.generate_filename()
		with open(filename, 'w') as f:
			try:
				f.write(bytes(formatted_tab, 'UTF-8'))
			except TypeError:
				f.write(bytes(formatted_tab))
