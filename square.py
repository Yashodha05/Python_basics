#square
#n=int(input("enter a number"))
#for i in range(1,11):
#    print("square of ", i, "is" ,i*i*i)

#factorial
#n=int(input("enter a number"))
#for i in range(1,n):
#    n=n*i
#print(n)

#divisible by 3 and 5
#for i in range(1,50):
 #   if i%3==0 and i%5==0:
  #      print(i)

#prime numbers
#for i in range(1,50):
 #   for j in range(2,i):
  #     if i%j==0:
   #        break
    #else:
     #   print(i, end=" ")

#pattern printing
#for i in range(0,4):
 #   print(" * " * 4)

#number pattern
#n=8
#for i in range(n):
 #   for j in range(n):
  #      print(i,j, end=' ')
   # print()

#0 0 0 1 0 2 0 3 0 4 0 5 0 6 0 7
#1 0 1 1 1 2 1 3 1 4 1 5 1 6 1 7
#2 0 2 1 2 2 2 3 2 4 2 5 2 6 2 7
#3 0 3 1 3 2 3 3 3 4 3 5 3 6 3 7
#4 0 4 1 4 2 4 3 4 4 4 5 4 6 4 7
#5 0 5 1 5 2 5 3 5 4 5 5 5 6 5 7
#6 0 6 1 6 2 6 3 6 4 6 5 6 6 6 7
#7 0 7 1 7 2 7 3 7 4 7 5 7 6 7 7

#border printing
#n=5
#for i in range(n):
 #   for j in range(n):
    #    if i==0 or j==0 or i==n-1 or j==n-1:
     #       print(" * ", end=' ')
      #  else:
       #     print(' ', end=' ')
    #print()

#check box
#n=8
#for i in range(n):
 #   for j in range(n):
  #      if j==0 or i==n-1 or i==0 or j==n-1 or i==j or i+j==n-1:
   #         print("*", end=' ')
    #    else:
     #       print(' ',end=' ')
    #print()


n=9
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==0 or j==n-1 or i==j or i+j==n-1 or i==n//2 or j==n//2 or i+j==n//2 or j-i==n//2 or i-j==n//2 or i+j==n-1:
            print("*" , end=' ')
        else:
            print(' ',end=' ')
    print()