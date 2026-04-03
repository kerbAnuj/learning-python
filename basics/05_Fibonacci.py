#05_Fibonacci
#Fibonacci sequence generation
#Code dated 3rd of April, 2026

f0 = 0
f1 = 1
fout = int(input("How many numbers? :"))
i = 1
fout -= 2

if fout == -2:
    pass
elif fout == -1:
    print(f0, end = " ")
elif fout > -1:
    print(f0, end = " ")
    print(f1, end = " ")

while i <= fout and fout>0:
    fnum = f0 + f1
    print(fnum, end=" ")
    f0 = f1
    f1 = fnum
    i += 1



