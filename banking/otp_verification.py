import random
import smtplib

# Setting up the SMTP server
def setup_server():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sampatparasmca@gmail.com", "<your app password>")  # Use App Password
    return server

# Function to validate email format
def email_verification(email):
    email_check1 = ["gmail", "hotmail", "yahoo", "outlook"]
    email_check2 = [".com", ".in", ".org", ".edu", ".co.in"]

    if "@" not in email or not any(domain in email for domain in email_check1) or not any(site in email for site in email_check2):
        print("Invalid email ID. Please enter again.")
        return False
    return True

# Function to send OTP
def send_otp(receiver_email):
    server = setup_server()
    otp = random.randint(100000, 999999)
    
    subject = "OTP Verification for ATM Access"
    body = f"Dear User,\n\nYour OTP is {otp}.\n\nThank you!"
    message = f'Subject:{subject}\n\n{body}'

    server.sendmail("sampatparasmca@gmail.com", receiver_email, message)
    server.quit()

    return otp  # Return the OTP for verification

# Function to verify OTP input
def verify_otp(expected_otp):
    for _ in range(3):  # Give 3 attempts
        entered_otp = input("Enter the OTP sent to your email: ")
        if entered_otp.isdigit() and int(entered_otp) == expected_otp:
            print("✅ OTP Verified!")
            return True
        print("❌ Invalid OTP. Try again.")
    
    print("Too many failed attempts. Exiting.")
    return False
