print ("Hello, welcome to my program, peasant. MUAHAHAHAHAHA!")
import random;
name = input("Whats your name?: ")
print(f"Hello {name}")

d100 = [ i for i in range(100)]
d50 = [i for i in range(50)]
d20 = [i for i in range (20)]
d10 = [i for i in range (10)]
d6 = [i for i in range (6)]
d4 = [i for i in range (4)]
d2 = [i for i in range (2)]


def roll() :

    print("Which dice would you like to roll?")
    dice = input("Please type = d100, d50, d10: ")
    print(random.randint(1, len(dice)))
    print("Would you like to roll again?")
    reroll = input("y/n?")

    return reroll

turn = roll()
while turn == 'y':

    turn = roll()
    
exit()
