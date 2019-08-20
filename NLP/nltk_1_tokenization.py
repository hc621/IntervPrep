#import nltk
#nltk.download('all')
# to download all the package within the nltk


'''
### tokenization

# tokenizing - word tokenizer sentence tokenizers
# corpora - body of text. ex: medical journals, presidential speeches
# lexicon = words and their means
from nltk.tokenize import sent_tokenize, word_tokenize
EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great," \
               " and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
# the most straight forward way is to separate by punctuation, space and capital letters.
# a good edge example is the Mr. Smith
print(sent_tokenize(EXAMPLE_TEXT))
print(word_tokenize(EXAMPLE_TEXT))
'''


#####################
###   stopwords  ###
#####################


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration"
# to get the predetermined stopwords embedded in the package
stop_words = set(stopwords.words("english"))
# print(stop_words)

words = word_tokenize(example_sentence)
filtered_sentence= []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

