'''
First 100 (one hundred) minutes in one day are priced at 1 coin per minute;
After 100 minutes in one day, each minute costs 2 coins per minute;
All calls are rounded up to the nearest minute. For example 59 sec ≈ 1 min, 61 sec ≈ 2 min;
Calls count on the day when they began. For example if a call was started 2014-01-01 23:59:59, then it counted to 2014-01-01;
'''
import math
def total_cost(bill):
	data = list(i.split(' ') for i in bill)
	start_time = data[0][0]
	print(data)
	cost = 0
	time = 0
	for i in data:
		date = i[0]
		if date == start_time:
			print(time)
			if time >= 100 :
				cost += 2 * math.ceil(int(i[2]) / 60)
				print('p1 :'+str(cost))
			elif time + math.ceil(int(i[2]) / 60)  < 100:
				cost += math.ceil(int(i[2]) / 60)
				print('p2 :'+str(cost))
			else:
				print(time)
				print(6000-time)
				print(time + int(i[2]) - 6000)
				cost += int(100 - time) + 2 * (time + math.ceil(int(i[2]) / 60) - 100)
				print('p5 :'+str(cost))
			time += math.ceil(int(i[2]) / 60)
		else:
			start_time = i[0]
			time = math.ceil(int(i[2]) / 60)
			if time >= 100:
				cost += 100 + 2 * math.ceil((int(i[2]) - 6000) / 60)
				print('p3 :'+str(cost))
			else:
				cost += math.ceil(int(i[2]) / 60)
				print('p4 :'+str(cost))
	return cost

print(total_cost(
("2054-07-17 10:21:08 1958",
"2054-07-17 16:17:18 1388",
"2054-07-18 00:30:57 729",
"2054-07-18 03:55:30 4970",
"2054-07-18 23:10:05 5397",
"2054-07-19 16:37:31 5894",
"2054-07-20 11:21:10 2537",
"2054-07-20 17:09:49 4398",
"2054-07-21 04:17:34 2839",
"2054-07-21 06:23:25 6229",
"2054-07-21 10:21:01 4540",
"2054-07-21 22:10:46 5599",
"2054-07-22 11:26:43 6199",
"2054-07-23 02:02:52 818",
"2054-07-23 14:30:19 3244",
"2054-07-23 20:46:25 380",
"2054-07-24 08:41:40 4774",
"2054-07-24 23:33:14 5206",
"2054-07-25 08:47:44 3848",
"2054-07-25 11:32:40 694",
"2054-07-25 18:28:25 5974",
"2054-07-26 09:24:52 4550",
"2054-07-26 13:06:07 6637",
"2054-07-27 09:03:40 177",
"2054-07-27 13:11:42 5736",
"2054-07-27 15:53:26 5698",
"2054-07-28 09:51:43 1996",
"2054-07-28 14:03:30 432")))
#print(total_cost(("2014-02-05 01:00:00 60","2014-02-05 02:00:00 60","2014-02-05 03:00:00 60","2014-02-05 04:00:00 6000")))