import readchar

def get_valid_mobile():
        print("Enter your mobile number: ", end="", flush=True)
        mobile_number = ""

        while len(mobile_number) < 10:  # Ensure max 10 digits
            char = readchar.readkey()

            if char.isdigit():  # Allow only numbers
                print(char, end="", flush=True)  # Show typed number
                mobile_number += char
            elif char == "\r" or char == "\n":  # Prevent Enter key early
                continue
            elif char == "\x08":  # Handle Backspace
                if mobile_number:
                    print("\b \b", end="", flush=True)  # Erase last character
                    mobile_number = mobile_number[:-1]

        print()  # Move to next line
        return mobile_number
        
def enter_pin():
        print("Please enter your 4-digit PIN:  ", end="", flush=True)
        pin = ""

        while len(pin) < 4:  # Ensure max 10 digits
            char = readchar.readkey()

            if char.isdigit():  # Allow only numbers
                print(char, end="", flush=True)  # Show typed number
                pin += char
            elif char == "\r" or char == "\n":  # Prevent Enter key early
                continue
            elif char == "\x08":  # Handle Backspace
                if pin:
                    print("\b \b", end="", flush=True)  # Erase last character
                    pin = pin[:-1]

        print()  # Move to next line
        return pin