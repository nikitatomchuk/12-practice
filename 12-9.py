def find_repeated(sentence):
    words = sentence[:-1].split()
    answer = "No words met twice"
    for word in words:
        if sentence.count(word) == 2:
            answer = word
            break
    return answer


text = "Hello my dear dear friend."

print(find_repeated(text))
