
import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)
    Returns a word from word_list at random
    """
    return random.choice(word_list)




#SUBMISSION OF THE FIRST ONE!
# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for letter in secret_word:
      if letter in letters_guessed:
        count += 1
    if count == len(secret_word):
      return True
    else:
      return False
pass
 


### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    output_string = ''
    for letters in secret_word:
      if letters in letters_guessed:
        output_string += letters
      else:
        output_string += '_'
    return output_string
    pass
    
    
    
      
#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    # FILL IN YOUR CODE HERE... 
  import string
  lowercase = string.ascii_lowercase
  for letters in letters_guessed:
    if letters in lowercase:
      lowercase = lowercase.replace(letters, '')
  return lowercase
pass



#Testcases 
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )



def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print("Let's start the game")
    print('Thinking of a word with', len(secret_word) ,'letters')
    numberofchance = 8
    letters_guessed = []
    

    while is_word_guessed(secret_word, letters_guessed) == False:  
      letterinput = input('Input a letter:')
      
      letters_guessed.append(letterinput)
      
      if letterinput in secret_word:
        print('Correct, you have', numberofchance, 'left')
        print(get_guessed_word(secret_word,letters_guessed))
        print('Letters available:', get_available_letters(letters_guessed))
      else:
        print('Wrong, you have', (numberofchance-1), 'gueses left')
        print(get_guessed_word(secret_word,letters_guessed))
        print('Letters available:', get_available_letters(letters_guessed))
        numberofchance-=1
        
      #if letterinput in secret_word:
        #print('You have guessed correctly:', get_guessed_word(secret_word, letterinput))
      #else:
        #print('Wrong, try again', get_guessed_word(secret_word,letterinput))
        #print(numberofchance-1,'chances left')
      if numberofchance == 0:
        break
      print("")
      #print('Correct guesses so far:', get_guessed_word(secret_word, letters_guessed.append(letterinput)))
    if is_word_guessed(secret_word, letters_guessed) == True:
      print('Win')
    else:
      print('lost, the word was:', secret_word)

      pass


def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()


   