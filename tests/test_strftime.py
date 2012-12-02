# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nose.tools import assert_equal
import datetime
import locale
import six
import re
import sys
import codecs
import os

DAY = 2
MON = 3 # Name of month 3 has umlaut (= non-ascii char) in German locale
YEAR = 2012


def fmt(new_locale, date_format, expected_result):
    # Set and check locale
    if not six.PY3:
        # Locale must be byte string for Python<3
        new_locale = new_locale.encode('utf-8')
    locale.setlocale(locale.LC_ALL, new_locale)
    assert_equal(locale.setlocale(locale.LC_ALL, None), new_locale)
    
    # BEGIN DEBUG
    # Actually, getlocale() is only needed for Python < 3. See below.
    lang_code, enc = locale.getlocale(locale.LC_ALL)
    print("Locale", new_locale, ": language code:", lang_code, ", encoding:", enc)
    # END DEBUG
    
    # Format date and check it
    d = datetime.date(YEAR, MON, DAY)
    if six.PY3:
        # It could be so easy... *sigh*
        result = d.strftime(date_format)
    else:
        # We must ensure that the format string is an encoded
        # byte string, ASCII only WTF!!!
        # But with "xmlcharrefreplace" our formatted date will produce *yuck*
        # like this:
        #        "Øl trinken beim Besäufnis"
        #    --> "&#216;l trinken beim Bes&#228;ufnis"
        date_format = date_format.encode('ascii', errors="xmlcharrefreplace")
        result = d.strftime(date_format)
        # strftime() returns an encoded byte string
        # which we must decode into unicode.
        lang_code, enc = locale.getlocale(locale.LC_ALL)
        if enc:
            result = result.decode(enc)
        else:
            result = unicode(result)
        # Convert XML character references back to unicode characters.
        if "&#" in result:
            result = re.sub(r'&#(?P<num>\d+);'
                , lambda m: unichr(int(m.group('num')))
                , result
            )

    # BEGIN DEBUG
    with codecs.open("formatted_dates.txt", "a", encoding="utf-8") as fh:
        fh.write("Locale: " + new_locale + ", language code: " + str(lang_code) + ", encoding: " + str(enc) + "\n")
        fh.write(".. Formatted date:" + result + "\n")
    # END DEBUG

    assert_equal(result, expected_result)


def test_strftime():
    try:
        os.unlink("formatted_dates.txt")
    except (WindowsError, IOError, OSError):
        pass
    if sys.platform == 'win32':
        # MSDN articles about locales:
        # - General format of locale string: http://msdn.microsoft.com/en-us/library/hzz3tw78.aspx
        # - Language strings: http://msdn.microsoft.com/en-us/library/39cwe7zf.aspx
        # - Country/Region: http://msdn.microsoft.com/en-us/library/cdax410z.aspx
        # - About code pages: http://msdn.microsoft.com/en-us/library/2x8et5ee.aspx
        # - setlocale() w/ samples: http://msdn.microsoft.com/en-us/library/x99tb11d.aspx
        fmt("C", "%a, %d %B %Y", "Fri, 02 March 2012")
        fmt("German_Germany.1252", "%a, %d %B %Y", "Fr, 02 März 2012")
        fmt("Russian_Russia.1251", "%a, %d %B %Y", "\u041f\u0442, 02 \u041c\u0430\u0440\u0442 2012")
        fmt("Russian_Russia.1251", "%a, %d %B %Y", "Пт, 02 Март 2012")
        # Get locale from console
        loc = locale.setlocale(locale.LC_ALL, '')
        # XXX My console is set to en_GB.UTF-8. If your setting is different, you may
        # XXX have to adjust the excpected result here!
        fmt(loc, "%a, %d %B %Y", "Fri, 02 March 2012")

        # Now, what if the format string itself contains non-ascii chars?
        fmt("C", "%a, %d %B %Y Øl trinken beim Besäufnis", "Fri, 02 March 2012 Øl trinken beim Besäufnis")
        fmt("German_Germany.1252", "%a, %d %B %Y Øl trinken beim Besäufnis", "Fr, 02 März 2012 Øl trinken beim Besäufnis")
        fmt("English_United Kingdom.1252", "%a, %d %B %Y Øl trinken beim Besäufnis", "Fri, 02 March 2012 Øl trinken beim Besäufnis")
        if six.PY3:
            # Py3 "normalizes" non-ascii chars to their ascii simile, e.g. `Ø' --> `O'
            fmt("Russian_Russia.1251", "%a, %d %B %Y Øl trinken beim Besäufnis", "Пт, 02 Март 2012 Ol trinken beim Besaufnis")
            fmt("Russian_Russia.1251", "Øl trinken beim Besäufnis", "Ol trinken beim Besaufnis")
        else:
            fmt("Russian_Russia.1251", "%a, %d %B %Y Øl trinken beim Besäufnis", "Пт, 02 Март 2012 Øl trinken beim Besäufnis")
            fmt("Russian_Russia.1251", "Øl trinken beim Besäufnis", "Øl trinken beim Besäufnis")
    else:
        fmt("C", "%c", "Fri Mar  2 00:00:00 2012")
        fmt("de_DE", "%c", "Fr 02 Mär 2012 00:00:00 ") # trailing blank WTF??
        fmt("de_DE.iso88591", "%c", "Fr 02 Mär 2012 00:00:00 ") # trailing blank WTF??
        fmt("de_DE.iso885915@euro", "%c", "Fr 02 Mär 2012 00:00:00 ") # trailing blank WTF??
        fmt("ru_RU.CP1251", "%c", "Птн 02 Мар 2012 00:00:00") # NO trailing blank :-)
        # Get locale from console
        loc = locale.setlocale(locale.LC_ALL, '')
        # XXX My console is set to en_GB.UTF-8. If your setting is different, you may
        # XXX have to adjust the excpected result here!
        fmt(loc, "%c", "Fri 02 Mar 2012 00:00:00 ") # trailing blank WTF??

        # Now, what if the format string itself contains non-ascii chars?
        # Grr, some questions may better not be asked...
        # Non-ASCII characters in format string in Python < 3 forces us to do the 
        # xmlcharrefreplace-regex-dance, see above.
        fmt("C", "%c Øl trinken beim Besäufnis", "Fri Mar  2 00:00:00 2012 Øl trinken beim Besäufnis")
        fmt("de_DE.iso88591", "%c Øl trinken beim Besäufnis", "Fr 02 Mär 2012 00:00:00  Øl trinken beim Besäufnis")
        fmt("en_GB.UTF-8", "%c Øl trinken beim Besäufnis", "Fri 02 Mar 2012 00:00:00  Øl trinken beim Besäufnis")
        fmt("ru_RU.CP1251", "%c Øl trinken beim Besäufnis", "Птн 02 Мар 2012 00:00:00 Øl trinken beim Besäufnis")
