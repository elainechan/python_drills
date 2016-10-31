import string
replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
text = text.translate(replace_punctuation)