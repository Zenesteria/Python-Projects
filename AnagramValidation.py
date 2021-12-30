def AnagramValidator(word1, word2):
    letters_in_word_one = list(str(word1))
    letters_in_word_two = list(str(word2))

    if len(letters_in_word_one) == len(letters_in_word_two):
        final_word = []
        for i in letters_in_word_one:
            for x in letters_in_word_two:
                if i == x:
                    final_word.append(x)
                    if final_word == letters_in_word_one:
                        print("%s is an anagram of %s"%(word1, word2))
        



AnagramValidator('fkst', 'fats')