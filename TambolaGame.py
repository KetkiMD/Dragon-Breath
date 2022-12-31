import random
n=int(input("\n\t\tEnter number of players min is 2 and max is 9\t:"))
if n>=2 and n<10:


    for i in range(0,n):
        Name = input("\n\t\tEnter Your name\t:")

        print("list of ",Name,"is\t:",random.sample(range(1,100),9))
print("20 numbers are\t:",random.sample(range(1,100),20))
winner=int(input("\n\t\tWhich player win the game\t:")) #Winner is one whose number matches msot in their list and 20 numbered list
print("*****Congrates ",winner," ,you win the game*****")

