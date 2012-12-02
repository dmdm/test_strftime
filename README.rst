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



Installation in Windows
-----------------------

1. Install ActivePython, both versions (2.7 and 3.2) can be installed
   in parallel.

   http://www.activestate.com/activepython/downloads

2. As a git client I use msysgit
   
   http://code.google.com/p/msysgit/downloads/detail?name=Git-1.7.11-preview20120710.exe&can=2&q=full+installer+official+git

3. In a msysgit console, install tox via pip:

       $ pip install tox


Desired output
..............

	$ tox
	GLOB sdist-make: c:\Users\dm\MyProgs\test_strftime\setup.py
	py27 sdist-reinst: c:\Users\dm\MyProgs\test_strftime\.tox\dist\test_strftime-1.zip
	py27 runtests: commands[0]
	(u'Locale', 'C', u': language code:', None, u', encoding:', None)
	(u'Locale', 'German_Germany.1252', u': language code:', 'de_DE', u', encoding:', 'cp1252')
	(u'Locale', 'Russian_Russia.1251', u': language code:', 'Russian_Russia', u', encoding:', '1251')
	(u'Locale', 'Russian_Russia.1251', u': language code:', 'Russian_Russia', u', encoding:', '1251')
	(u'Locale', 'English_United Kingdom.1252', u': language code:', 'English_United Kingdom', u', encoding:', '1252')
	(u'Locale', 'C', u': language code:', None, u', encoding:', None)
	(u'Locale', 'German_Germany.1252', u': language code:', 'de_DE', u', encoding:', 'cp1252')
	(u'Locale', 'English_United Kingdom.1252', u': language code:', 'English_United Kingdom', u', encoding:', '1252')
	(u'Locale', 'Russian_Russia.1251', u': language code:', 'Russian_Russia', u', encoding:', '1251')
	(u'Locale', 'Russian_Russia.1251', u': language code:', 'Russian_Russia', u', encoding:', '1251')
	.
	----------------------------------------------------------------------
	Ran 1 test in 0.140s

	OK
	py32 sdist-reinst: c:\Users\dm\MyProgs\test_strftime\.tox\dist\test_strftime-1.zip
	py32 runtests: commands[0]
	Locale C : language code: None , encoding: None
	Locale German_Germany.1252 : language code: de_DE , encoding: cp1252
	Locale Russian_Russia.1251 : language code: Russian_Russia , encoding: 1251
	Locale Russian_Russia.1251 : language code: Russian_Russia , encoding: 1251
	Locale English_United Kingdom.1252 : language code: English_United Kingdom , encoding: 1252
	Locale C : language code: None , encoding: None
	Locale German_Germany.1252 : language code: de_DE , encoding: cp1252
	Locale English_United Kingdom.1252 : language code: English_United Kingdom , encoding: 1252
	Locale Russian_Russia.1251 : language code: Russian_Russia , encoding: 1251
	Locale Russian_Russia.1251 : language code: Russian_Russia , encoding: 1251
	.
	----------------------------------------------------------------------
	Ran 1 test in 0.031s

	OK
	_______________________________________________________ summary __________________________________________________
	  py27: commands succeeded
	  py32: commands succeeded
	  congratulations :)

	$ cat formatted_dates.txt
	Locale: C, language code: None, encoding: None
	.. Formatted date:Fri, 02 March 2012
	Locale: German_Germany.1252, language code: de_DE, encoding: cp1252
	.. Formatted date:Fr, 02 März 2012
	Locale: Russian_Russia.1251, language code: Russian_Russia, encoding: 1251
	.. Formatted date:Пт, 02 Март 2012
	Locale: Russian_Russia.1251, language code: Russian_Russia, encoding: 1251
	.. Formatted date:Пт, 02 Март 2012
	Locale: English_United Kingdom.1252, language code: English_United Kingdom, encoding: 1252
	.. Formatted date:Fri, 02 March 2012
	Locale: C, language code: None, encoding: None
	.. Formatted date:Fri, 02 March 2012 Øl trinken beim Besäufnis
	Locale: German_Germany.1252, language code: de_DE, encoding: cp1252
	.. Formatted date:Fr, 02 März 2012 Øl trinken beim Besäufnis
	Locale: English_United Kingdom.1252, language code: English_United Kingdom, encoding: 1252
	.. Formatted date:Fri, 02 March 2012 Øl trinken beim Besäufnis
	Locale: Russian_Russia.1251, language code: Russian_Russia, encoding: 1251
	.. Formatted date:Пт, 02 Март 2012 Ol trinken beim Besaufnis
	Locale: Russian_Russia.1251, language code: Russian_Russia, encoding: 1251
	.. Formatted date:Ol trinken beim Besaufnis

