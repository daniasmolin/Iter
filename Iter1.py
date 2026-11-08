class WordLengthIterator:
    def __init__(self, words_list):
        self.words = words_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return len(word)

words = ["програмування", "ітератор", "Python", "код", "розробка"]
length_iterator = WordLengthIterator(words)

print("Довжини слів:")
for length in length_iterator:
    print(length)