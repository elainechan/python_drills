"""
wordcount.py

Counts the occurrences of each word in any given phrase.
"""
from collections import Counter
import string
from string import punctuation

def word_count(phrase=''):
       
        for ch in phrase:
                if ch in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                        phrase = phrase.replace(ch, " ")
                        return phrase
        print(phrase)
        return Counter(phrase.lower().split())


## Replace punctuations with space
## Convert letters to lower case
##        .lower
## Split phrase into list of words
##        .split
## Count occurence of each word
##        Counter()
        
##	clean = phrase.maketrans(phrase.punctuation, ' '*len(phrase.punctuation))
##	text = text.translate(clean)
##	print(text)

##	clean = str.maketrans("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

	
    # clean = ''.join(chr for chr in phrase if chr not in punctuation)
    # print(clean)
    # return Counter(clean.lower().split())
##        clean = str.replace(c for c in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~", " ")
##        clean = str.replace("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~", " ")

##        clean = ' '.join([c for c in phrase if not c.isalpha()])
##        print(clean)
