import random 
hand={1:"Rock", 2:"Paper", 3:"Scissors"}
n=int(input("Enter number of rounds:"))
c=0
p=0
while n>0:
    player1=int(input("Player choose rock[1], paper[2], scissors[3]."))
    computer=random.randint(1,3)
    if player1==1 and computer==2:
        print("Computer chooses:",hand[computer])
        print("---------------------------------")
        print("Computer wins this round.")
        c+=1
    elif player1==1 and computer==1:
        print("Computer chooses:",hand[computer])
        print("---------------------------------")
        print("Draw!")
    elif player1==1 and computer==3:
        print("Computer chooses:",hand[computer])
        print("---------------------------------")
        print("You win this round.")
        p+=1
    elif player1==2 and computer==1:
        print("Computer chooses:",hand[computer])
        print("---------------------------------")
        print("You win this round!")
        p+=1
    elif player1==2 and computer==2:
        print("Computer chooses:",hand[computer])
        print("---------------------------------")
        print("Draw!")
    elif player1==2 and computer==3:
        print("Computer chooses:",hand[computer])
        print("---------------------------------")
        print("Computer wins this round.")
        c+=1
    elif player1==3 and computer==1:
        print("Computer chooses:",hand[computer])
        print("---------------------------------")
        print("Computer wins this round.")
        c+=1
    elif player1==3 and computer==2:
        print("Computer chooses:",hand[computer])
        print("---------------------------------")
        print("You win this round!")
        p+=1
    elif player1==3 and computer==3:
        print("Draw!")
    n-=1
if c>p:
    print("Computer wins the game.")
elif p>c:
    print("You win the game.")
else:
    print("Game draw!")
