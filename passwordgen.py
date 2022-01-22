#necessary modules for projects
import random
import string

print("Hello, Welcome to the Password generated!")

#define the length of the password 
length = int(input("Enter the length of password:"))

#define the database name
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

#now let's combine the database 
all = lower+upper+num+symbols

#now let's use random 
temp=random.sample(all, length)

#create the password 
password="".join(temp)

#print the password
print(password)