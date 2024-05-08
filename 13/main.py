##import nltk
##from nltk.tokenize import word_tokenize
import re
from collections import Counter
file = open('txtw', 'r').read()
##nltk.download('punkt')
print(file.split())
token = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+", file)
print(token)
print(len(token))
print(Counter(token))
##nldo = word_tokenize(file)
##print(nldo)