import pandas as pd

# Sample data for 10 customers
data = {
    "cust_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "cust_name": ["John Doe", "Alice Smith", "Bob Johnson", "Charlie Brown", "David Wilson", 
                  "Emma Watson", "Frank Miller", "Grace Lee", "Henry Adams", "Isla White"],
    "cust_mobile_number": ["9876543210", "9876543211", "9876543212", "9876543213", "9876543214", 
                           "9876543215", "9876543216", "9876543217", "9876543218", "9876543219"],
    "cust_pin": [1234, 2345, 3456, 4567, 5678, 6789, 7890, 8901, 9012, 1122],
    "cust_balance": [10000, 20000, 15000, 5000, 12000, 8000, 7000, 18000, 22000, 9000],
    "last_updated": ["2025-03-05", "2025-03-04", "2025-03-03", "2025-03-02", "2025-03-01",
                     "2025-02-28", "2025-02-27", "2025-02-26", "2025-02-25", "2025-02-24"],
    "account_number": ["123456789012", "123456789013", "123456789014", "123456789015", "123456789016", 
                       "123456789017", "123456789018", "123456789019", "123456789020", "123456789021"],
    "account_type": ["Savings", "Current", "Savings", "Savings", "Current", 
                     "Savings", "Current", "Savings", "Savings", "Current"],
    "branch_name": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad", 
                    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"],
    "last_transaction_amount": [500, 1000, 200, 1500, 300, 700, 400, 600, 2000, 250],
    "last_transaction_type": ["Withdrawal", "Deposit", "Withdrawal", "Deposit", "Withdrawal", 
                              "Deposit", "Withdrawal", "Deposit", "Withdrawal", "Deposit"],
    "failed_login_attempts": [0, 1, 0, 2, 0, 3, 1, 0, 0, 2],
    "account_status": ["Active", "Active", "Active", "Blocked", "Active", 
                       "Blocked", "Active", "Active", "Active", "Blocked"],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel file
file_path = r"F:\Paras\Python\banking\ATM_Customers.xlsx"  # Use a valid path
df.to_excel(file_path, index=False)

# Return file path
file_path
