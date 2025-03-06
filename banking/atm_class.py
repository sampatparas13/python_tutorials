import pandas as pd
from banking_io import get_user_by_mobile, update_balance_in_excel
from otp_verification import send_otp, verify_otp
from utils import get_valid_mobile, enter_pin

class ATM:
    def __init__(self):
        self.pinTry = 0
        self.user = None
        self.init()
        
    
    def init(self):
        self.pinTry = 0
        self.user = None
        self.authenticate()
    
    def authenticate(self):
        mobile_number = get_valid_mobile()
        self.user = get_user_by_mobile(mobile_number)

        if self.user is None:
            print("❌ Mobile number not found! Please try again.")
            self.authenticate()
            return
        
        self.email = self.user["cust_email"]
        otp = send_otp(self.email)

        if not verify_otp(otp):
            print("Authentication failed. Exiting.")
            return

        print("✅ Authentication successful!")
        self.welcome_screen()
        
    
                
    

    def welcome_screen(self):
        
        print("\nWelcome to Business Bank")
        print("What would you like to do today?")
        print("1. Check balance")
        print("2. Withdraw money")
        print("3. Quick withdrawal")
        print("4. Change PIN")
        print("5. Exit")
        
        self.operation = self.get_valid_input("Selection: ")

        match self.operation:
            case 1:
                if(self.fetchPin()):
                    print("check balance under development")
                    self.welcome_screen()
            case 2:
                if(self.fetchPin()):
                    self.withdrawal_process()
            case 3:
                if(self.fetchPin()):
                    print("Quick withdrawal under development")
                    self.welcome_screen()
            case 4:
                print("PIN change feature coming soon!")
                self.welcome_screen()
            case 5:
                print("Thank you for using the ATM!")
                self.init()
            case _:
                print("Invalid selection!")
                self.init()

    def get_valid_input(self, prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit() and len(user_input) == 1:
                return int(user_input)  # Convert to integer
            else:
                print("Invalid input! Please enter a single digit (1-5).")
    
    def fetchPin(self):
        
        self.pin = enter_pin()
        
        if int(self.pin) != int(self.user["cust_pin"]):
            self.pinTry += 1
            if self.pinTry < 3:
                print(f"❌ Incorrect PIN, {3 - self.pinTry} attempts left.") 
                return self.fetchPin()
            else:
                print("🚫 Your ATM card has been blocked!")
                exit()
        else:
            print("✅ PIN Verified!")
            return True
        return False

    def withdrawal_process(self):
        tmp = input("Enter withdrawal amount: ")
        if tmp == '':
            print("Please enter withdrawal amount")
            self.withdrawal_process()
            return
        amount = int(tmp)
        
        if amount <= int(self.user["cust_balance"]):
            new_balance = int(self.user["cust_balance"]) - amount
            update_balance_in_excel(new_balance, self.user)  # Update in Excel
            print(f"✅ Withdrawal Successful! New Balance: ₹{new_balance}")
            self.init();
        else:
            print("❌ Insufficient balance!")

# Run ATM
atm = ATM()
