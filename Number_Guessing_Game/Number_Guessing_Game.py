import random
Number = random.randint(1,10)
Run_Time = True

print("==========================================") 
print("🎯 NUMBER GUESSING GAME (Python)")
print("==========================================")
print("# Guess the correct number between 1 and 10")
print("------------------------------------------")

while Run_Time:
    Guess = int(input("Enter your guess:"))

    if Number == Guess:
       print("   CONGRATULATIONS! ")
       print("✅ You guessed the correct number!")
       Run_Time = False

    if Number < Guess :
        print("⬆️ Too high! Try again.")
        
    elif Number > Guess:
        print("⬇️ Too low! Try again.")
    
