import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")
nltk.download("omw-1.4")

# Initialize WordNet lemmatizer
wl = WordNetLemmatizer()

words = []
text = "I am Mostafa Ahmadi, born on 1379/6/12, with a height of 174 cm and a weight of 70 kg. My personal email is tah3in@gmail.com. I can say that I am a logical, orderly, patient person and I usually use 😄 😂 😑 emojis and I also use the hashtags #zan_zendegi_azadi"
nltk.download('punkt')
tokens = nltk.word_tokenize(text)

# Perform lemmatization
lemmatized_words = [wl.lemmatize(i) for i in tokens]

print(lemmatized_words)
