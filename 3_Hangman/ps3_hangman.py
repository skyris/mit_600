# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
      """
      Returns a list of valid words. Words are strings of lowercase letters.
      
      Depending on the size of the word list, this function may
      take a while to finish.
      """
      print("Loading word list from file...")
      # inFile: file
      inFile = open(WORDLIST_FILENAME, 'r')
      # line: string
      line = inFile.readline()
      # wordlist: list of strings
      wordlist = line.split()
      print("  ", len(wordlist), "words loaded.")
      return wordlist

def choose_word(wordlist):
      """
      wordlist (list): list of words (strings)

      Returns a word from wordlist at random
      """
      return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secretWord, lettersGuessed):
      '''
      secretWord: string, the word the user is guessing
      lettersGuessed: list, what letters have been guessed so far
      returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
      '''
      # Code using sets
      # setSecretWord = set(secretWord)
      # setGuessed = set(lettersGuessed)
      # return setSecretWord == set.intersection(setSecretWord, setGuessed)
      # return setSecretWord == setSecretWord & setGuessed

      secretWord = double_del(secretWord)
      lettersGuessed = double_del(lettersGuessed)
      for i in secretWord:
            if i not in lettersGuessed:
                  return False
      return True


def double_del(iterable):
      nondouble = []
      for i in iterable:
           if i not in nondouble:
                 nondouble.append(i)
      return nondouble 


def get_guessed_word(secretWord, lettersGuessed):
      '''
      secretWord: string, the word the user is guessing
      lettersGuessed: list, what letters have been guessed so far
      returns: string, comprised of letters and underscores that represents
        what letters in secretWord have been guessed so far.
      '''
      # FILL IN YOUR CODE HERE...
      secretWord_copy = secretWord[:]
      for letter in secretWord:
            if letter not in lettersGuessed:
                  secretWord_copy = secretWord_copy.replace(letter, "_ ")
      return secretWord_copy
          


def get_available_letters(lettersGuessed):
      '''
      lettersGuessed: list, what letters have been guessed so far
      returns: string, comprised of letters that represents what letters have not
            yet been guessed.
      '''
      # FILL IN YOUR CODE HERE...
      ascii_string = string.ascii_lowercase
      ascii_list = list(ascii_string)
      for symbol in ascii_string:
            if symbol in lettersGuessed:
                  ascii_list.remove(symbol)
      return "".join(ascii_list)
    

def hangman(secretWord):
      '''
      secretWord: string, the secret word to guess.

      Starts up an interactive game of Hangman.

      * At the start of the game, let the user know how many 
        letters the secretWord contains.

      * Ask the user to supply one guess (i.e. letter) per round.

      * The user should receive feedback immediately after each guess 
        about whether their guess appears in the computers word.

      * After each round, you should also display to the user the 
        partially guessed word so far, as well as letters that the 
        user has not yet guessed.

      Follows the other limitations detailed in the problem write-up.
      '''

      print("Welcome to the game, Hangman!")
      print("I am thinking of a word that is %s letters long." % len(secretWord))
      numGuesses = 8
      lettersGuessed = []
      while numGuesses > 0:
            print("-------------")
            print("You have %s guesses left." % numGuesses)
            print("Available letters: %s" % get_available_letters(lettersGuessed))
            new_letter = input("Please guess a letter: ")
            if new_letter in lettersGuessed:
                  print("Oops! You've already guessed that letter: %s" % get_guessed_word(secretWord, lettersGuessed))
            else:
                  lettersGuessed.append(new_letter)
                  if new_letter in secretWord:
                        print("Good guess: %s" % get_guessed_word(secretWord, lettersGuessed))
                  else:
                        print("Oops! That letter is not in my word: %s" % get_guessed_word(secretWord, lettersGuessed))
                        numGuesses -= 1
            if is_word_guessed(secretWord, lettersGuessed):
                  print("-------------")
                  print("Congratulations, you won!")
                  break

      if numGuesses == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was %s." % secretWord)


secretWord = choose_word(wordlist).lower()
hangman(secretWord)
