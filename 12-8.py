def sorted_sentence(sentence):
    words = sentence[:-1].split()
    words = {words[index]: len(words[index]) for index in range(len(words))}
    word_lens = sorted(words.values())
    for length in word_lens:
        for key in words.keys():
            if words[key] == length:
                print(key, end=" ")
                words.update({key: 0})


text = "It is another sentence right now."

sorted_sentence(text)
