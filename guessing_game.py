'''
  Starter Code for number guessing game
  
  Please enter your team members names here:
  name1: Ernesto Cardoso
'''
# Begin your code here
import random
random_numbers= random.randint(1,100)
User_Choice= int(input("Choose a number from 1-100:"))
if User_Choice < 1 or User_Choice > 100:
    print("Use a number between 1 and 100!")
elif User_Choice > random_numbers:
    print("Too low")
elif User_Choice < random_numbers:
    print("Too high")
elif User_Choice== random_numbers:
    print("You Win")