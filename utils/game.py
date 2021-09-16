from random import randint
import re
from typing import List


class Hangman:
    """
    Hangman is a game where you must find a hidden word in a certain number of tries (5 by default).
    Use start_game() to play
    """
    def __init__(self) -> None:
        with open('./wordlist.txt', 'r') as io:
            wordlist = io.read()
            self.possible_words: List[str] = wordlist.split()
        # Takes a random word form self.possible_words. Using randint function
        self.word_to_find: str = self.possible_words[randint(0, len(self.possible_words) - 1)]
        self.lives: int = 5
        # Generate list with empty guesses
        self.correctly_guessed_letters: List[str] = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def _play(self) -> None:
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

    def _well_played(self) -> None:
        """
        This method sends a message when you finished (and won) the game
        """
        print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} error(s)!')

    def _game_over(self) -> None:
        """
        This method sends a message when you are game over
        """
        print(f'game over...\nThe word to guess was {self.word_to_find}')
        prompt = input('Play again (y or n)?')
        if prompt.lower() == 'y':
            self.reset()
            self.start_game()
    
    def reset(self) -> None:
        """
        Resets the game, removing the previously guessed word from the wordlist
        """
        # Remove previous word from wordlist
        self.possible_words.remove(self.word_to_find)
        self.word_to_find: str = self.possible_words[randint(0, len(self.possible_words) - 1)]
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = ['_'] * len(self.word_to_find)
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def start_game(self) -> None:
        """
        This method is the game main loop. Calls play() evert turn, and checks if game is won or lost
        """
        while self.lives > 0 and '_' in self.correctly_guessed_letters:
            self._play()
        if '_' not in self.correctly_guessed_letters:
            self._well_played()
        else:
            self._game_over()
