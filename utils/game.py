from random import randint
import re
from typing import NoReturn, List


class Hangman:
    """
    Hangman is a game where you must find a hidden word in a certain number of tries (5 by default).
    Use start_game() to play
    """
    def __init__(self) -> NoReturn:
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions', 'papers', 'hangman']
        # Takes a random word form self.possible_words. Using randint function
        self.word_to_find: str = self.possible_words[randint(0, len(self.possible_words) - 1)]
        self.lives: int = 5
        # Generate list with empty guesses
        self.correctly_guessed_letters: List[str] = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def _play(self) -> NoReturn:
        """
        This method prompts the user to guess a letter, then checks if the guess is correct or not
        Asks again until the prompt format is respected
        """
        guess: str = ''
        regex = re.compile(r'^[a-zA-Z]$')
        # Asks user input until it is well formated (single letter)
        while not regex.match(guess):
            guess = input('Guess a letter : ')
            guess = guess.lower()
        if guess in self.word_to_find \
                and guess not in self.correctly_guessed_letters:
            for index, value in enumerate(self.word_to_find):
                if guess == value:
                    self.correctly_guessed_letters[index] = guess
        # Do not remove lives if player guesses the same letter twice
        elif guess in self.correctly_guessed_letters \
                or guess in self.wrongly_guessed_letters:
            print(f'You already guessed {guess.upper()}')
        else:
            self.error_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(guess)
        self.turn_count += 1
        print(f'Lives: {self.lives}\n\
Word: {" ".join(self.correctly_guessed_letters)}\n\
Misses: {", ".join(self.wrongly_guessed_letters)}\n')

    def _well_played(self) -> NoReturn:
        """
        This method sends a message when you finished (and won) the game
        """
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} error(s)!')

    def _game_over(self) -> NoReturn:
        """
        This method sends a message when you are game over
        """
        print('game over...')

    def start_game(self) -> NoReturn:
        """
        This method is the game main loop. Calls play() evert turn, and checks if game is won or lost
        """
        while self.lives > 0 and '_' in self.correctly_guessed_letters:
            self._play()
        if '_' not in self.correctly_guessed_letters:
            self._well_played()
        else:
            self._game_over()
