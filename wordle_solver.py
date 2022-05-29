# program to solve wordle

import re

class Word:

  # creates the word classes
  def __init__(self, word, possible):

    self.word = word
    self.possible = possible
    self.entropy = 0

  # function used to return entropy of a particular word
  def find_entropy(s):
    if (s.possible):
      s.entropy += 1

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
    for i in range(0, 5):
      if (len(re.findall(line[i], line)) > 2):
        print(line)
        break

    guess = Word(line, False) 
    guesses.append(guess)

  # close the guesses file
  wordleDic.close()

# add if each word is a possible answer
def append_answers(guesses):

  # open the list of all possible answers
  wordleAnswers = open('wordle_answers.txt', 'r')

  # check if a word is possible to be a valid answer
  for line in wordleAnswers.readlines():
    line = line.strip()
    line = line.upper()
    binary_search(line, guesses)

# allow the user to enter a correct guess
def validate_guess(guesses):

  # tell the user to enter a word
  solution = input("Enter a five letter word: ")
  solution = solution.upper()

  # ensures that the word is a valid word
  valid_word = 0

  while (valid_word == 0):

    # open the list of all possible wordle words
    wordleDic = open('wordle_guesses.txt', 'r')

    # loop through each word in the set of all possible wordle words and see if the word is allowed
    for line in wordleDic.readlines():
      line = line.strip()
      line = line.upper()
      if (solution == line):
        valid_word = 1
        return solution
    
    # tell the user to enter a word
    validate_guess(guesses)
  
# plays the game 
def play_game(solution, guesses):

  # choose what method is being played
  mode = int(input("Do you want to play wordle or use calculator \n0: play wordle \n1: calculator\n"))

  # - denotes the character is correct in the right place
  # + denotes the character is correct in the wrong place
  # x denotes the character is incorrect

  # define what the user's guess will be 
  guess = ""

  # string to handle current user progress
  output_string = ""

  #calculate how many guesses you have
  guess_count = 1

  # loop until the guess is correct 
  while (solution != guess):

    # if the user is using a calculator
    if (mode == 1):

      # due to information theory, the first word to guess is always CRANE
      guess = "CRANE"

    # if the user is playing regular wordle
    else:
      guess = validate_guess(guesses)

      # have the user enter a new guess
      #while (len(guess) != 5):

        # have the user input their next guess
        #guess = input("Enter your next guess, must be five letters: ")

        # convert guess to upper to make it easier to compare strings
        #guess = guess.upper()

    # show the user what there current output is
    print("Guess " + str(guess_count) + ": " + guess)

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
      elif count_guess == 1 or count_guess == count_solution:
        
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

          if (guess[j] == solution[j]) or (guess[j] == guess[i] and j < i and len(output_string) > j and output_string[j] == "+"):

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

        print("------------BEGIN OF DEBUG AREA------------")
        print (guess + " " + guess[i])
        print(solution + " " + solution[i])
        print("i: " + str(i))
        print("count_guess: " + str(count_guess))
        print("count_solution: " + str(count_solution))
        print("this is where more instances in the guess will be handled")
        print("-------------END OF DEBUG AREA-------------")
      
      else:

        print("------------BEGIN OF DEBUG AREA------------")
        print (guess + " " + guess[i])
        print(solution + " " + solution[i])
        print("i: " + str(i))
        print("count_guess: " + str(count_guess))
        print("count_solution: " + str(count_solution))
        print("this is where more instances in the solution will be handled")
        print("-------------END OF DEBUG AREA-------------")

    # give the user a menu showing their total
    print("--------------------------------------------------")
    print("USER GUESS:   " + guess)
    print("OUTPUT SCORE: " + output_string)
    print("--------------------------------------------------")

    # check to see if the game was finished
    if (output_string == "-----"):

      print ("Congrats, you beat the game!")
      break 

    else:

      if (mode == 1):
        print("mode 1")
        print()

    # clear the user's old guess
    guess = ""

    # clear the output score
    output_string = ""

if __name__ == "__main__":

  # create a list to hold all possible guesses
  guesses = []
  
  # append each word to the wordlist 
  append_wordlist(guesses)

  # determine if each word is an answer or not
  append_answers(guesses)

  # recieve a valid guess from user
  solution = validate_guess(guesses)
  
  # play the game
  play_game(solution, guesses)
