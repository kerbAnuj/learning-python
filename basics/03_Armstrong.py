#03_Armstrong
#Big Neil Armstrog
#Code dated 1st April, 2026

num = int(input("Number: "))
copy = num
sm = 0
n = len(str(num))

while num>0:
    rem = num % 10
    sm += rem ** n
    num //= 10

if sm == copy:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


