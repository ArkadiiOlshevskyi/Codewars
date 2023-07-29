'''
Write a function that takes an array of
words and smashes them together into a
sentence and returns the sentence.
You can ignore any need to sanitize words
or add punctuation, but you should add spaces
between each word. Be careful, there shouldn't
be a space at the beginning or the end of the sentence!
'''

def words_to_sentence(dataset):
    sentence = " ".join(word for word in dataset)
    return sentence

dataset = ['Hello', 'word', 'this', 'is', 'great']
sentence = words_to_sentence(dataset)
print(sentence)
