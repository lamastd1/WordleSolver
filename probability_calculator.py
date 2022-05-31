# program to solve wordle

import re
import random

class Word:

  # creates the word classes
  def __init__(self, word, possible):

    self.word = word
    self.possible = possible
    self.entropy = 0

  # function used to return entropy of a particular word
  def find_entropy(self):
    if (self.possible):
      self.entropy += 1

# helper method algorithim to quicksort an array
def quick_sort():
  pass

# helper method binary search technique to find words in the array
def binary_search(line, guesses):
  pass

# helper method to print the array
def print_words():      
  pass

# append the possible words to the guesses wordlist 
def append_wordlist(guesses):

  # open the list of all possible wordle words
  wordleDic = open('wordle_guesses.txt', 'r')

  # reads in all the data from the guesses file to be stored into an array
  for line in wordleDic.readlines():
    line = line.strip()
    line = line.upper()

    guess = Word(line, False) 
    guesses.append(guess)

  # close the guesses file
  wordleDic.close()

# add if each word is a possible answer
def append_answers(answers):

  # open the list of all possible answers
  wordleAnswers = open('wordle_answers.txt', 'r')

  # check if a word is possible to be a valid answer
  for line in wordleAnswers.readlines():
    line = line.strip()
    line = line.upper()

    answer = Word(line, True)
    answer.find_entropy() 
    answers.append(answer)
    
if __name__ == "__main__":

  # create a list to hold all possible guesses
  guesses = []
  answers = []
  
  # append each word to the wordlist 
  append_wordlist(guesses)

  # determine if each word is an answer or not
  append_answers(answers)

  # recieve a valid guess from user
  solution_obj = random.choice(answers)
  solution = solution_obj.word

  #for i in range(0, len(answers)):
   #print(answers[i].word + " " + str(answers[i].possible))
  
  # find the optimal solution
  #find_optimal_guess(guesses, answers)
  