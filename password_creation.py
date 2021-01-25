import random
passlen=int(input("Enter the length : "))
password_char="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@!@#$%^&*"
password="".join(random.sample(password_char,passlen))
print(password)
               
               
               
