from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'core python programming',
    '0132356139': 'python web development',
    '0137143419': 'Python Fundamentals', }


def getRanking(isbn):
    print '%s%s' % (AMZN, isbn)
    page = urlopen('%s%s' % (AMZN, isbn))

    data = page.read()
    # print data
    page.close()
    return REGEX.findall(data)[0]


def _showRanking(isbn):
    print '- %r ranked %s' % (ISBNs[isbn], getRanking(isbn))


def _main():
    print 'AT', ctime(), 'on Amazon...'
    for isbn in ISBNs:
        getRanking(isbn)


@register
def _atexit():
    print 'all DONE at:', ctime()


if __name__ == '__main__':
    _main()