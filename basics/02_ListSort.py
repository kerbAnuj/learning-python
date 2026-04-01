#02_ListSort
#Manual list sort
#Code dated 1st of March, 2026

lst = list(eval(input("List:")))
copy = lst.copy()
new = []

for i in copy:
    x = min(lst)
    lst.remove(min(lst)) 
    new.append(x) 

print(new)