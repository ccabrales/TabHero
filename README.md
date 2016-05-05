# TabHero
Python command line tool to search and download guitar tabs from ultimate-guitar.com

	usage: tabhero.py [-h] [-p] [-s] [-o [OUTPUT_DIR]] query [query ...]

	View and download guitar tabs from ultimate-guitar.com to the current
	directory

	positional arguments:
	  query                 Query song or artist to search on ultimate-guitar.com

	optional arguments:
	  -h, --help            show this help message and exit
	  -p, --print_tab       Print the resulting tab to console instead of
	                        downloading directly.
	  -s, --select          Show top results found without automatic selection and
	                        choose among them.
	  -o [OUTPUT_DIR], --output-dir [OUTPUT_DIR]
	                        Specify the output directory for saving tabs. Defaults
	                        to tabs

	