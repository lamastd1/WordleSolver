# program to take all the five letter words out of a dictionary used for wordle
# https://puzzling.stackexchange.com/questions/114419/what-dictionary-is-wordle-based-on#:~:text=My%20conclusion%20is%20that%20the,and%20for%20its%20match%20wordlist.

# opens the files used
totalDic = open('CSW19.txt') 
wordleDic = open('wordle_words.txt', 'a')

# loop through every word in the dictionary
for line in totalDic.readlines():

  # remove unwanted characters in the string
  line = line.strip() 

  # check if the string is usable for wordle
  if ((line.isalpha() == True) and (len(line) == 5)):

    # add the word to the dictionary of usable wordle words
    print(line)
    wordleDic.write(line + "\n")

# close the files
totalDic.close()
wordleDic.close()

