import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
import csv
import codecs

ps = PorterStemmer()
stop_words = set(stopwords.words("english"))

with open('postag.csv','wb') as fp:
	a = csv.writer(fp, delimiter = ',')
	with codecs.open('mann_ki_bat.csv', 'r', encoding = 'utf-8') as f:
		rows = csv.reader(f)
		for row in rows:
			data = row[1]
			words = word_tokenize(data)
			words = filter(lambda x: x not in string.punctuation, words)
			for w in words:
				output = nltk.pos_tag(words)
				a.writerows(output)
