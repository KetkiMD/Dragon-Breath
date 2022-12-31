# In this game 1st player is Human
#  And 2nd player is computer
import random

print("------------Welcome to Snake Water Gun game----------")
print("Note : You need to play this game for 5 time")
print("Note : Tou need to write your option in Block letter")
n = 1
sum = 0
somi = 0
JK  = 0
while n < 6:
    print("Enter your choice between Snake Water Gun...")
    ch = str(input("Enter S or W or G\t\t:"))
    p = random.choice("S"  "W"  "G")
    if ch == "S" and p == "S":
        print("Game is tie")
        JK = JK + 1
    elif ch == "s" and p == "W":
        print("Winner is You")
        sum = sum + 1
    elif ch == "S"  and p =="G":
        print("Winner is Computer")
        somi = somi + 1

    if ch == "W" and p == "S":
        print("Winner is Computer")
        somi = somi + 1
    elif ch == "W" and p == "W":
        print("Game is tie")
        JK = JK + 1
    elif ch == "W"  and p =="G":
        print("Winner is You")
        sum = sum + 1

    if ch == "G" and p == "S":
        print("Winner is You")
        sum = sum + 1
    elif ch == "G" and p == "W":
        print("Winner is Computer")
        somi = somi + 1
    elif ch == "G"  and p =="G":
        print("Game is tie")
        JK = JK + 1
    print("---------------------------------------------")
    n +=1



print("---------------------------------------------")
if sum>somi:
    print(f"Your score is {sum} and computer's score s {somi} ")
    print("So Game was tie for %d times"%JK)
    print("So the final winner is...You")

elif sum<somi:
    ll = f"Your score is {sum} and computer's score s {somi} "
    print("So Game was tie for %d times" % JK)
    print("So the final winner is...Computer")
    print(ll)
else:
    print("Final Result : Game is tie")
