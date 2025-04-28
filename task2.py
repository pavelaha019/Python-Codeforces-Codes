sentence = input("Enter a sentence: ")
words = sentence.lower().split()
word_count = {}

for word in words:
    word = word.strip(".,!?")
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
