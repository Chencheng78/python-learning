import sys
from numbers import Number
from collections import Set, Mapping, deque

# try: # Python 2
#     zero_depth_bases = (basestring, Number, xrange, bytearray)
#     iteritems = 'iteritems'
# except NameError: # Python 3
#     zero_depth_bases = (str, bytes, Number, range, bytearray)
#     iteritems = 'items'


def getsize(obj_0):
    """Recursively iterate to sum size of object & members."""
    zero_depth_bases = (basestring, Number, xrange, bytearray)
    iteritems = 'iteritems'
    def inner(obj, _seen_ids = set()):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, zero_depth_bases):
            pass # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, iteritems):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, iteritems)())
        # Check for custom object instances - may subclass above too
        if hasattr(obj, '__dict__'):
            size += inner(vars(obj))
        if hasattr(obj, '__slots__'): # can have __slots__ with __dict__
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        return size
    return inner(obj_0)


def read_in_chunks(file_object, chunk_size=1024*1024*10):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

if __name__ == '__main__':
    f = open('K:\\WeChatSetup.exe', 'rb')
    for i in read_in_chunks(f):
        chunk_size = sys.getsizeof(i)
        print chunk_size
        rs = getsize(i)
        print rs
