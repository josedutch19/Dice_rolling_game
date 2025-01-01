import random
# Loop
while True:
    choice = input('Roll the dice? (y/n):') # Ask: roll the device?
    if choice == 'y': # If user enters y
         die1 = random.randint(1,6) #   Generate two random umbers
         die2 = random.randint(1,6) #   Generate two random umbers
         print(f'({die1}, {die2})') #   Print them
    elif choice == 'n': # If user enters n
        print('Thanks for playing!') #   Print thank you message 
        break#   Terminate 
else: # Else
    print('Invalid choice!')#   Print invalid choice