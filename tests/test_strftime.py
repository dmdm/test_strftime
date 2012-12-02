# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from nose.tools import assert_equal
import datetime
import locale
import six

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
    result = d.strftime(date_format)
    if not six.PY3:
        # For Python < 3 we must decode from set locale into unicode
        lang_code, enc = locale.getlocale(locale.LC_ALL)
        if enc:
            result = result.decode(enc)
    assert_equal(result, expected_result)


def test_strftime():
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
