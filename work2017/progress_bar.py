import time
import thread
import sys

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '+'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()
    # Print New Line on Complete
    if iteration == total:
        print()

#
# Sample Usage
#

from time import sleep

# A List of Items
items = list(range(0, 10))
l = len(items)

# Initial call to print 0% progress
print time.ctime()
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    sleep(0.5)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
print time.ctime()


# def progress(width, percent):
#     print "\r%s %d%%" % (('%%-%ds' % width) % (width * percent / 100 * '='), percent),
#     if percent >= 100:
#         print sys.stdout.flush()
#
#
#
# def demo1():
#     for i in xrange(100):
#         progress(50, (i + 1))
#         time.sleep(0.1)
#
#
#
# def demo2():
#     i = 19
#     n = 200
#     while n > 0:
#         print "\t\t\t%s \r" % (i * "="),
#         i = (i + 1) % 20
#         time.sleep(0.1)
#         n -= 1

# for i in range(100):
#     time.sleep(1)
#     sys.stdout.write("\r%d%%" % i)
#     sys.stdout.flush()
#demo1()
#demo2()
# class Progress:
#     def __init__(self):
#         self._flag = False
#
#     def timer(self):
#         i = 19
#         while self._flag:
#             print "\t\t\t%s \r" % (i * "="),
#             sys.stdout.flush()
#             i = (i + 1) % 20
#             time.sleep(0.05)
#         print "\t\t\t%s\n" % (19 * "="),
#         thread.exit_thread()
#
#     def start(self):
#         self._flag = True
#         thread.start_new_thread(self.timer, ())
#
#     def stop(self):
#         self._flag = False
#         time.sleep(1)
#
# if __name__ == '__main__':
#     progress = Progress()
#     progress.start()
#     time.sleep(10)
#     progress.stop()
