#!/usr/bin/env python

import sys
import os
import argparse
from tabhero_functions import *

parser = argparse.ArgumentParser(description="View and download guitar tabs from ultimate-guitar.com to the current directory")
parser.add_argument('query', metavar='query', nargs='+',
					help='Query song or artist to search on ultimate-guitar.com')
parser.add_argument('-p', '--print_tab',
					action='store_true', default=False,
					help='Print the resulting tab to console instead of downloading directly.')
parser.add_argument('-s', '--select',
					action='store_true', default=False,
					help='Show top results found without automatic selection and choose among them.')
parser.add_argument('-o', '--output-dir',
					nargs='?', default=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tabs'),
					help='Specify the output directory for saving tabs. Defaults to tabs')

if len(sys.argv) < 2:
	parser.print_help()
	sys.exit(1)

args = parser.parse_args()

# Performs the entire search and selection. Ends by writing to file or stdout.
def perform_search(raw_query, select, print_tab, output_dir):
	query = '+'.join(raw_query)
	search_results = tabs_search(query)

	# Allow the user to choose from the results, or pick the first result by default
	if select is True:
		tab_choice = choose_from_results(search_results)
	else:
		tab_choice = search_results[0]

	print('Downloading tab...\n')
	formatted_tab = tab_choice.format_tab_output().strip()

	# Print the tab to command line or download by default
	if print_tab is True:
		print('\n' + formatted_tab)
	else:
		filename = os.path.join(output_dir, tab_choice.generate_filename())
		dirname = os.path.dirname(filename)

		# Referenced http://stackoverflow.com/a/12517490
		if dirname != '' and not os.path.exists(dirname):
			try:
				os.makedirs(dirname)
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise

		print('Writing to file...')
		with open(filename, 'w') as f:
			try:
				f.write(bytes(formatted_tab, 'UTF-8'))
			except TypeError:
				f.write(bytes(formatted_tab))



if __name__ == '__main__':
	perform_search(args.query, args.select, args.print_tab, args.output_dir)
