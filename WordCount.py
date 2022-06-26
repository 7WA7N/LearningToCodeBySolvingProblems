def word_count(words):
    total_words = words.count(' ') + 1
    return print(f'Total Words are {total_words}')

word_count('Hello World')
word_count('Hello World Hello World')
word_count('Hello World Hello World Hello World')