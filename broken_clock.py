import datetime
import math
def broken_clock(starting_time, wrong_time, error_description):
	start = [int(i) for i in starting_time.split(':')]
	wrong = [int(i) for i in wrong_time.split(':')]

	t1 = datetime.datetime(1,1,1,start[0],start[1],start[2])
	t2 = datetime.datetime(1,1,1,wrong[0],wrong[1],wrong[2])
	diff = t2 -t1

	#diff = diff + datetime.timedelta(seconds=60)
	error = error_description.split(' ')
	for i in range(len(error)):
		try:
			error[i] = int(error[i])
		except:pass
		if error[i] == 'hours' or error[i] == 'hour':
			error[i] ='seconds'
			error[i-1] = error[i-1]*3600
		elif error[i] == 'minutes'or error[i] == 'minute':
			error[i] ='seconds'
			error[i-1] = error[i-1]*60
	print(diff,diff.total_seconds(),error)
	resolution =  diff.total_seconds() / (error[0] + error[3]) *error[0]
	correct = t2 - datetime.timedelta(seconds = resolution)
	print(resolution,correct)

	return ('%g:%02g:%02g'%(correct.hour,correct.minute,correct.second))

print(broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute'))
print(broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds'))
print(broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds'))
print(broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours'))
print(broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds'))
