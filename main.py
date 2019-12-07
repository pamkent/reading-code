from Hangman import Hangman
#welcomes the user to the game 
print("Welcome to Hangman!\n")
#prompts the user if they would like to play
play = input("Would you like to play a game? (y/N) ")
#
if play.lower() != "y":
   print("Maybe later! Goodbye!")
   exit()
play_again = True
game = Hangman()
game.initialize_file('words.dat')
while play_again and game.num_words_available > 0:
   print("Starting game.")
   game.display_statistics()
   print("\n")
   game.new_word()
   while not game.game_over:
      game.display_game()
      user_guess = input("Enter a letter to guess. ")
      if not user_guess.isalpha():
         print("Sorry, I don't understand. That's not a letter. \n")
      elif not game.guess(user_guess.upper()):
         print("Sorry, you've alread guessed that letter. \n")
   game.reveal_word()
   game.display_statistics()
   game.game_over = False
   again = input("Would you like to play again? (y/N)")
   if again.lower() != "y":
      play_again = False
   
print("Thanks for playing! Goodbye!")
exit()
