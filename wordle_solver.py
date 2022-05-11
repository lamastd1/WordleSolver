# program to solve wordle

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
  wordle_word = input("Enter a five letter word: ")
  wordle_word = wordle_word.upper()

  # ensures that the word is a valid word
  valid_word = 0

  while (valid_word == 0):

    # open the list of all possible wordle words
    wordleDic = open('wordle_guesses.txt', 'r')

    # loop through each word in the set of all possible wordle words and see if the word is allowed
    for line in wordleDic.readlines():
      line = line.strip()
      line = line.upper()
      if (wordle_word == line):
        valid_word = 1
        return wordle_word
    
    # tell the user to enter a word
    validate_guess(guesses)
  
# plays the game 
def play_game(wordle_word, guesses):

  # choose what method is being played
  mode = input("Do you want to play wordle or use calculator \n0: play wordle \n1: calculator\n")

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
  while (wordle_word != guess):

    # if the user is using a calculator
    if (mode == 1):

      # due to information theory, the first word to guess is always CRANE
      guess = "CRANE"

    # if the user is playing regular wordle
    else:

      # have the user enter a new guess
      #while (len(guess) != 5):

        # have the user input their next guess
        #guess = input("Enter your next guess, must be five letters: ")

        # convert guess to upper to make it easier to compare strings
        #guess = guess.upper()
      guess = validate_guess(guesses)

    # show the user what there current output is
    print("Guess " + str(guess_count) + ": " + guess)

    # loop through each character of the guess and the wordle word at the same time
    for i in range(0, 5):

      # check if the character is in the substring
      if guess[i] in wordle_word:
        
        # check if the character is in the right position
        if (guess[i] == wordle_word[i]):

          # character is in the right place so it recieves a -
          output_string += "-"
        
        # character is in the wrong place
        else:

          # character is in the right place so it recieves a -
          output_string += "+"
      
      # character is in the wrong place
      else:

        # character is in the wrong place so it recieves a x
        output_string += "x"

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

      print("mode: ")
      print(mode)
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
  wordle_word = validate_guess(guesses)
  
  # play the game
  play_game(wordle_word, guesses)
