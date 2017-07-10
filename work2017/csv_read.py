import csv

with open('result\\result11.csv', 'rb') as f:
    reader = csv.reader(f)
    #print reader.line_num

    for row in reader:
        if ''.join(row) == 'GROUP AVERAGES':
            a = reader.next()
            b = reader.next()
            break
    print len(a)
    print len(b)
    list1 =  zip(a,b)
    dict1 = dict(list1)
    print dict1['Throughput Avg.(Mbps)']
# print '~~~~~~~~~~~~~~~~~~~'
# with open('result1.csv', 'rb') as f:
#     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         print row

# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
