"""
Module 3 - Hangman in python3.9 by Matthew Barson

Requirements:
- The program must run in Python3 without error.
- The script must ONLY stop to either ask for the next guess or because the game has been won or lost (i.e. no menus or
    other user input).
- Asking the user to make her next guess must use the following text (case sensitive and a space after the colon are
    necessary (I think)): “Please enter your next guess: “
- The text printed before “Please enter your next guess: “ must END in the word to be guessed with the unknown letters
    starred out (i.e. hello would start as ***** and change into *e*** after ‘e’ was guessed). The string must not contain
    any other stars.
- The program must print either “congratulations you win” or “you lose” on exit (not case sensitive).
- When a game is played, a word must be picked randomly (from a uniform distribution) from the word_list.txt file.
- The word_list.txt file must be stored in the same path as your code and when you load the file don't include the path
    (i.e. "open('word_list.txt', ...)").
- If the user makes 7 wrong guesses then they lose the game.

Notes
word_list copied from inbuilt mac /usr/share/dict/words
"""

import random


class Hangman:
    def __init__(self, number_of_guesses=7):
        with open('./word_list.txt', 'r') as file:
            words = file.readlines()
            self.word = words[random.randint(0, len(words))]  # Random word from list of words.
            self.word = self.word.lower().strip()  # lower case so guesses can be case unsensitive.
        self.guessed_letters = ''
        self.number_of_guesses = number_of_guesses

    def process_guess(self, guess):
        guess = guess.lower().strip()

        if len(guess) > 1:
            print('You can only guess one letter at a time. Guess again.')
            return None

        if guess in self.guessed_letters:
            print(f'You have already guessed that letter, guess again. You have guessed:\n{self.guessed_letters}')
            return None

        if guess not in self.word:
            print('Incorrect guess.')
            self.guessed_letters += guess
            self.number_of_guesses -= 1
            return None

        if guess in self.word:
            print('Correct guess!')
            self.guessed_letters += guess
            return None

    def censor_word(self, word):
        censored_word = ''
        for letter in list(word):
            if letter in self.guessed_letters:
                censored_word += letter
            else:
                censored_word += '*'
        return censored_word

    def main(self):
        print('Starting your game of hangman!\n')
        while self.number_of_guesses > 0:
            print(f'{self.censor_word(self.word)}')
            guess = input(f'\n. Please enter your next guess: ')
            self.process_guess(guess)
            if '*' not in self.censor_word(self.word):
                print('Congratulations you win! The word was', self.word)
                break

        if self.number_of_guesses == 0:
            print('You lose the word was', self.word)


if __name__ == '__main__':
    h = Hangman()
    h.main()
