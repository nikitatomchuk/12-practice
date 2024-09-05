def max_same_letter_streak(text):
    counter = 1
    max_counter = 0
    last_letter = text[0]
    for letter in text:
        if letter == last_letter:
            counter += 1
            max_counter = max(counter, max_counter)
        else:
            max_counter = max(counter, max_counter)
            counter = 1
        last_letter = letter
    return max_counter


string = "lllddddlfffffllkkkkkk"

print(max_same_letter_streak(string))
