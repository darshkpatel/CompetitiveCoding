for case in range(int(input())):
    word = input()
    if len(word)>10:
        new_word = word[0]+str(len(word)-2)+word[-1]
    else:
        new_word = word
    print(new_word)