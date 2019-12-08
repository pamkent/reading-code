#this imports the Hangman
from Hangman import Hangman
#welcomes the user to the game 
print("Welcome to Hangman!\n")
#prompts the user if they would like to play
play = input("Would you like to play a game? (y/N) ")
#if the player does not enter anything equal to "y" then exit the game
if play.lower() != "y":
   print("Maybe later! Goodbye!")
   exit()
#continue with the game if the player enters "y"   
play_again = True
#the Hangman function is assigned to  a variable game
game = Hangman()
#this calls on Hangman to initialize the file that contains the words
game.initialize_file('words.dat')
#this will play the game until the guesses run out AND there are still words to guess 
while play_again and game.num_words_available > 0:
   print("Starting game.")
#this prints the current word, games won and games lost 
   game.display_statistics()
   print("\n")
#the game will pick a new word to guess  
   game.new_word()
#if the user would 
   while not game.game_over:
      game.display_game()
      user_guess = input("Enter a letter to guess. ")
      if not user_guess.isalpha():
         print("Sorry, I don't understand. That's not a letter. \n")
      elif not game.guess(user_guess.upper()):
         print("Sorry, you've alread guessed that letter. \n")
#this will reveal the word that the game picked          
   game.reveal_word()
#   
   game.display_statistics()
#   
   game.game_over = False
#   
   again = input("Would you like to play again? (y/N)")
   if again.lower() != "y":
      play_again = False
   
print("Thanks for playing! Goodbye!")
exit()
