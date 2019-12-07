from collections import namedtuple
import random


class Hangman():
   # Constants
   BODY_SIZE = 9
   WORD_LIST_SIZE = 100
   ALPHA_SIZE = 26
   # Named tuples to hold immutible data.
   BodyPart = namedtuple(
       'BodyPart', ['first', 'second', 'third', 'display_two', 'display_three'])
   WordInfo = namedtuple('WordInfo', ['word', 'is_available'])
   AlphaInfo = namedtuple('AlphaInfo', ['letter', 'is_available'])

   # Class properties
   body = []
   words = []
   alphabet = []
   game_over = False
   game_won = False
   games_won = 0
   games_lost = 0
   num_words_read = 0
   num_words_available = 0
   current_word = ""

   def __init__(self):
      # Here I'm creating the body array.
      # for each line I'm creating a new BodyPart namedtuple.
      # The first position holds the characters to be displayed the first time
      # this line is shown.
      # Second position holds characters to display the second time.
      # Third position holds characters to be displayed third.
      # Fourth position is a boolean to tell us if we should display the second position
      # Fifth position is a boolean to tell us if we should display the third position.
      # Only one of the first three positions should be displayed, the first position
      # should be displayed by default.
      self.body.append(self.BodyPart("   ----", None, None, False, False))
      self.body.append(self.BodyPart("   |  |", None, None, False, False))
      self.body.append(self.BodyPart("      |", "   O  |", None, False, False))
      self.body.append(self.BodyPart("      |", "   |  |", None, False, False))
      self.body.append(self.BodyPart("      |", "  -|  |", "  -|- |", False, False))
      self.body.append(self.BodyPart("      |", "   |  |", None, False, False))
      self.body.append(self.BodyPart("      |", "  /   |", "  /\\ |", False, False))
      self.body.append(self.BodyPart("      |", None, None, False, False))
      self.body.append(self.BodyPart("______|__\n", None, None, False, False))
      # Initialize the alphabet.
      alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      for l in alpha:
          self.alphabet.append(self.AlphaInfo(l, True))

   def initialize_file(self, filename):
      """Initializes the word data structure from the file."""
      with open(filename, 'r') as fhandle:
         data = fhandle.read().split('\n')
         for w in data:
            word = self.WordInfo(w, True) # Create the word object
            self.words.append(word)
            self.num_words_read += 1
      
      self.num_words_available = self.num_words_read

   def display_statistics(self):
      """Displays the game statistics."""
      print("Games won: {}".format(self.games_won))
      print("Games lost: {}".format(self.games_lost))
      print("Total words read: {}".format(self.num_words_read))
      print("Words left: {}".format(self.num_words_available))
    
   def new_word(self):      
      """Selects a random word from the words data structure"""
      # Generate a random number within the size of words[], and then check if that word
      # is still available.
      num = random.randint(0, self.num_words_read - 1)
      while not self.words[num].is_available:
         num = random.randint(0, self.num_words_read - 1)

      self.current_word = self.words[num].word 
      self.words[num] = self.words[num]._replace(is_available=False)
      self.num_words_available -= 1

      # We're starting a new round, so we need to reset display_two and display_three
      for i in range(len(self.body)):
         self.body[i] = self.body[i]._replace(display_two=False, display_three=False)

      # Last, we need to re-initialize the alphabet, I'll do one, you'll, again, need
      # some sort of loop to get all the letters.
      for i in range(len(self.alphabet)):
         self.alphabet[i] = self.alphabet[i]._replace(is_available=True)
      

   def display_game(self):
      """Display method displays the game."""
      # HINT: This uses loops and logic gates.
      for b in self.body:
         if b.display_three and b.third is not None:
            print(b.third)
         elif b.display_two and b.second is not None:
            print(b.second)
         else:
            print(b.first)      

      # Now we print out the word letter by letter. If the letter has been
      # guessed (or is_available is set to False) you display the letter. Otherwise,
      # display "_"
      # Display the current word here. No line breaks between letters.
      out = ""
      for l in self.current_word:
         for a in self.alphabet:
            if l == a.letter:
               if not a.is_available:
                  out += l # display the letter
               else:
                  out += "_"
         out += " "
      print(out)

      # Finally, display all the letters in the alphabet. If the letter is available,
      # then you should display it. Otherwise, you should display a blank space.
      # Display the alphabet here:
      out = ""
      for a in self.alphabet:
         if a.is_available:
            out += a.letter 
         else:
            out += " "
      print(out)

   def guess(self, let):
      """Guess is how the game play works. Notice, the UI is not part of this method.
      We leave that to the main.py file."""
      # Check if the user has guessed the letter (ie. is_available is set to false)
      # If it's not available, tell the user they guessed it already and return false.
      for i in range(len(self.alphabet)):
         if self.alphabet[i].letter == let:
            if not self.alphabet[i].is_available:
               return False 
            else:
               # update the alphabet lists to set the letter's is_available to false.
               self.alphabet[i] = self.alphabet[i]._replace(is_available=False) 
      
      # Check if letter is in the word
      if let in self.current_word:
         # Check if the whole word has been guessed (all the letters in the word are
         # not available) 
         self.game_won = True # Assume all letters have been guessed
         for i in self.current_word: 
            for a in self.alphabet:
               if a.letter == i and a.is_available:
                  # If one letter has not been guessed, set back to false
                  self.game_won = False
         if self.game_won:
            self.game_over = True
            self.games_won += 1    
      else:
         # if the letter isn't in the word, set the next appropriate element in the
         # body list displays to display.
         if self.body[6].display_two:
            # if the whole body is displayed, set game_over to true.
            self.body[6] = self.body[6]._replace(display_three=True)
            self.game_over = True
            self.games_lost += 1
         elif self.body[5].display_two:
            self.body[6] = self.body[6]._replace(display_two=True)
         elif self.body[4].display_three:
            self.body[5] = self.body[5]._replace(display_two=True)
         elif self.body[4].display_two:
            self.body[4] = self.body[4]._replace(display_three=True)
         elif self.body[3].display_two:
            self.body[4] = self.body[4]._replace(display_two=True)
         elif self.body[2].display_two:
            self.body[3] = self.body[3]._replace(display_two=True)
         else:
            self.body[2] = self.body[2]._replace(display_two=True)
      return True

   def reveal_word(self):
      """Reveals the word."""
      print("The current word is: {}".format(self.current_word))