import nltk
from nltk.tokenize import word_tokenize
import re
file = open('txtw', 'r').read()
nltk.download('punkt')
print(file.split())
token = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+", file)
print(token)
nldo = word_tokenize(file)
print(nldo)