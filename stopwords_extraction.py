from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
file = open('stop_words_english','w')

for each_word in stop:
	file.write(each_word)
	file.write('\n')
file.close()

