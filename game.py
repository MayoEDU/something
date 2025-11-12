import random
list = [1, 2, 3]
roll = random.choice(list)
result = " "
if (roll == 1):
    result = "Rock"
elif (roll == 2):
    result = "Paper"
elif (roll == 3):
    result = "Scissors"
print("Welcome to Rock-Paper-Scissors!")
print(f"Computer Chose {result}")