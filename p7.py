class BankAccount:
    def __init__(self, balance=0):       
        self.balances = balance
        
    def withdraw(self, amount): 
        if self.balances>=amount: 
            self.balances-=amount 
            print(f"{amount} with draw successfully") 
        else:  
            print("Not enough balance") 
            print("Available Balance :",self.balances) 
         
    def deposit(self,amount): 
        self.balances+=amount  
        print(f"{amount} successfully deposited") 
 
    def balance(self): 
        print(f"The balance is {self.balances}") 
     
account = BankAccount(int(input("Enter the opening balance: ")))   
while True:
    print("\n**BankAccount**") 
    print("Operations\n 1. Withdraw\n 2. Deposit \n 3. Balance \n 4. To Exit") 
    choice = int(input("Choice: ")) 
    if choice == 1:  
        account.withdraw(int(input("Enter the amount: "))) 
    elif choice == 2:  
        account.deposit(int(input("Enter the amount: "))) 
    elif choice == 3:  
        account.balance() 
    else:  
        break 
