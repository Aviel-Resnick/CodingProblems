import inflect

p = inflect.engine()
words = []
total_sum = 0

for x in range(1,1001):
    words.append(p.number_to_words(x))

for i in range (0,1000):
    current_word = words[i]
    str_word = str(current_word)
    refined_word = str_word.replace(" ", "")
    refined_word = refined_word.replace("-", "")
    print(refined_word)
    length = len(refined_word)
    total_sum = total_sum + length

print(total_sum)
