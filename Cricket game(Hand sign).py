 # Cricket Game
 # Made by Vivek Nishad
print(""" ~~~~~~~~~~ Game of Cricket ~~~~~~~~~~

Instructions:
1. You have to chose between head/tails for the toss.
2. If you won the toss chose bat/bowl.
2. You have to select any random number from 1 to 6.
2. The computer will also select a number.
3. While batting, if the number selected by you and computer is different, then your number will add to your runs.
   If the number selected by you and computer is same, then you will lose your wicket.
4. While bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
   If the number selected by you and computer is same, then the computer will lose its wicket.
5. Each player will get 2 wickets and 2 overs (12 balls) for batting and bowling.
6. The innings will end after either the two wickets fell or the overs end.
7. The player with maximum runs wins. """)

print("\n---------- Start Game ----------")

import random


print("Lets do the toss")
toss_call = input("Chose (H) for heads/ (T) for tails: ").upper()   #Asking for the toss
toss = ["H", "T"]
val = random.choice(toss)
Runs = 0
Wickets = 0
Balls = 0
if val == toss_call:      
    print("Congratulations you won the toss")
    option = input("Chose what you want to do first bat/bowl : ").lower()    # Asking the user to chose bat or bowl
    if option == "bat":
        print("Let's start the first innings:")
        while Wickets < 2 and Balls < 12:
            p_chose = int(input("Enter a number between 1 to 6 : "))
            c_chose=random.randint(1,6)
            while not(1<=p_chose <=6):         #If user inputs a invaild number from games condition
                p_chose = int(input("Please enter a value from 1-6 \nEnter a number between 1 to 6 : "))
            print("Your choice is ", p_chose)
            print("Computers choice is ", c_chose)
            if p_chose == c_chose:
                Balls += 1
                Wickets += 1
                Runs += 0
                print("Score=", Runs, "/", Wickets)
                print("Balls bowled: ", Balls)
            elif p_chose != c_chose:
                Balls += 1
                Runs += p_chose
                Wickets += 0
                print("Score=", Runs, "/", Wickets)
                print("Balls bowled: ", Balls)
            else:
                print("Read The Game rule correctly You can't enter number other than 1-6 sorry restart the game")
        print("Your total Score=", Runs, "/", Wickets)
        wik = 0
        ri = 0
        ba = 0
        print("Now it's your turn to bowl ")
        while wik < 2 and ba < 12:
            p_chose = int(input("Enter a number between 1 to 6 : "))
            c_chose = random.randint(1, 6)
            while not(1<=p_chose <=6):
                p_chose = int(input("Please enter a value from 1-6 \nEnter a number between 1 to 6 : "))
            print("Your choice is ", p_chose)
            print("Computers choice is ", c_chose)
            if p_chose == c_chose:
                ba += 1
                wik += 1
                ri += 0
                print("Score=", ri, "/", wik)
                print("Balls bowled: ", ba)
            elif p_chose != c_chose:
                ba += 1
                ri += c_chose
                wik += 0
                print("Score=", ri, "/", wik)
                print("Balls bowled: ", ba)
                if ri > Runs:
                    print("!!YOU LOSE BETTER LUCK NEXT TIME!!")
                    break
                elif wik == 2:
                    print("!!Congratulations you won the match!!")
                    break
            else:
                print("Read The Game rule correctly You can't enter number other than 1-6 sorry restart the game")
        if ri < Runs:
            print("!!Congratulations you won the match!!")
        else:
            pass
    elif option == "bowl":
        print("Let's start the game:")
        while Wickets < 2 and Balls < 12:
            p_chose = int(input("Enter a number between 1 to 6 : "))
            c_chose = random.randint(1, 6)
            while not(1<=p_chose <=6):
                p_chose = int(input("Please enter a value from 1-6 \nEnter a number between 1 to 6 : "))
            print("Your choice is ", p_chose)
            print("Computers choice is ", c_chose)
            if p_chose == c_chose:
                Balls += 1
                Wickets += 1
                Runs += 0
                print("Score=", Runs, "/", Wickets)
                print("Balls bowled: ", Balls)
            elif p_chose != c_chose:
                Balls += 1
                Runs += c_chose
                Wickets += 0
                print("Score=", Runs, "/", Wickets)
                print("Balls bowled: ", Balls)
            else:
                print("Read The Game rule correctly You can't enter number other than 1-6 sorry restart the game")
        print("Computers total Score=", Runs, "/", Wickets)
        wik = 0
        ri = 0
        ba = 0
        print("Now it's your turn to bat ")
        while wik < 2 and ba < 12:
            p_chose = int(input("Enter a number between 1 to 6 : "))
            c_chose = random.randint(1, 6)
            while not(1<=p_chose <=6):
                p_chose = int(input("Please enter a value from 1-6 \nEnter a number between 1 to 6 : "))
            print("Your choice is ", p_chose)
            print("Computers choice is ", c_chose)
            if p_chose == c_chose:
                ba += 1
                wik += 1
                ri += 0
                print("Score=", ri, "/", wik)
                print("Balls bowled: ", ba)
            elif p_chose != c_chose:
                ba += 1
                ri += p_chose
                wik += 0
                print("Score=", ri, "/", wik)
                print("Balls bowled: ", ba)
                if ri > Runs:
                    print("!!Congratulations you won the match!!")
                    break
                elif wik == 2:
                    print("!!YOU LOSE BETTER LUCK NEXT TIME!!")
                    break
                else:
                    pass
            else:
                print("Read The Game rule correctly You can't enter number other than 1-6 sorry restart the game")
        print("Your total Score=", ri, "/", wik)
        if ri > Runs:
            print("Computer won the match, Better luck next time")
        else:
            pass

    else:
        print("Please provide a correct information: ")
elif val != toss_call:
    print("Computer won the toss and decided to bat first")
    print("Lets begin the first innings")
    while Wickets < 2 and Balls < 12:
        p_chose = int(input("Enter a number between 1 to 6 : "))
        c_chose = random.randint(1, 6)
        while not(1<=p_chose <=6):
                p_chose = int(input("Please enter a value from 1-6 \nEnter a number between 1 to 6 : "))
        print("Your choice is ", p_chose)
        print("Computers choice is ", c_chose)
        if p_chose == c_chose:
            Balls += 1
            Wickets += 1
            Runs += 0
            print("Score=", Runs, "/", Wickets)
            print("Balls bowled: ", Balls)
        elif p_chose != c_chose:
            Balls += 1
            Runs += c_chose
            Wickets += 0
            print("Score=", Runs, "/", Wickets)
            print("Balls bowled: ", Balls)
        else:
            print("Read The Game rule correctly You can't enter number other than 1-6 sorry restart the game")
    print("Computers total Score=", Runs, "/", Wickets)
    wik = 0
    ri = 0
    ba = 0
    print("Now it's your turn to bat ")
    while wik < 2 and ba < 12:
        p_chose = int(input("Enter a number between 1 to 6 : "))
        c_chose = random.randint(1, 6)
        while not(1<=p_chose <=6):
                p_chose = int(input("Please enter a value from 1-6 \nEnter a number between 1 to 6 : "))
        print("Your choice is ", p_chose)
        print("Computers choice is ", c_chose)
        if p_chose == c_chose:
            ba += 1
            wik += 1
            ri += 0
            print("Score=", ri, "/", wik)
            print("Balls bowled: ", ba)
        elif p_chose != c_chose:
            ba += 1
            ri += p_chose
            wik += 0
            print("Score=", ri, "/", wik)
            print("Balls bowled: ", ba)
            if ri > Runs:
                print("!!Congratulations you won the match!!")
                break
            elif wik == 2:
                print("!!YOU LOSE BETTER LUCK NEXT TIME!!")
                break
            else:
                pass
        else:
            print("Read The Game rule correctly You can't enter number other than 1-6 sorry restart the game")
    print("Your total Score=", ri, "/", wik)
    if ri < Runs:
        print("Computer won the match, Better luck next time")
    else:
        pass
else:
    print("Please provide a valid entry from heads/tails Restart The game")
