import random

# all things that we need .
numbers = "1234567890"
signs = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# find number pf any type :
number_numbers = input("please enter number of numbers : ")
number_signs = input("please enter number of signs : ")
number_charachters = input("please enter number od charachters : ")
# build a password :
# step 1 : build random numbers , signs and characters :
final_numbers = ""
final_signs = ""
final_charachters = ""
for n in range(1, int(number_numbers) + 1):
    final_numbers += str(random.choice(numbers))
for n in range(1, int(number_signs) + 1):
    final_signs += str(random.choice(signs))
for n in range(1, int(number_charachters) + 1):
    final_charachters += str(random.choice(characters))
# step 2 : build final password :
final = final_charachters + final_signs + final_numbers
final1 = list(final)
random.shuffle(final1)
final = "".join(final1)
print("------------------------------------")
print(f">>> your password is : {final}")
