from translate import translated_words_list

word_list = translated_words_list
new_wl = []
i = 0
len_stroke = 13

while i < len(word_list):
    if i+1 == len(word_list):
        new_wl.extend([word_list[i]])
        i += 1
    elif i+2 == len(word_list):
        if len(word_list[i] + word_list[i+1]) < len_stroke:
            new_wl.extend([word_list[i], word_list[i+1]])
            i += 2
        else:
            new_wl.extend([word_list[i], '\n'])
            i += 1
    else:
        if len(word_list[i] + word_list[i+1] + word_list[i+2]) < len_stroke:
            new_wl.extend([word_list[i], word_list[i+1], word_list[i+2], '\n'])
            i += 3
        elif len(word_list[i] + word_list[i+1]) < len_stroke:
            new_wl.extend([word_list[i], word_list[i+1], '\n'])
            i += 2
        else:
            new_wl.extend([word_list[i], '\n'])
            i += 1

line = ' '.join(new_wl)
print(line)