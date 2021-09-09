def duplicate_encode(word):
    """
    Function takes a string as an argument and returns the same string encoded.
    If a character in a string appears only once, it becomes ')', if more than once – '('.
    """
    # to ignore case of a word:
    word = word.lower()
    new_word = []
    new_letter = ''

    for i in range(len(word)):
        count_letter = word.count(word[i])
        if count_letter > 1:
            new_letter = ')'
        elif count_letter == 1:
            new_letter = '('
        new_word.append(new_letter)
    return ''.join(new_word)


print(duplicate_encode("!(CNzxDeIg i)UkCYZ@@O)yHMBGS@YqlPRah"))
