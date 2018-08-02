import os
import math

def read_in_chunks(file_object, chunk_size=1024 * 1024 * 10):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

if __name__ == '__main__':
    filenames = 'K:\\largevideo.mkv'
    output_names = 'K:\\largevideo_part'
    MegaByte = 1024 * 1024
    GigaByte = 1024 * 1024 * 1024
    Custom_size = 111

    file_size = float(os.stat(filenames).st_size)
    parts = int(math.ceil(file_size / GigaByte))
    print parts
    with open(filenames, 'rb') as f:
        cut_size = GigaByte
        chunk_size = 1024*1024
        for i in range(parts):
            psize = 0
            output_part = output_names + '%s' % i
            with open(output_part, 'wb') as of:
                while psize <= cut_size - chunk_size:
                    j = f.read(chunk_size)
                    of.write(j)
                    psize += chunk_size
