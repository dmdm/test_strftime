This is a testbed to test `strftime()` in different environments.

The unittest needs tox and nose. It checks the output of `strftime()` in
Python 2.7 and Python 3.2 for several locales.

Make sure the tested locales are installed on your system.

Run from command line:

	$ tox

The test writes the formatted dates into file "./formatted_dates.txt".
The file is encoded in UTF-8. I would have preferred to just print
the foratted date out on the console, but in Windows this proved rather
annoying (impossible due to encoding glitches).
