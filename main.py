#this imports the Hangman class
from Hangman import Hangman
#welcomes the user to the game 
print("Welcome to Hangman!\n")
#prompts the user if they would like to play
play = input("Would you like to play a game? (y/N) ")
#if the player enters anything other than lower case y, the game quits
if play.lower() != "y":
   print("Maybe later! Goodbye!")
   exit()
#continue with the game if the player enters "y"  
play_again = True
#the Hangman function is assigned to the variable game
game = Hangman()
#this calls on Hangman to initialize the file that contains the words
game.initialize_file('words.dat')
#this will play the game until the guesses run out AND there are still words to guess 
while play_again and game.num_words_available > 0:
   print("Starting game.")
#this prints the current word, games won and games lost 
   game.display_statistics()
#this prints a new line   
   print("\n")
#the game picks a new word   
   game.new_word()
#if the user continues the game will display a new gameboard   
   while not game.game_over:
      game.display_game()
#this prompts the user to guess a letter      
      user_guess = input("Enter a letter to guess. ")
#if the user doesn't enter an alphabetical letter then the game will catch that      
      if not user_guess.isalpha():
         print("Sorry, I don't understand. That's not a letter. \n")
#if the user enters the same letter the game will catch it      
      elif not game.guess(user_guess.upper()):
         print("Sorry, you've alread guessed that letter. \n")
#this reveals the word the game picked    
   game.reveal_word()
#this displays the updated game stats
   game.display_statistics()
#this will set the end of the game to false
   game.game_over = False
#this will prompt the player if the want to play again
   again = input("Would you like to play again? (y/N)")
#if the player doesn't enter y play again will be false and game will end  
   if again.lower() != "y":
      play_again = False
#this thanks the user for playing and exits the game   
print("Thanks for playing! Goodbye!")
exit()