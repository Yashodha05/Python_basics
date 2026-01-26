#balance= 5000
#amt=user_input
#more than 5000- invalid amt(warning)
#50, 70, 150, 170- warning: amt should be multiple of 100, 200, 500
#amt=500, 800, 1000
# with drawl successful
#show the new balance
balance=5000
print("present balance",balance)
amt=int(input("enter amount"))
if amt>balance:
    print("invalid amount")
elif amt%100!=0:
    print("warning:amount should be multiple of 100, 200, 500")
else:
    print("with drawl successful")
    present_balance=balance-amt
    print("present balance", present_balance)
