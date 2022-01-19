import random

rps = "rock", "paper", "scissor"

randomBot = random.choices(rps)
print(randomBot)

user = input("Rock/Paper/Scissor? ")
