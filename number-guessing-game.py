import random
def game():
  rand = randint(1,100)
  print("Welcome to the Number Guessing Game!\nI am thinking of a random whole number between 1 and 100 (inclusive).\nIn order to win the game, you must guess the number in a certain amount of tries. Said amount is determined by the difficulty that you choose.\n\nChoose your difficulty:\n1 - Easy (10 chances)\n2 - Medium (5 chances)\n3 - Hard (3 chances)")
  diff = input("Enter the number of your chosen difficulty: ")
  print("\nGood luck!")
  if diff == "1":
    ci = 10
  elif diff == "2":
    ci == 5
  elif diff == "3":
    ci == 3
  for a in range(ci):
    lose = True
    g = input("Enter you guess:")
    if g.isdigit():
      if g < rand:
        less = "less"
      else:
        less = "more"
      if int(g) == rand:
        print("Congrats! You guessed the number in", a+1, "tries!")
        if not high:
          high = a + 1
        else:
          if high > a + 1:
            high = a + 1
            print("New high score!", high, "tries")
        lose = False
        break
      else:
        print("Incorrect! The number is" + less + "than" + str(g) + ". " + str(a - 1 + ci) + " tries remaining")
    else:
      print("Non-integer input received.", a - 1 + ci, "tries remaining.")
  if lose == True:
    print("You lose! Better luck next time.")
  while rand:
    ret = input("Do you want to play again? (Y/N): ")
    if ret == "Y":
      game()
    elif ret == "N":
      ret = "N"
      break
    else:
      print("Invalid answer.") 
