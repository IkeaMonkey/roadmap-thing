import random
def game(high):
  rand = random.randint(1,100)
  print("Welcome to the Number Guessing Game!\nI am thinking of a random whole number between 1 and 100 (inclusive).\nIn order to win the game, you must guess the number in a certain amount of tries. Said amount is determined by the difficulty that you choose.\n\nChoose your difficulty:\n1 - Easy (10 chances)\n2 - Medium (5 chances)\n3 - Hard (3 chances)")
  while True:
    diff = input("Enter the number of your chosen difficulty: ")
    if diff == "1":
        ci = 10
        break
    elif diff == "2":
        ci == 5
        break
    elif diff == "3":
        ci == 3
        break
    else:
        print("Invalid input")
  print("\nGood luck!")
  for a in range(ci):
    lose = True
    g = input("Enter you guess:")
    if g.isdigit():
      if int(g) > rand:
        less = "less"
      else:
        less = "more"
      if int(g) == rand:
        print("Congrats! You guessed the number in", a+1, "tries!")
        if high > a + 1:
            high = a + 1
            print("New high score!", high, "tries")
        lose = False
        break
      else:
        print("Incorrect! The number is " + less + " than " + str(g) + ". " + str(ci - a - 1) + " tries remaining")
    else:
      print("Non-integer input received.",ci - a - 1, "tries remaining.")
  if lose == True:
    print("You lose! Better luck next time.")
  while rand:
    ret = input("Do you want to play again? (Y/N): ")
    if ret == "Y":
      game(high)
    elif ret == "N":
      ret = "N"
      rand = False
    else:
      print("Invalid answer.") 
game(11)