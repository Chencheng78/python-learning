import os
import subprocess
import time

work_dir = 'C:\\Program Files (x86)\\Ixia\\IxChariot'
tst_file = 'Tests\\test1.tst'
#print os.getcwd()
os.chdir(work_dir)
print os.getcwd()

runtst_cmd = 'runtst %s -t 60' %tst_file
runtst = subprocess.check_output(runtst_cmd)
print runtst
print '~~~~~~~~~~~~~~~~'
time.sleep(2)
if 'Ending time:' in runtst:
    current_time = time.strftime('%m_%d_%H_%M_%S', time.localtime())
    results_file = 'result_%s' % current_time
    fmttst_cmd = 'fmttst.exe Tests\\test1.tst Results\\%s -v' % results_file
    fmttst = subprocess.check_output(fmttst_cmd)
else:
    print 'chariot running error!'

