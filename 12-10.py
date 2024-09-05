def another_words(sentence):
    words = sentence[:-1].split()
    words_set = set(words) - {words[0]}
    for word in words_set:
        if len(word) == len(set(word)):
            print(word, end=" ")


text = "hello hello hello interest ping no lo."

another_words(text)
