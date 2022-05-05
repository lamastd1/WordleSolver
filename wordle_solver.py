# program to solve wordle

# ensures that the word is a valid word
valid_word = 0

while (valid_word == 0):

  # tell the user to enter a word
  wordle_word = input("Enter a five letter word: ")
  wordle_word = wordle_word.upper()

  # open the list of all possible wordle words
  wordleDic = open('wordle_words.txt', 'r')

  # loop through each word in the set of all possible wordle words and see if the word is allowed
  for line in wordleDic.readlines():
    line = line.strip()
    if (wordle_word == line):
      valid_word = 1
      break


# due to information theory, the first word to guess is always CRANE
guess = "CRANE"

# - denotes the character is correct in the right place
# + denotes the character is correct in the wrong place
# x denotes the character is incorrect

# string to handle current user progress
output_string = ""

#calculate how many guesses you have
guess_count = 1

while (wordle_word != guess):

  # show the user what there current output is
  print("Guess " + str(guess_count) + ": " + guess)

  for i in range(0, 5):

    # check if the character is in the substring
    if guess[i] in wordle_word:
      
      # check if the character is in the right position
      if (guess[i] == wordle_word[i]):

        # character is in the right place so it recieves a -
        output_string += "-"
      
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


  # clear the user's old guess
  guess = ""

  # have the user enter a new guess
  while (len(guess) != 5):

    # have the user input their next guess
    guess = input("Enter your next guess, must be five letters: ")

    # convert guess to upper to make it easier to compare strings
    guess = guess.upper()



  # clear the output score
  output_string = ""
        


