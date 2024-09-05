def reversed_sentence(sentence):
    sign = sentence[-1]
    string = sentence[:-1].split()
    string.reverse()
    string[0] = string[0].capitalize()
    string[-1] = string[-1].lower()
    new_sentence = " ".join(string)
    print(new_sentence + sign)


text = "Hello world, I like you."

reversed_sentence(text)
