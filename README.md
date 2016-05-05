# TabHero
Python command line tool to search and download guitar tabs from ultimate-guitar.com for different songs

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
	                        to tabs/

You will download (or print) the top item based on your search results by default.

The option to manually select from the search results is also available.

Example Usage:

	> python tabhero.py -s -p colourblind
	Searching...

	[1] Hands Like Houses - Colourblind - 5/5 - tab
	[2] Darius - Colourblind - 2/5 - chords
	[3] Darius - Colourblind (ver 2) - 4/5 - chords
	[4] Darius - Colourblind - 0/5 - ukulele chords
	[5] Elyar Fox - Colourblind - 0/5 - chords
	[6] Grass - Colourblind - 0/5 - chords
	[7] Hardship Post - Colourblind - 0/5 - chords
	[8] Hardship Post - Colourblind - 0/5 - ukulele chords

	Select a tab number: 1

	Downloading tab...


	Hands Like Houses - Colourblind
	-------------------------------


	+ --------------------------------------------------------------------- +
	| Ultimate Guitar Tabs Archive - your #1 source for tabs!               |
	| http://www.ultimate-guitar.com/                                       |
	|                                                                       |
	| Over 1,000,000 guitar, guitar pro and bass tabs! Also lessons         |
	| news and guitar forums!                                               |
	+ --------------------------------------------------------------------- +

	Tabbed by: jcameronp
	Tuning: Drop B
	Guitar 1 - Lead
	Guitar 2 - Rhythm

	-----

	Intro
	Guitar 1
	C#|---8-5---8-5-3------------------------------------------------------------|
	G#|--------------------------------------------------------------------------|
	 E|-7-----7------------------------------------------------------------------|
	 B|--------------------------------------------------------------------------|
	F#|--------------------------------------------------------------------------|
	 B|--------------------------------------------------------------------------|
	Guitar 2
	C#|--------------------------------------------------------------------------|
	G#|--------------------------------------------------------------------------|
	 E|--------------------------------------------------------------------------|
	 B|--------------------------------------------------------------------------|
	F#|--------------------------------------------------------------------------|
	 B|-0-0-0-00-00-0-0-8-8-8-0-0-0-3-3-3-10-10-0-0-0-00-00-0-0-8-8-8-0-0-0------|

	C#|--------------------------------------------------------------------------|
	G#|--------------------------------------------------------------------------|
	 E|--------------------------------------------------------------------------|
	 B|--------------------------------------------------------------------------|
	F#|--------------------------------------------------------------------------|
	 B|-5-5-5-5-10-10-10-10------------------------------------------------------|

	 ...

This is just something I wanted to do in my free time.

Hopefully it helps prevents someone from having to go to the website, search, then copy and paste into a separate file.
