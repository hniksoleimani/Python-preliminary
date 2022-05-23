theboard={'7':' ','8':' ','9':' '
                ,'4':' ','5':' ','6':' '
                ,'1':' ','2':' ','3':' '}

board_key=[]
for key in theboard:
    board_key.append(key)
def printboard(theboard):
    print(theboard['7']+'|'+theboard['8']+'|'+theboard['9'])
    print('-+-')
    print(theboard['4']+'|'+theboard['5']+'|'+theboard['6'])
    print('-+-')
    print(theboard['1']+'|'+theboard['2']+'|'+theboard['3'])
 
          
def game():
    turn="x"
    count=0
    while count<10:
        printboard(theboard)
        print("its your turn:",turn)
        move=input("move to which place?")
        if theboard[move]==" ":
            theboard[move]=turn
            count+=1
        else:
            print("That tile is already taken.")
            continue
        if count>=5:
            if theboard["1"]==theboard["2"]==theboard["3"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
            if theboard["3"]==theboard["5"]==theboard["7"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
            if theboard["1"]==theboard["2"]==theboard["3"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
            if theboard["4"]==theboard["5"]==theboard["6"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
            if theboard["7"]==theboard["8"]==theboard["9"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
            if theboard["1"]==theboard["4"]==theboard["7"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
            if theboard["2"]==theboard["5"]==theboard["8"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
            if theboard["3"]==theboard["6"]==theboard["9"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
            if theboard["1"]==theboard["5"]==theboard["9"] !=" ":
                print(theboard)
                print("**********************"+turn+" won****************")
                break
    if count==9:
        printboard(theboard)
        print("Game over.")
        break
    if turn== "x":
        turn="o"
    else:
        turn="x"
    restart=input("Do you want to play again?(y/n)")
    if restart=="y":
        for key in board_key:
            theboard[key]=" "
            game()
game()

