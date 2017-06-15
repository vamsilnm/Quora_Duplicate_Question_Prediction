import csv





file_open = open('/home/vamsi/Documents/Kaggle/Quora/questions.csv','r')
file_read = csv.reader(file_open)
count_0 = 0
count_1 = 0
for each_row in file_read:
	if each_row[5] == '0':
		count_0 += 1
	else:
		count_1 += 1

	if count_0 % 10000 == 0:
		print 'processing'
	
print 'Duplicate_questions_count',count_0
print 'Different_questions_count',count_1
print count_0+count_1