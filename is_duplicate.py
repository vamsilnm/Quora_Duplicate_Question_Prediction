import csv
import re
from nltk.corpus import wordnet_ic
import math
from nltk.corpus import wordnet as wn
brown_ic = wordnet_ic.ic('ic-brown.dat')


def preprocessing():
	stop_words = []
	file_open_stop = open('stop_words_english','r')
	for each_stop_word in file_open_stop:
		stop_words.append(each_stop_word.strip())
	file_open = open('/home/vamsi/Documents/Kaggle/Quora/sample_5_questions.csv','r')
	file_read = csv.reader(file_open)
	questions_clean = []
	for each_row in file_read:
		question_1_clean = []
		question_2_clean = []
		question_1 = each_row[3]
		question_2 = each_row[4]
		for each_word in question_1.split():
			question_1_clean.append(re.sub(r'[^A-Za-z0-9]','',each_word))
		for each_word in question_2.split():
			question_2_clean.append(re.sub(r'[^A-Za-z0-9]','',each_word))
		question_1_final = [each_word.lower() for each_word in question_1_clean if each_word.lower() not in stop_words]
		question_2_final = [each_word.lower() for each_word in question_2_clean if each_word.lower() not in stop_words]
		questions_clean.append([question_1_final,question_2_final])
	return questions_clean

def sim_table(questions):
	sim_table_total = []
	for each_question_pair in questions:
		unq_wds = set(each_question_pair[0]+each_question_pair[1])
		sim_table= []
		for each_word in unq_wds:
			row=[]
			for every_word in unq_wds:
				row.append(similarity(each_word,every_word,'jcn'))
			sim_table.append(row)
		sim_table_total.append(sim_table)
	print sim_table_total
	raw_input()
 	return sim_table_total

def similarity(str1,str2,type_1):
	try :
		word1 = wn.synset(str1 + '.n.01')
		word2 = wn.synset(str2 + '.n.01')
		if type_1 == 'jcn':
			return word1.jcn_similarity(word2, brown_ic)
	except :
		return 0

def is_duplicate(questions,sim_table):
	question_number = 0
	similarity_score_list = []
	file_open_output = open('questions_similarity_scores.csv','w')
	output_writer = csv.writer(file_open_output)
	output_writer.writerow(['question_1','question_2','similarity_score'])
	for each_question_pair in questions:
		unique_words = set(each_question_pair[0]+each_question_pair[1])
		question_vector_1 = []
		question_vector_2 = []
		for each_word in unique_words:
			if each_word in each_question_pair[0]:
				question_vector_1.append(1)
			else:
				question_vector_1.append(0)
			if each_word in each_question_pair[1]:
				question_vector_2.append(1)
			else:
				question_vector_2.append(0)
		similarity_score = 0
		for each_value in range(0,len(question_vector_1)):
			for every_value in range(0,len(question_vector_2)):
				if question_vector_1[each_value] * question_vector_2[every_value] :
					similarity_score += sim_table[question_number][question_vector_1[each_value]][question_vector_2[each_value]]
		similarity_score = similarity_score/math.sqrt(sum(question_vector_1)*sum(question_vector_2))
		similarity_score_list.append(similarity_score)
		output_writer.writerow([each_question_pair[0],each_question_pair[1],similarity_score])

	# return similarity_score_list




if __name__ == '__main__':
	questions_total = preprocessing()
	is_duplicate(questions_total,sim_table(questions_total))







