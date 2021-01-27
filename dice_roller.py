import random
min_dice=1
max_dice=6
user_inp="yes"

while user_inp=="yes" or user_inp=="y":
    
    print("Rolling the dice...........")
    print("The Values are ......")
    
    print(random.randint(min_dice,max_dice))
          
    print(random.randint(min_dice,max_dice))
          
    user_inp=str(input("Enter you want to roll again ? "))
    
