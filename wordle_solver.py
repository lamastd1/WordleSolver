# program to solve wordle

import re
import random

class Word:

  # creates the word classes
  def __init__(self, word):

    self.word = word
    self.possible = True
    self.entropy = 0

  # function used to return entropy of a particular word
  def initilize_answer_entropy(self):
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

    guess = Word(line) 
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

    answer = Word(line) 
    answer.initilize_answer_entropy() 
    answers.append(answer)
    

# allow the user to enter a correct guess
def validate_guess(guesses):

  # tell the user to enter a word
  solution = ""
  solution = input("Enter a five letter word: ")
  solution = solution.upper()

  # ensures that the word is a valid word
  valid_word = 0

  # iterate over all the words to determine if the word is valid
  while (valid_word == 0):

    # loop through each word in the set of all possible wordle words and see if the word is allowed
    for guess in guesses:
      word = guess.word
      if (solution == word):
        valid_word = 1
        return solution
    
    # tell the user to enter a word
    return validate_guess(guesses)
  
def find_optimal_guess(guesses, answers, history):

  # used to change the ASCII to be used to index the array
  ASCII_CONVERTER = 65

  # hold the letters a-z and the 5 locations where each letter could be to count how often a letter appears in a certain position
  rows, cols = (26, 5)
  letter_frequencies_per_spot = [[0 for i in range(cols)] for j in range(rows)]
  letter_frequencies_total = [0 for i in range(rows)]
  letter_frequencies_wrong_place = [0 for i in range(rows)]
  letter_frequencies_not_seen = [0 for i in range(rows)]

  # loop through the answers to see where the location can be increased
  for i in range(0, len(guesses)):

    # keep track of what characters have already been seen
    seen_chars = [0 for i in range(rows)]
    for j in range(0, cols):
      found_char = ord(guesses[i].word[j]) - ASCII_CONVERTER
      letter_frequencies_per_spot[found_char][j] += 1
      letter_frequencies_total[found_char] += 1
      seen_chars[found_char] += 1
    
    for i in range(0, rows):
      if (seen_chars[i] == 0):
        letter_frequencies_not_seen[i] += 5
      else:
        letter_frequencies_wrong_place[i] += 5 - seen_chars[i]

  # keep track of letters that are already found
  found_letters = [0 for i in range(5)]

  # keep track of how many letters we know and how many we don't 

  # determine which letters are usable in certain locations
  for i in range(0, 26):
    for j in range(0, 5):
      if (history[i][j] == 3):
        found_letters[j] = i

  # determine which guesses are usable
  usable_guesses = []

  # find the words with the right letters if we have all 5
  for i in range(0, len(guesses)):
    usable = True
    if (guesses[i].possible == True):
      for j in range(0, 5):
        found_char = ord(guesses[i].word[j]) - ASCII_CONVERTER
        if (found_letters[j] != found_char and found_letters[j] != 0):
          if (guesses[i].word == "CURSE"):
            print("ACTUAL CHAR 1: " + guesses[i].word[j] + "\t " + str(j))
          guesses[i].possible = False
          usable = False
          break
        elif (history[found_char][j] == 1 or history[found_char][j] == 2):
          if (guesses[i].word == "CURSE"):
            print("ACTUAL CHAR 2: " + guesses[i].word[j] + "\t " + str(j))
          guesses[i].possible = False
          usable = False
          break

      if (usable == True):

        usable_guesses.append(guesses[i].word)
    
  # for i in range(0, len(guesses)):
  #   for j in range(0, 5):
  #     found_char = ord(guesses[i].word[j:j+1]) - ASCII_CONVERTER
  #     if (history[found_char][j] == 1):


  # to get the first guess, return a word that is most common in all 5 areas
  max = 0
  held_word = ""
  
  for i in range(0, len(usable_guesses)):
    sum = 0
    for j in range(0, 5):
      found_char = ord(usable_guesses[i][j]) - ASCII_CONVERTER
      sum += letter_frequencies_per_spot[found_char][j]
    if (sum > max):
      max = sum
      held_word = usable_guesses[i]

  # print("-------HELD WORD-------")
  # print(held_word)
  # print("-----END HELD WORD-----")
  # print("-------SOLUTION-------")
  # print(solution)
  # print("-----END SOLUTION-----")
  # print("-----USABLE GUESSES-----")
  # print(usable_guesses)
  # print("---END USABLE GUESSES---")
  # print()

  return held_word

def new_update_history(history, guess, output_string):
  
  # used to change the ASCII to be used to index the array
  ASCII_CONVERTER = 65

  for i in range(0, 5):

    found_char = ord(guess[i]) - ASCII_CONVERTER

    if (output_string[i] == "-"):
      history[found_char][i] = 3
    elif (output_string[i] == "+"):
      history[found_char][i] = 2
    else:
      if (history[found_char].count(2) == 0):
        for j in range(0, 5):
          history[found_char][j] = 1

  return history

def update_history(guess, solution, history):

  # used to change the ASCII to be used to index the array
  ASCII_CONVERTER = 65

  for i in range(0, 5):

    found_char = ord(guess[i]) - ASCII_CONVERTER

    # update the history
    # the letter does not appear in the solution
    if (solution.count(guess[i]) == 0):
                   
      for l in range(0, 5):
        history[found_char][l] = 1
        
    # the letter is in the right spot  
    elif (guess[i] == solution[i]):
        
        history[found_char][i] = 3
      
      # for l in range(0, 5):
      #   if (i != l and solution.count(guess[i]) == history[found_char].count(3) and history[found_char][l] != 3):
      #     #print("ACTUAL CHAR: " + guess[i] + "\t " + str(l))
      #     history[found_char][l] = 1
      #   else:
      #     if (i == l):
      #       history[found_char][l] = 3
      #     for m in range(0, 5):
      #       if history[found_char][m] > 3:
      #         history[found_char][m] -= 2

    # the letter is in the wrong spot  
    elif (guess[i] != solution[i]):

      history[found_char][i] = 2
      # already_solved = False
      # count = 0
      # for l in range(0, 5):
      #   if history[found_char][l] == 3:
      #     count += 1
      #     if (count == solution.count(guess[i])):
      #       already_solved = True
      #     break

      # for l in range(0, 5):
      #   if (history[found_char][l] == 3):
      #     pass
      #   elif (i != l and history[found_char][l] != 1 and already_solved == False):
      #     history[found_char][l] = (2 * guess.count(guess[i])) - (2 * history[found_char].count(3))
      #   else:
      #     history[found_char][l] = 1 

  return history 


  # this one does it by options left
  # for i in range(0, len(guesses)):
  #   seen_chars = [0 for ii in range(rows)]
  #   for j in range(0, 5):
  #     found_char_guess = ord(guesses[i].word[j:j+1]) - ASCII_CONVERTER
  #     seen_chars[found_char_guess] += 1

  #   for j in range(0, len(answers)):
  #     for k in range(0, 5):

  #       found_char_answer = ord(answers[j].word[k:k+1]) - ASCII_CONVERTER

  #       # the letter is not in the guess
  #       if (seen_chars[found_char_answer] == 0):
          
  #         for l in range(0, 5):
  #           history[found_char_answer][l] = 1

  #       # the letter is in the wrong spot
  #       elif (guesses[i].word[k:k+1] != answers[j].word[k:k+1]):
          
  #         history[found_char_answer][k] = 2
        
  #       # the letter is in the right spot
  #       else:

  #         history[found_char_answer][k] = 3



# plays the game 
def play_game(solution, guesses, answers, num):

  # collect the history of the game moves so far
  # a 0 in this array means that the letter's status is not known
  # a 1 in this array means that the letter is not in the word
  # a 2 in this array means that the letter is in the wrong place
  # a 3 in this array means that the letter is in the right place 
  rows, cols = (26, 5)
  history = [[0 for i in range(cols)] for j in range(rows)]

  # choose what method is being played
  #mode = int(input("Do you want to play wordle or use calculator \n0: play wordle \n1: calculator\n"))
  mode = num
  # - denotes the character is correct in the right place
  # + denotes the character is correct in the wrong place
  # x denotes the character is incorrect

  # define what the user's guess will be 
  guess = ""

  # string to handle current user progress
  output_string = ""

  #calculate how many guesses you have
  guess_count = 1

  error = False
  # loop until the guess is correct 
  while (solution != guess and guess_count < 100):

    if (guess_count == 99):
      error = True

    # if the user is using a calculator
    if (mode == 1):

      # find the optimal guess
      guess = find_optimal_guess(guesses, answers, history)
      #print("GUESS: " + guess)

    # if the user is playing regular wordle
    else:
      guess = validate_guess(guesses)

    # loop through each character of the guess and the wordle word at the same time
    for i in range(0, 5):

      # check if the character in the guess is in the wordle word and how often it appears
      count_solution = len(re.findall(guess[i], solution))
      
      # check how often the character appears in the guess
      count_guess = len(re.findall(guess[i], guess))

      # if a guess has a character repeat more than what is in the solution, count how many have already been handled
      count_mult = 0

      # the character from the guess is not in the solution
      if count_solution == 0:

        # character is not in the word so it recieves a x
        output_string += "x"

      # the character from the guess is in the word once
      elif count_guess == count_solution or (count_guess >= 1 and count_solution > count_guess):
        
        # check if the character is in the right position
        if (guess[i] == solution[i]):

          # character is in the right place so it recieves a -
          output_string += "-"
        
        # character is in the wrong place
        else:

          # character is in the wrong place so it recieves a +
          output_string += "+"
      
      # the character from the guess is in the word multiple times
      elif count_guess > count_solution:

        for j in range(0, 5):

          if (guess[j] == solution[j] and j == i) or (guess[j] == guess[i] and j < i and len(output_string) > j and output_string[j] == "+"):

            count_mult = count_mult + 1  
          
        # check if the character is in the right place
        if guess[i] == solution[i]:

          # assign a - to the output string
          output_string += "-"

        # check if every instance of the character has been hit and if the character is in the right spot
        elif count_mult < count_solution and guess[i] != solution[i]:

          # assign a + to the output string
          output_string += "+"

        else:
  
          # assign an x to the output string
          output_string += "x"

    history = new_update_history(history, guess, output_string)

    # give the user a menu showing their total
    print("--------------------------------------------------")
    print("USER GUESS: \t" + guess + "\t\t COUNT: " + str(guess_count))
    print("OUTPUT SCORE: \t" + output_string)
    print("--------------------------------------------------")

    # print("---------HISTORY---------")
    # for row in history:
    #   print(row)
    # print("-------END HISTORY-------")

    # increment the guess count for the user
    guess_count = guess_count + 1

    # check to see if the game was finished
    if (output_string == "-----"):

      print ("Congrats, you beat the game!")
      return error

    # clear the user's old guess
    guess = ""

    # clear the output score
    output_string = ""

if __name__ == "__main__":

  for i in range(0, 2315):
    # create a list to hold all possible guesses
    guesses = []
    answers = []
    
    # append each word to the wordlist 
    append_wordlist(guesses)

    # determine if each word is an answer or not
    append_answers(answers)
  
    #solution_obj = random.choice(answers)
    solution_obj = answers[i]
    solution = solution_obj.word
    print(solution)
  #solution = "CURSE"
  
    # play the game
    error = play_game(solution, guesses, answers, 1)
    if (error == True):
      break

  # guesses = []
  # answers = []

  # # append each word to the wordlist 
  # append_wordlist(guesses)

  # # determine if each word is an answer or not
  # append_answers(answers)

  # solution = "SISSY"
  # play_game(solution, guesses, answers, 1)
