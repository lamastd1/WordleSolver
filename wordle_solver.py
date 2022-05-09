# program to solve wordle

# ensures that the word is a valid word
valid_word = 0

while (valid_word == 0):

  # tell the user to enter a word
  wordle_word = input("Enter a five letter word: ")
  wordle_word = wordle_word.upper()

  # open the list of all possible wordle words
  wordleDic = open('wordle_guesses.txt', 'r')

  # loop through each word in the set of all possible wordle words and see if the word is allowed
  for line in wordleDic.readlines():
    line = line.strip()
    if (wordle_word == line):
      valid_word = 1
      break

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
    while (len(guess) != 5):

      # have the user input their next guess
      guess = input("Enter your next guess, must be five letters: ")

      # convert guess to upper to make it easier to compare strings
      guess = guess.upper()

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

  # clear the user's old guess
  guess = ""

  # clear the output score
  output_string = ""
        


