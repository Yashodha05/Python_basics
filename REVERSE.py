n=int(input("enter a sequence of number"))
rev=0
while n>0:
    rev +=n%10
    n//=10
print(rev)



