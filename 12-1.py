def max_space_streak(text):
    counter = 0
    max_counter = 0
    for letter in text:
        if letter == " ":
            counter += 1
        else:
            if counter > max_counter:
                max_counter = counter
            counter = 0
    return max_counter


string = "sd dd  sd    dddd           salad"

print(max_space_streak(string))
