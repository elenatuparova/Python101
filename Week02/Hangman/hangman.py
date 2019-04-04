def hangman(clue_word):
    hangman_figure = ' _________ \n|    |    |\n|  \ O /  |\n|    |    |\n|    |    |\n|   / \   |'
    print('Welcome to Hangman! Let\'s play!')
    coded_word = ['_' for ch in clue_word]
    to_guess = len(clue_word)
    print(''.join(ch for ch in coded_word))
    mistakes = 0
    while mistakes < 10 and to_guess > 0:
        current_guess = input('Guess a letter: ')
        if current_guess not in clue_word:
            mistakes += 1
            print('Incorrect!')
        else:
            for index, ch in enumerate(clue_word):
                if current_guess == ch:
                    coded_word[index] = ch
                    to_guess -= 1
            print(''.join(ch for ch in coded_word))
    if to_guess == 0:
        print('Congratulations!')
    else:
        print('You lost!')
        print(hangman_figure)
