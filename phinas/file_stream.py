import io
import hashlib
import os



def file_size(filename):
    try:
        size = os.stat(filename)
        return int(size.st_size)
    except WindowsError as e:
        print '%s not found.' % e
        return False


def file_hash(filename):
    try:
        opened_file = open(filename, 'rb')
        sha256 = hashlib.sha256()
        # md5 = hashlib.md5()
        while True:
            data = opened_file.read(1024*1024)
            if not data:
                break
            sha256.update(data)
        return sha256.hexdigest()
    except IOError as e:
        print e
        return False


def buffered_hash(fileobj, size=None, step=1024*1024*128):
    sha256 = hashlib.sha256()
    p_size = 0
    if size:
        while p_size <= size - step:
            data = fileobj.read(step)
            p_size += step
            # print p_size
            if not data:
                break
            sha256.update(data)
        return sha256
    else:
        while True:
            data = fileobj.read(step)
            if not data:
                break
            sha256.update(data)
        return sha256


# def FpCalc():


def read_in_chunks(file_object, chunk_size= 1024 * 1024 *1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data



if __name__ == '__main__':
    # Create the form with simple fields
    # hv = file_hash('K:\\largevideo.mkv')
    # print hv
    total_hash = '3d840a8bf11af122f152e2922fa32e5ca45232e3ae45c8e39360b1a0a5e6fdc1'


    chunked_hash = ['d8460e536a682f5ba25a752ea7a048cdd2f883791e45c19f56dd973a717d46b1',
                    '83d6ae583ecd90d8ca8e191bfca260dbec683fc5b39d4010770392bedc43d48e',
                    'b5eaf0d1a7822b3cfe9cbf68d150716fa3953bdee64e01d1036892c00c619164',
                    '6d4b74565e893d2d0c0cbf62d595b86368c2d232b8a81b9ca508cc734e2187be']

    [0, 'd8460e536a682f5ba25a752ea7a048cdd2f883791e45c19f56dd973a717d46b1',
     'df80fa609f39fbf2a7e9867d61e242f93ab6ec955902157ab19739063994c491',
     'd3f5fe5512096dfa463b021bec4286f4d9b82429bbac25e1661fddcf6fa03988',
     '9887176f2a48defd5f1343dcb42de864dba6f01ffac47e3e21060185c8d623e0']
    #
    #
    # pv1 = file_hash('K:\\largevideo_part0')
    # print pv1
    # pv2 = file_hash('K:\\largevideo_part1')
    # print pv2
    # pv3 = file_hash('K:\\largevideo_part2')
    # print pv3
    # pv4 = file_hash('K:\\largevideo_part3')
    # print pv4
    # print total_hash
    #
    #
    fp = hashlib.sha256()
    fp.update(bytearray.fromhex(chunked_hash[0]))
    print fp.hexdigest()
    fp.update(bytearray.fromhex(chunked_hash[1]))
    print fp.hexdigest()


    # f = io.open('K:\\largevideo.mkv', 'rb')
    # buffered_reader = io.BufferedReader(f)
    # position = 0
    # bf_hash = []
    # bf_hash.append(buffered_hash(buffered_reader, size=1024*1024*1024))
    # buffered_reader.seek(1024*1024*1024)
    # fp0 = bf_hash[0][0]
    # print fp0.hexdigest()
    # bf_hash.append(buffered_hash(buffered_reader, fp0, size=1024*1024*1024))
    # fp1 = bf_hash[1][1]
    # print fp1.hexdigest()
    # buffered_reader.seek(1024*1024*1024*2)
    # bf_hash.append(buffered_hash(buffered_reader, fp1, size=1024*1024*1024))
    # fp2 = bf_hash[2][1]
    # print fp2.hexdigest()
    # buffered_reader.seek(1024*1024*1024*3)
    # bf_hash.append(buffered_hash(buffered_reader, fp2, size=1024*1024*1024))
    # fp3 = bf_hash[3][1]
    # print fp3.hexdigest()
    # print bf_hash

    # bf_hash = []
    # bf_hash.append(buffered_hash(buffered_reader, size=1024*1024*1024))
    # buffered_reader.seek(0)
    # bf_hash.append(buffered_hash(buffered_reader, size=1024*1024*1024*2))
    # buffered_reader.seek(0)
    # bf_hash.append(buffered_hash(buffered_reader, size=1024*1024*1024*3))
    # buffered_reader.seek(1024*1024*1024*3)
    # bf_hash.append(buffered_hash(buffered_reader, size=1024*1024*1024))

    # print bf_hash
    # bf_hexhash = [i[0].hexdigest() for i in bf_hash]
    # print bf_hexhash

    # fp0 = bf_hash[0]
    # fp1 = bf_hash[0].update(bf_hash[1])
    # fp2 = fp1.update(bf_hash[2])
    # print fp0.hexdigest()
    # print fp1.hexdigest()
    # print fp2.hexdigest()
