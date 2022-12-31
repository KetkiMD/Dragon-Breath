import random
num = random.randint(1, 10)

player_name = input("Hello, Enter your name\t:")
number_of_guesses = 0
print('Welcome ! {} \nLet\'s play a game, I will think a number between 1 and 10 then you will guess, Ok? \nRemember! You have only 3 chances so guess:'.format(player_name))

while number_of_guesses < 3:

    guessed_no = int(input("Enter number\t:"))
    number_of_guesses += 1
    if guessed_no < num:
        print('Your estimate is too low, go up a little!')
    if guessed_no > num:
        print('Your estimate is too high, go down a bit!')
    if guessed_no == num:
        break
if guessed_no == num:
    print('Congratulations {}, you guessed the absolute correct number in {} tries!'.format(player_name, number_of_guesses))
else:
    print('Close but no cigar, you couldn\'t guess the number. \nWell, the number was {}.'.format(num))
