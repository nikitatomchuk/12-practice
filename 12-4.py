def three_times_letter(text):
    let_set = set(text)
    answer = None
    let_counts = {letter: text.count(letter) for letter in let_set}
    for letter in let_counts.keys():
        if let_counts[letter] == 3:
            answer = letter
    return answer


string = "sdfawfgsdlll"


print(three_times_letter(string))