import random
Options = ["rock","paper","scissor"]
Running = True
while Running:
  Computer = random.choice(Options)
  player = None

  while player not in Options:
    player = input("Enter a choice (rock, paper, scissor): ").lower()

    if Computer == player:
      print("It's Tie !")
    elif Computer == "rock" and player == "paper":
      print("you win!")
    elif Computer == "paper" and player == "scissor":
      print("you win!")
    elif Computer == "scissor" and player == "rock":
      print("you win!")
    else:
      print("you lose !")
    if input("Play again? (y/n)") == "n":
     Running = False    


print("Thanks for playing!")

