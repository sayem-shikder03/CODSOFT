import random
import string

password_length=int(input("Enter your Password lenght:"))

charValue=string.ascii_letters+string.digits+string.punctuation

password=""

for i in range(password_length):
    password+=random.choice(charValue)


print("Your PASSWORD is:",password)