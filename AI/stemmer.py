import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download("wordnet")
nltk.download("omw-1.4")

# Initialize wordnet lemmatizer
ps = PorterStemmer()


words = []
# " I am Mostafa Ahmadi , born on 1379/6/12 , with a height of 174 cm and a weight of 68 kg.My personal email is tah3in@gmail.com. I can say that I am a logical, orderly,patient person and I usually use 😄 😂 😑 emojis and I also use the hashtags #zan_zendegi_azadi "
text = " I am Mostafa Ahmadi , born on 1379/6/12 , with a height of 174 cm and a weight of 70 kg. My personal email is tah3in@gmail.com. I can say that I am a logical, orderly,patient person and I usually use 😄 😂 😑 emojis and I also use the hashtags #zan_zendegi_azadi "
nltk.download('punkt')
tokens = nltk.word_tokenize(text)

# Perform lemmatization
stemmed_words=[ps.stem(i) for i in tokens]

print(stemmed_words)