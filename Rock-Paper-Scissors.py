import random

print("----------------------")
print("Rock - Paper - Scissor")
print("----------------------")
a = 0
b = 0
c = 0
while c < 3:
    d = input("Enter response: ")
    while d != "rock" and d!= "paper" and d != "scissor":
        d = input("Enter valid response: ")
    e = random.randint(1,3)
    if d == "rock" and e == 1:
        c +=1
        print("Computer is rock. You are rock. You tie.")
    elif d == "rock" and e == 2:
        c +=1
        b +=1
        print("Computer is paper. You are rock. You lose.")
    elif d == "rock" and e == 3:
        c +=1
        a +=1
        print("Computer is scissor. You are rock. You win")
    elif d == "paper" and e == 1:
        c +=1
        a +=1
        print("Computer is rock. You are paper. You win")
    elif d == "paper" and e == 2:
        c +=1
        print("Computer is paper. You are paper. You tie.")
    elif d == "paper" and e == 3:
        c +=1
        b +=1
        print("Computer is scissor. You are paper. You lose.")
    elif d == "scissor" and e == 1:
        c +=1
        b+= 1
        print("Computer is rock. You are scissor. You lose.")
    elif d == "scissor" and e == 2:
        c +=1
        a +=1
        print("Computer is paper. You are scissor. You win")
    elif d == "scissor" and e == 3:
        c +=1
        print("Computer is scissor. You are scissor. You tie.")
if a > b:
    print("GAME OVER - YOU WIN")
elif b >a:
    print("GAME OVER - COMPUTER WINS")
elif b == a:
    print("GAME OVER - IT'S A TIE")