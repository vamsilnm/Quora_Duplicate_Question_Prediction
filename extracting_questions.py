import csv





file_open = open('/home/vamsi/Documents/Kaggle/Quora/questions.csv','r')
file_read = csv.reader(file_open)
open_output = open('sample_5_questions.csv','w')
output_writer = csv.writer(open_output)
i = 0
for each_row in file_read:
	output_writer.writerow(each_row)
	i = i + 1
	if i == 5:
		break