#!/usr/bin/env python

import sys
import argparse
from tabhero_functions import *

parser = argparse.ArgumentParser(description="View and download guitar tabs from ultimate-guitar.com")
parser.add_argument('query', metavar='query', nargs='+',
					help='Query song or artist to search on ultimate-guitar.com')
parser.add_argument('-a', '--artists',
					action='store_true', default=False,
					help='Query for an artist rather than individual song names')
#maybe remove this in future
parser.add_argument('-p', '--print',
					action='store_true', default=False,
					help='Print the resulting tab to console instead of downloading directly')

if len(sys.argv) < 2:
	parser.print_help()
	sys.exit(1)

args = parser.parse_args()

