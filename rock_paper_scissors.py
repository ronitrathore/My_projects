# Python_Project2 : Rock,Paper,Scissor Game
import random
paper = '''
       ---------
------       -----)-----
                ---------)
                 ---------)
                ---------)
------        -------)
'''
rock = '''
     ------
----'   -----)
       (------)
       (------)
       (-----)
---.---(---)
'''
scissor = '''
      --------
----       -----)-----
                --------)
            -------------)
            (------)
-----______(----)
'''

       
image = [rock,paper,scissor]
user_choice = int(input("Enter your choice : Type '0' for Rock , '1' for Paper , and '2' for Scissor  "))
sys_choice = random.randint(0,2)
print(image[sys_choice])
print("System choice",sys_choice)
print(image[user_choice])
print("User choice",user_choice)
if user_choice>=3 or user_choice< 0:
    print("Invalid Choice,you lose")
else:
    if sys_choice == user_choice:
        print("It's a Tie , play again.")
    elif sys_choice ==0 and user_choice==2:
        print("you lose")
    elif sys_choice ==2 and user_choice==0:
        print("you win")
    elif sys_choice > user_choice:
        print("you lose")
    elif sys_choice < user_choice:
        print("you win")

print("Thank you!")
