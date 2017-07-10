import os
import subprocess
import time
import csv

work_dir = 'C:\\Program Files (x86)\\Ixia\\IxChariot'
tst_file = 'Tests\\test1.tst'
os.chdir(work_dir)
print os.getcwd()

runtst_cmd = 'runtst %s -t 60' % tst_file
runtst = subprocess.check_output(runtst_cmd)
print runtst
print '~~~~~~~~~~~~~~~~'
time.sleep(2)
if 'Ending time:' in runtst:
    current_time = time.strftime('%m_%d_%H_%M_%S', time.localtime())
    results_file = 'Results\\result_%s.csv' % current_time
    fmttst_cmd = 'fmttst.exe %s %s -v -s' % (tst_file, results_file)
    fmttst = subprocess.check_output(fmttst_cmd)
else:
    print 'chariot running error!'

with open(results_file, 'rb') as f:
    reader = csv.reader(f)

    for row in reader:
        if ''.join(row) == 'GROUP AVERAGES':
            k = reader.next()
            v = reader.next()
            break
    f.close()

    dict_results = dict(zip(k, v))
    print 'Throughput Avg.(Mbps):' + dict_results['Throughput Avg.(Mbps)']
