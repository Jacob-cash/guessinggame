import random   
try:

    guess = int(input("Pick a number between 1 and 10 peasant: "))
    rannum = random.randint(0,10)
    answer = guess
except ValueError:
    print("you did not choose a number , too bad.")
    

while answer != rannum:
    
    guess = int(input("Pick again you guessed wrong peasant: "))
    answer = guess

print("you finally got it peasant")



