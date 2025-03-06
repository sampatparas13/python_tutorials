import pandas as pd

def get_user_by_mobile(mobile_number):
        try:
            # Read Excel
            df = pd.read_excel("ATM_Customers.xlsx", dtype={"cust_mobile_number": str})
            # Ensure all mobile numbers are strings and strip spaces
            df["cust_mobile_number"] = df["cust_mobile_number"].astype(str).str.strip()
            
            # Search for the user
            user = df[df["cust_mobile_number"] == mobile_number]

            if user.empty:
                return None  # Mobile number not found
            
            return user.iloc[0].to_dict()  # Convert row to dictionary

        except FileNotFoundError:
            print("❌ Error: ATM_Customers.xlsx file not found!")
            return None
            
def update_balance_in_excel(new_balance, user):
    
    try:
        # Load Excel file
        df = pd.read_excel("ATM_Customers.xlsx", dtype={"cust_mobile_number": str})

        # Find user index
        index = df[df["cust_mobile_number"] == user["cust_mobile_number"]].index

        if not index.empty:
            df.at[index[0], "cust_balance"] = new_balance  # Update balance in DataFrame
            df.to_excel("ATM_Customers.xlsx", index=False)  # Save changes
            print("✅ Account balance updated in database.")
        else:
            print("❌ Error: Unable to update balance in database.")

    except FileNotFoundError:
        print("❌ Error: ATM_Customers.xlsx file not found!")