print("Welcome to my gaming quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's start!")

score = 0

answer = input("What does FPS means in game genres? ")
if answer.lower() == "first person shooter":
    print("Phenomenal!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does RPG means? ")
if answer.lower() == "role play game":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What do you call Playstation/XBOX/Nintendo? ")
if answer.lower() == "game consoles" or "game console":
    print("Fabulous!")
    score+=1
    print("Score: "+str(score)+"/3")
else:
    print("Incorrect!")