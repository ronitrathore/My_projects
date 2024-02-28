# Python_Project1 : Password Generator 
import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','@','#','$','%','~','^','&','*','(',')','/','<','>','?','+','-']
print("Welcome to Password Generator!")
no_l=int(input("How many letters do you want in your password? \n"))
no_s=int(input("How many symbols do you want in your password? \n"))
no_n=int(input("How many numbers do you want in your password? \n"))
password =""
    
for i in range(1,no_l+1):
               l = random.choice(Letters)
               password = password + l
for i in range(1,no_s+1):
               s = random.choice(Symbols)
               password = password + s
for i in range(1,no_n+1):
               n = random.choice(Numbers)
               password = password + n
               
print("This is your weak password " ,password)
print("**************************************")
password_list = []
for i in range(1,no_l+1):
               char = random.choice(Letters)
               password_list += char
for i in range(1,no_s+1):
               char = random.choice(Symbols)
               password_list += char
for i in range(1,no_n+1):
               char = random.choice(Numbers)
               password_list += char
random.shuffle(password_list)
#print(password_list)
password =""
for char in password_list:
    password += char
print("This is your strong password",password)
print("Thank you!")

    


