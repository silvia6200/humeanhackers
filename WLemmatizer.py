from nltk.stem.wordnet import WordNetLemmatizer
import nltk

def lmtz(word):

	
	wl = WordNetLemmatizer()
	words = word.split('/')
	word = words[0]
	tag = words[1]
	if tag.startswith('V'):
		return (wl.lemmatize(word,'v') + "/" + tag)
	else:
		return (wl.lemmatize(word) + "/" + tag)
	