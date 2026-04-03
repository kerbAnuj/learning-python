#04_Prime
#Check prime
#Code dated 3rd April, 2026

prime = True
number = int(input("Number: "))
divisor = 2

if number < 0:
    number = -(number)


while divisor < number and number > 1:
    if number % divisor == 0:
        divisor += 1
        prime = False
    elif number % divisor != 0:
        divisor += 1
        pass
    
if prime and number > 1:
    print("The number is prime.")
elif not prime or number < 2:
    print("The number is not a prime.")
