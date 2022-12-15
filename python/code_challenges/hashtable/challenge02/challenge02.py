# Write here the code challenge solution
import re
def first_repeated(s):
    s = re.sub(r'[^\w\s]', '', s) # Remove non-alphanumeric characters from aa string
    s=re.split(' ',s) # convert string to list of words
    d={}
    for word in s:
        d[word]= 1+ d.get(word,0)
    for word in d:
        if d[word]>1:
            return word
    return "No Repetition"