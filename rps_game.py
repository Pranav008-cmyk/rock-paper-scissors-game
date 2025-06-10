from playsound import playsound
import random
print("Rock Paper Scissor GAME")
a=input("Enter you Name:")
print("Let's Start")
p=0
c=0
n=int(input("How many rounds or best of how much?:"))
for i in range(n):
    player_choice=input("Enter you Choice(Rock/Paper/Scissor):").capitalize()
    print("Your choice is",player_choice)
    options=["Rock","Paper","Scissor"]
    comp_choice=random.choice(options)
    print("Computer choice is",comp_choice)
    print("Score:",a,"COMPUTER")
    if (player_choice=="Rock" and comp_choice=="Scissor") or (player_choice=="Scissor" and comp_choice=="Paper") or (player_choice=="Paper" and comp_choice=="Rock"):
        p+=1
        print("SCORE:",p,c)
    elif (player_choice==comp_choice):
        print("OH! Same choice")
        print("Score:", a, p, "| COMPUTER", c)
    else:
        c+=1
        print("Score:", a, p, "| COMPUTER", c)
if p>c:
    print(f"\nFINAL SCORE:\n{a}: {p}  |  COMPUTER: {c}")
    print("YOU WIN!!")
    playsound("win.mp3")
elif p==c:
    print(f"\nFINAL SCORE:\n{a}: {p}  |  COMPUTER: {c}")
    print("You are really competitive to computer's brain")
    playsound("draw.mp3")
else:
    print(f"\nFINAL SCORE:\n{a}: {p}  |  COMPUTER: {c}")
    print("Sorry! Better luck next time")
    playsound("lose.mp3")
