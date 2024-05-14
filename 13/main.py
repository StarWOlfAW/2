import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
import matplotlib.pyplot
import spacy


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
file = open('txtw.txt', 'r').read()
opt = re.sub(r'[^\w\s]','', file)
nlp = spacy.load('en_core_web_sm')
nltk.download('wordnet')
print(opt.split())
tokend = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+", opt)
token = word_tokenize(opt)
wistop = [word for word in token if not word in stopwords.words('english')]
stemmed_words = [stemmer.stem(word) for word in token]
lemmatized_words = [lemmatizer.lemmatize(word) for word in token]
print(token)
print(len(token))
print(Counter(token))
fdist = FreqDist(token)
fdist.most_common(5)
certain = FreqDist(wistop)
certain.plot(30,cumulative=False)
doc = nlp(opt)
for tokens in doc:
    print(tokens.text, tokens.lemma_)


nldo = word_tokenize(opt)
print(nldo)
print(wistop)
print(stemmed_words)
print(lemmatized_words)