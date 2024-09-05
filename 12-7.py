def short_len(sentence):
    words = sentence[:-1].split()
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)
    return min_len


text = "This is just a short sentence."

print(short_len(text))
